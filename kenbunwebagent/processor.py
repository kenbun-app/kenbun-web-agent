from multiprocessing import Process

from kenbundata.storage.factory import create_storage
from kenbundata.types import Url

from .drivers.factory import create_web_agent
from .settings import GlobalSettings


class Processor(Process):
    def __init__(self, url: Url, settings: GlobalSettings):
        super(Processor, self).__init__()
        self._url = url
        self._settings = settings

    def run(self) -> None:
        driver = create_web_agent(settings=self._settings, target_url=self._url)
        storage = create_storage(settings=self._settings.data_global_settings)
        storage.store_url(url=self._url)
        with driver:
            storage.store_blob(blob=driver.dump_har())
            storage.store_screenshot(screenshot=driver.take_full_screenshot())
