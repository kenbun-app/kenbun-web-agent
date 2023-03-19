from typing import cast

from kenbundata.types import Url
from pydantic import AnyHttpUrl

from kenbunwebagent.drivers.factory import create_web_agent
from kenbunwebagent.drivers.firefox_wire.core import FirefoxWireAgent
from kenbunwebagent.settings import DriverType, GlobalSettings


def test_factory_returns_firefox_wire_driver() -> None:
    target_url = Url(url=cast(AnyHttpUrl, "https://example.com"))
    settings = GlobalSettings(driver_type=DriverType.FIREFOX_WIRE)
    agent = create_web_agent(settings=settings, target_url=target_url)
    assert isinstance(agent, FirefoxWireAgent)
    assert agent.target_url == target_url
