import pytest
from matematica.Calculadora import soma,sub,multiplicacao,divisao,media_lista_valores
import numpy as np

@pytest.mark.op_simples
@pytest.mark.positivos
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 12 == soma(v1,v2)

@pytest.mark.op_simples
@pytest.mark.negativos
def test_soma_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    assert -12 == soma(v1,v2)

@pytest.mark.op_simples
@pytest.mark.positivos
def test_soma_dois_valores_iguais():
    v1 = 5.0
    v2 = 5.0
    assert 10 == soma(v1,v2)

@pytest.mark.op_simples
@pytest.mark.negativos
def test_soma_dois_valores_iguais_negativos():
    v1 = -5.0
    v2 = -5.0
    assert -10 == soma(v1,v2)

@pytest.mark.op_simples
@pytest.mark.positivos
def test_sub_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert -2 == sub(v1,v2)

@pytest.mark.op_simples
@pytest.mark.negativos
def test_sub_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    assert 2 == sub(v1,v2)

@pytest.mark.op_simples
@pytest.mark.positivos
def test_sub_dois_valores_iguais():
    v1 = 5.0
    v2 = 5.0
    assert 0 == sub(v1,v2)

@pytest.mark.op_simples
@pytest.mark.negativos
def test_sub_dois_valores_iguais_negativos():
    v1 = -5.0
    v2 = -5.0
    assert 0 == sub(v1,v2)

@pytest.mark.op_simples
@pytest.mark.positivos
def test_multiplicacao_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 35 == multiplicacao(v1,v2)

@pytest.mark.op_simples
@pytest.mark.negativos
def test_multiplicacao_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    assert 35 == multiplicacao(v1,v2)

@pytest.mark.op_simples
@pytest.mark.positivos
def test_multiplicacao_dois_valores_iguais():
    v1 = 5.0
    v2 = 5.0
    assert 25 == multiplicacao(v1,v2)

@pytest.mark.op_simples
@pytest.mark.negativos
def test_multiplicacao_dois_valores_iguais_negativos():
    v1 = -5.0
    v2 = -5.0
    assert 25 == multiplicacao(v1,v2)

@pytest.mark.op_simples
@pytest.mark.positivos
def test_divisao_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 0.7142857142857143 == divisao(v1,v2)

@pytest.mark.op_simples
@pytest.mark.negativos
def test_divisao_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    assert 0.7142857142857143 == divisao(v1,v2)

@pytest.mark.op_simples
@pytest.mark.positivos
def test_divisao_dois_valores_iguais():
    v1 = 5.0
    v2 = 5.0
    assert 1 == divisao(v1,v2)

@pytest.mark.op_simples
@pytest.mark.exercicio_1
def test_divisao_por_0():
    v1 = 5.0
    v2 = 0.0
    assert np.inf == divisao(v1,v2)
        

@pytest.mark.op_simples
@pytest.mark.negativos
def test_divisao_dois_valores_iguais_negativos():
    v1 = -5.0
    v2 = -5.0
    assert 1 == divisao(v1,v2)

@pytest.mark.op_complexa
@pytest.mark.positivos
def test_media_lista_valores_positivos():
    v = [1,2,3,4,5]
    assert 3 == media_lista_valores(v)

@pytest.mark.op_complexa
@pytest.mark.negativos
def test_media_lista_valores_negativos():
    v = [-1,-2,-3,-4,-5]
    assert -3 == media_lista_valores(v)

@pytest.mark.op_complexa
@pytest.mark.positivos
def test_media_lista_valores_iguais():
    v = [1,1,1,1,1]
    assert 1 == media_lista_valores(v)  

@pytest.mark.op_complexa
@pytest.mark.negativos
def test_media_lista_valores_iguais_negativos():
    v = [-1,-1,-1,-1,-1]
    assert -1 == media_lista_valores(v)

@pytest.mark.op_complexa
@pytest.mark.positivos
def test_media_lista_valores_um_valor():
    v = [1]
    assert 1 == media_lista_valores(v)

@pytest.mark.op_complexa
@pytest.mark.negativos
def test_media_lista_valores_um_valor_negativo():
    v = [-1]
    assert -1 == media_lista_valores(v)

@pytest.mark.op_complexa
@pytest.mark.exercicio_1
def test_media_lista_com_string():
    v = [1,"b",2,3,4]
    assert 2.5 == media_lista_valores(v)

@pytest.mark.op_complexa
@pytest.mark.exercicio_1
def test_media_lista_vazia():
    v = []
    assert 0 == media_lista_valores(v)