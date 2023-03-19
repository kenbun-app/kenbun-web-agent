from abc import ABCMeta, abstractmethod
from types import TracebackType
from typing import Optional, Type, TypeVar

from kenbundata.types import Blob, Screenshot, Url

T = TypeVar("T", bound="BaseWebDriver")


class BaseWebDriver(metaclass=ABCMeta):
    def __init__(self, target_url: Url):
        self._target_url = target_url

    @abstractmethod
    def _init_driver(self) -> None:
        ...

    @abstractmethod
    def _quit_driver(self) -> None:
        ...

    @abstractmethod
    def take_full_screenshot(self) -> Screenshot:
        ...

    @abstractmethod
    def dump_har(self) -> Blob:
        ...

    @property
    def target_url(self) -> Url:
        return self._target_url

    def __enter__(self: T) -> T:
        self._init_driver()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        excinst: Optional[BaseException],
        exctb: Optional[TracebackType],
    ) -> None:
        self._quit_driver()
        return None
