from comando import saudacao

def test_saudacao():
    assert saudacao("João") == "Olá, João!"
    assert saudacao("Maria") == "Olá, Maria!"
    assert saudacao("Ana") == "Olá, Ana!"

test_saudacao()