from kenbundata.types import Url

from ..base import BaseWebDriver
from ..drivers.firefox_wire.core import FirefoxWireAgent
from ..drivers.firefox_wire.settings import FirefoxWireSettings
from ..settings import DriverType, GlobalSettings


def create_web_agent(settings: GlobalSettings, target_url: Url) -> BaseWebDriver:
    if settings.driver_type == DriverType.FIREFOX_WIRE:
        FirefoxWireSettings.from_global_settings(settings=settings)
        return FirefoxWireAgent(target_url=target_url)
    else:
        raise ValueError(f"Unknown driver type: {settings.driver_type}")
