from unittest.mock import Mock

import pytest

from libpythonjessy import github_api

@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/33210748?v=4'
    resp_mock.json.return_value = {
        'login': 'jessica', 'id': 33210748,
        'avatar_url': url,
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.request.get = get_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('jessica')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('Jessicabferreira')
    assert 'https://avatars.githubusercontent.com/u/101604106?v=4' == url
