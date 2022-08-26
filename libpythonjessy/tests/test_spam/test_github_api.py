from unittest.mock import Mock

import pytest

from libpythonjessy import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/33210748?v=4'
    resp_mock.json.return_value = {
        'login': 'jessica', 'id': 33210748,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonjessy.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('jessica')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('jessicabferreira')
    assert 'https://avatars.githubusercontent.com/u/101604106?v=4' == url
