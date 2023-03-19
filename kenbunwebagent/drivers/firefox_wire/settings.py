from ...settings import GlobalSettings
from ..settings import BaseDriverSettings


class FirefoxWireSettings(BaseDriverSettings):
    @classmethod
    def from_global_settings(cls: type["FirefoxWireSettings"], settings: GlobalSettings) -> "FirefoxWireSettings":
        return cls()
