import pytest
from src.belly import Belly, BellyForTesting
from unittest.mock import MagicMock
# test: grunir si cumple condiciones
def test_gruñir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True

def test_comer_pepinos_fraccionarios():
    belly = Belly()
    belly.comer(2.5)
    belly.esperar(1.0)  
    assert belly.pepinos_comidos == 2.5, "El número de pepinos comidos no es correcto."
    assert belly.esta_gruñendo() == False, "El estómago no debería gruñir."

def test_comer_pepinos_fraccionarios_y_grunir():
    belly = Belly()
    belly.comer(17.5)
    belly.esperar(1.5)  
    assert belly.pepinos_comidos == 17.5, "El número de pepinos comidos no es correcto."
    assert belly.esta_gruñendo() == True, "El estómago debería gruñir."

def test_comer_pepinos_negativos():
    belly = Belly()
    with pytest.raises(ValueError):
        belly.comer(-5)  # Lanzar un error al intentar comer pepinos negativos

def test_comer_pepinos_excesivos():
    belly = Belly()
    with pytest.raises(ValueError):
        belly.comer(150)  # Lanzar un error al intentar comer más de 100 pepinos
    
def test_grandes_cantidades():
    belly = BellyForTesting()  # Usamos la versión para pruebas
    belly.comer(1000)
    belly.esperar(10)
    assert belly.esta_gruñendo()

def test_pepinos_comidos():
    belly = Belly()
    belly.comer(10)
    belly.comer(5)
    assert belly.pepinos_comidos == 15 # Devolver el total de pepinos comidos

def test_pepinos_fraccionarios():
    belly = Belly()
    belly.comer(0.5)
    belly.comer(1.5)
    assert belly.pepinos_comidos == 2.0 

def test_estomago_gruñendo():
    belly = Belly()
    belly.comer(20)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True

def test_estomago_predecir_gruñido():
    belly = Belly()
    assert belly.predecir_gruñido(12, 2) == True
    assert belly.predecir_gruñido(8, 2) == False
    assert belly.predecir_gruñido(15, 1) == False

def test_reloj_simulado():
    fake_clock = MagicMock()
    fake_clock.get_current_time.return_value = 12345.67

    belly = Belly(clock_service=fake_clock)
    belly.esperar(1)  # Acción que usará el reloj si lo incluiste como debug

    # Aseguramos que se llamó al reloj
    fake_clock.get_current_time.assert_called_once()