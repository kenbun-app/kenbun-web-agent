from abc import ABCMeta, abstractmethod
from collections.abc import Mapping
from enum import Enum
from typing import Any, TypeVar

from kenbundata.settings import BaseSettings
from kenbundata.settings import GlobalSettings as DataGlobalSettings

S = TypeVar("S", bound="BaseSettings")


class DriverType(str, Enum):
    FIREFOX_WIRE = "firefox_wire"


class GlobalSettings(BaseSettings):
    data_global_settings: DataGlobalSettings = DataGlobalSettings()
    driver_type: DriverType = DriverType.FIREFOX_WIRE
    driver_settings: Mapping[str, Any] = {}


class BaseComponentSettings(BaseSettings, metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def from_global_settings(cls: type[S], settings: GlobalSettings) -> S:
        raise NotImplementedError
