from elevador import Elevador

def test_full_name():
    name = "Kelly Frazão"
    std_name = Elevador.standardize(name)
    assert len(std_name.split(' ')) > 1