import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--url", default="https://api.spacexdata.com/v3/", help="This is request url")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")

