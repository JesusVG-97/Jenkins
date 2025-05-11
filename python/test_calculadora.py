import pytest
import calculadora

def test_suma():
    assert calculadora.suma(3, 4) == 7

def test_resta():
    assert calculadora.resta(10, 5) == 5

def test_multiplica():
    assert calculadora.multiplica(2, 3) == 6

def test_divide():
    assert calculadora.divide(10, 2) == 5

def test_divide_por_cero():
    with pytest.raises(ValueError):
        calculadora.divide(10, 0)
