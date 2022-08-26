from unittest.mock import Mock

import pytest

from libpythonjessy.spam.enviador_de_email import Enviador
from libpythonjessy.spam.main import EnviadorDeSpam
from libpythonjessy.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Jessica', email='jessiferreira.contato@gmail.com'),
            Usuario(nome='Pedro', email='jessiferreira.contato@gmail.com')
        ],
        [
            Usuario(nome='Jessica', email='jessiferreira.contato@gmail.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'jessiferreira.contato@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Jessica', email='jessiferreira.contato@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'pedroferreira.contato@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'pedroferreira.contato@gmail.com',
        'jessiferreira.contato@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )