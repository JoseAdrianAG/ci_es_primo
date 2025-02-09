'''asd'''
import src.funcions as es_primo

def test_primo_1():
    '''asd'''
    assert es_primo.es_primo(1) is False

def test_es_primo_numero_primo():
    '''asd'''
    assert es_primo.es_primo(2) is True

def test_es_primo_negativo():
    '''asd'''
    assert es_primo.es_primo(-10) is False

def test_es_primo_numero_primo_mayor_2():
    '''asd'''
    assert es_primo.es_primo(29) is True
