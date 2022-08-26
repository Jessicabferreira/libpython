from libpythonjessy.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Jessica', email='jessiferreira.contato@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios( sessao):
    usuarios = [
        Usuario(nome='Jessica', email='jessiferreira.contato@gmail.com'),
        Usuario(nome='Pedro', email='jessiferreira.contato@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()