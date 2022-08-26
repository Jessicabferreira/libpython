import pytest as pytest

from libpythonjessy.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['jessi.contato@gmail.com', 'jessiferreira.contato@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()

    resultado = enviador.enviar(
        '%s' % remetente,
        'pedroferreira.contato@gmail.com',
        'Cursos Python Pro',
        'Primeira turma aberta.'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'jessiferreira']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            '%s' % remetente,
            'pedroferreira.contato@gmail.com',
            'Cursos Python Pro',
            'Primeira turma aberta.'
    )