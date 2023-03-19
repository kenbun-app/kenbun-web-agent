from typing import Optional

from kenbundata.fields import Bytes, EncodedImage, MimeType
from kenbundata.types import Blob, Screenshot, Url
from selenium.webdriver.firefox.options import Options
from seleniumwire import webdriver

from ...base import BaseWebDriver


class FirefoxWireAgent(BaseWebDriver):
    def __init__(self, target_url: Url):
        super(FirefoxWireAgent, self).__init__(target_url=target_url)
        self._driver: Optional[webdriver.Firefox] = None

    def _init_driver(self) -> None:
        options = Options()
        options.headless = True
        self._driver = webdriver.Firefox(options=options, seleniumwire_options={"enable_har": True})
        self._driver.get(self.target_url.url)

    def _quit_driver(self) -> None:
        if self._driver is not None:
            self._driver.quit()

    def take_full_screenshot(self) -> Screenshot:
        if self._driver is None:
            raise RuntimeError("Driver is not initialized")
        return Screenshot(encoded_image=EncodedImage(self._driver.get_full_page_screenshot_as_base64()))

    def dump_har(self) -> Blob:
        if self._driver is None:
            raise RuntimeError("Driver is not initialized")
        return Blob(data=Bytes(self._driver.har.encode("utf-8")), mime_type=MimeType("application/json"))
