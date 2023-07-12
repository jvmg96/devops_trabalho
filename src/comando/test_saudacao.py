from comando import saudacao

def teste():
    assert saudacao("João") == "Olá, João!"
    assert saudacao("Maria") == "Olá, Maria!"
    assert saudacao("Ana") == "Olá, Ana!"

teste()