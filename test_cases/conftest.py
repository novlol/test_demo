import pytest
import requests


@pytest.fixture
def base_url():
    return "https://www.baidu.com"


@pytest.fixture
def session():
    return requests.Session()
