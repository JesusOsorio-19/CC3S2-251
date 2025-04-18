# src/belly.py
from src.clock import ClockService

class Belly:
    def __init__(self, clock_service=None):
        # Inicializamos el reloj si se proporciona un servicio de reloj
        self.pepinos_comidos = 0.0
        self.tiempo_esperado = 0.0
        self.clock_service = clock_service or ClockService()       # Si no se proporciona un servicio de reloj, usamos el reloj real

    def reset(self):
        self.pepinos_comidos = 0.0
        self.tiempo_esperado = 0.0

    def comer(self, pepinos):
        print(f"He comido {pepinos} pepinos.")
        if pepinos < 0 or pepinos > 100:
            raise ValueError("Cantidad no válida de pepinos. Debe ser entre 0 y 100.")
       
        self.pepinos_comidos += float(pepinos)

    def esperar(self, tiempo_en_horas):
        self.tiempo_esperado += tiempo_en_horas
        if self.clock_service:
            self.clock_service.get_current_time() # Simula el avance del tiempo
            

    def esta_gruñendo(self):
        # Verificar que ambas condiciones se cumplan correctamente:
        # Se han esperado al menos 1.0 hora Y se han comido más de 10 pepinos
        if self.tiempo_esperado >= 1.0 and self.pepinos_comidos > 10:
            return True
        return False
    
    def predecir_gruñido(self, pepinos, horas):
        return horas >= 1.5 and pepinos > 10
    
    # test: pepinos restantes para grunir
    def pepinos_restantes_para_grunir(self):
        if self.esta_gruñendo():
            return 0
        elif self.tiempo_esperado >= 1.0:
            faltan = max(0, 11 - self.pepinos_comidos)
            return int(faltan)
        else:
            return "esperar más"

# clase BellyForTesting es una versión de Belly para pruebas de comer 1000 pepinos
class BellyForTesting(Belly):
    def __init__(self, clock_service=None):
        super().__init__(clock_service)
    def comer(self, pepinos):
        if pepinos < 0:
            raise ValueError("Cantidad no válidad de pepinos")
        self.pepinos_comidos += pepinos