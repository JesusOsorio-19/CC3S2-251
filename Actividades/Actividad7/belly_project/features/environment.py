from src.belly import Belly, BellyForTesting
from unittest.mock import MagicMock

def before_scenario(context, scenario):
    fake_clock = MagicMock()
    fake_clock.get_current_time.return_value = 123456.78

    # tags para el ejercicio de escalabilidad
    # si el escenario tiene la etiqueta 'escalabilidad', usamos BellyForTesting
    if 'escalabilidad' in scenario.tags:
        context.belly = BellyForTesting(clock_service=fake_clock)
        print("Modo de prueba: se ignora el limite de 100 pepinos.")
    else:
        context.belly = Belly(clock_service=fake_clock)

"""
# features/environment.py

from unittest.mock import MagicMock
from src.belly import Belly
import time

def before_scenario(context, scenario):
    # Creamos un mock del reloj para poder simular tiempo
    fake_clock = MagicMock()
    # Valor inicial del reloj
    initial_time = 10000.0
    fake_clock.return_value = initial_time
    
    context.current_time = initial_time

    def advance_time(hours):
        # Convierte horas a segundos
        context.current_time += (hours * 3600)
        fake_clock.return_value = context.current_time

    context.advance_time = advance_time

    # Instanciamos Belly con el servicio de reloj mockeado
    context.belly = Belly(clock_service=fake_clock)
    context.exception = None

def after_scenario(context, scenario):
    # Limpieza al final del escenario
    pass

"""