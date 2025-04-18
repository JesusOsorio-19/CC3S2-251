from behave import given, when, then, step, register_type
import re
from parse_type import TypeBuilder
import parse
import random
from src.belly import Belly

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        
        numeros_esp = {
            "cero": 0, "uno": 1, "una":1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete":17, "dieciocho":18, "diecinueve":19, "veinte":20,
            "treinta": 30, "cuarenta":40, "cincuenta":50, "sesenta":60, "setenta":70,
            "ochenta":80, "noventa":90, "media": 0.5
        }
        numeros_ing = {
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
            "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
            "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
            "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
            "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "half": 0.5
        }
        return numeros_esp.get(palabra.lower(), numeros_ing.get(palabra.lower(), 0))

def obtener_tiempo_aleatorio(rango):
    match = re.match(r"entre (\d+) y (\d+)", rango)
    if match:
        min_horas = int(match.group(1))
        max_horas = int(match.group(2))
        return random.uniform(min_horas, max_horas)
    else:
        raise ValueError(f"Rango de tiempo no válido: {rango}")

# captura de números enteros o decimales, positivos o negativos    
# y los convierte a float
@parse.with_pattern(r"\-?\d+(?:\.\d+)?")
def parse_float(text):
    return float(text)

register_type(Number=parse_float)

@given('que he comido {cukes:Number} pepinos')
def step_given_eaten_cukes(context, cukes):
    try:
        context.belly.comer(cukes)
        context.exception = None # Si no hay excepción, se establece en None
    except ValueError as e:
        context.exception = e
        
@when('he comido {cukes:Number} pepinos más')
def step_when_eaten_more_cukes(context, cukes):
    context.belly.comer(cukes)

@then('debería haber comido {expected:Number} pepinos')
def step_then_should_have_eaten(context, expected):
    assert context.belly.pepinos_comidos == expected, \
        f"Se esperaba haber comido {expected} pepinos, pero comí {context.belly.pepinos_comidos}."    

@when('espero un tiempo aleatorio entre {min_time} y {max_time} horas')
def step_when_wait_random_time(context, min_time, max_time):
    rango = f"entre {min_time} y {max_time} horas"
    tiempo_aleatorio = obtener_tiempo_aleatorio(rango)
    print(f"Tiempo aleatorio generado: {tiempo_aleatorio} horas")  # ver el tiempo en la salida de pruebas
    context.belly.esperar(tiempo_aleatorio)


@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('y', ' ')
    time_description = time_description.replace(',', ' ')
    time_description = time_description.strip()

    # Manejar casos con numeros directamente como 1.5, 2 o etc.
    try:
        tiempo = float(time_description.replace(" horas", "").strip())
        context.belly.esperar(tiempo)
        return
    except ValueError:
        pass

    # Manejar casos especiales como 'media hora'
    if time_description == 'media hora':
        total_time_in_hours = 0.5

    else:

        # Expresión regular para extraer horas y minutos
        pattern = re.compile(
            r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?\s*(?:(\w+)\s*segundos?)?'  
            r'(?:(\w+)\s*hours?)?\s*(?:(\w+)\s*minutes?)?\s*(?:(\w+)\s*seconds?)?'   
        )

        match = pattern.match(time_description)

        if match:
            hours_word = match.group(1) or match.group(4) or "0"
            minutes_word = match.group(2) or match.group(5) or "0"
            seconds_word = match.group(3) or match.group(6) or "0"

            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)
            seconds = convertir_palabra_a_numero(seconds_word)

            total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
        else:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('error de cantidad de pepinos negativos')
def step_then_should_raise_error_negative(context):
    assert isinstance(context.exception, ValueError), "Se esperaba un error de cantidad de pepinos negativos, pero no se produjo"

@then('error de cantidad de pepinos excesivos')
def step_then_should_raise_error_excessive(context):
    assert isinstance(context.exception, ValueError), "Se esperaba un error de cantidad de pepinos excesivos, pero no se produjo"


@when('pregunto cuántos pepinos más puedo comer')
def step_when_ask_pepinos_restantes(context):
    context.pepinos_restantes = context.belly.pepinos_restantes_para_grunir()

# para 'Y he esperado 1 horas' o 'Y he esperado 2 horas'
@given('he esperado {horas:Number} horas')
def step_given_esperado_horas(context, horas):
    context.belly.esperar(horas)

@then('debería decirme que puedo comer {cantidad:d} pepinos más')
def step_then_decirme_cuantos_faltan(context, cantidad):
    assert context.pepinos_restantes == cantidad, \
    f"Se esperaba {cantidad} pepinos más, pero se obtuvo {context.pepinos_restantes}"

@then('debería decirme que ya no puedo comer más')
def step_then_ya_gruniendo(context):
    assert context.pepinos_restantes == 0, \
        f"Se esperaba 0 porque ya gruñe, pero se obtuvo {context.pepinos_restantes}"

@then('debería decirme que debo esperar más')
def step_then_decirme_esperar_mas(context):
    assert context.pepinos_restantes == "esperar más", \
        f"Se esperaba 'esperar más', pero se obtuvo {context.pepinos_restantes}"

