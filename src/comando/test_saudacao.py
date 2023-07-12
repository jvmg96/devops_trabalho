# from src.comando import saudacao

# print(saudacao("João"))
# print(saudacao("Maria"))
# print(saudacao("Ana"))

from comando import stringstd


def test_full_name():
    name = "Kelly Frazão"
    std_name = stringstd.standardize(name)
    assert len(std_name.split(' ')) > 1