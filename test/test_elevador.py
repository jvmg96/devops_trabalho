from src import Elevador

def test_entrar():
    elevador = Elevador(7, 0, 8, 0)
    elevador.entrar()
    assert elevador.pessoasDentro == 1

def test_sair():
    elevador = Elevador(7, 0, 8, 1)
    elevador.sair()
    assert elevador.pessoasDentro == 0

def test_subir():
    elevador = Elevador(7, 0, 8, 0)
    elevador.subir()
    assert elevador.andarAtual == 1

def test_descer():
    elevador = Elevador(7, 1, 8, 0)
    elevador.descer()
    assert elevador.andarAtual == 0