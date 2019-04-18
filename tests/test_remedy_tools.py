import pytest

import remedy_tools


def test_Client_init():
    test_client = remedy_tools.Client(
        'http://test.com', 'C:/Users/admin/chromedriver.exe')
    assert test_client.link == 'http://test.com'
    assert test_client.driver == 'C:/Users/admin/chromedriver.exe'
