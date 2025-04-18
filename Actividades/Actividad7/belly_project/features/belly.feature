# language: es

Característica: Característica del estómago

  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir

  Escenario: Comer una cantidad fraccionaria de pepinos
    Dado que he comido 0.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir  

  Escenario: esperar usando horas en inglés 
    Dado que he comido 20 pepinos
    Cuando espero "two hours and thirty minutes"
    Entonces mi estómago debería gruñir  

  Escenario: esperar usando segundos en inglés
    Dado que he comido 35 pepinos
    Cuando espero "one hour, thirty minutes and forty seconds"
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espero un tiempo aleatorio entre 1 y 3 horas 
    Entonces mi estómago debería gruñir
  
  Escenario: Manejar una cantidad no valida de pepinos
    Dado que he comido -5 pepinos
    Entonces error de cantidad de pepinos negativos

  Escenario: Manejar una cantidad excesiva de pepinos
    Dado que he comido 150 pepinos
    Entonces error de cantidad de pepinos excesivos
  
  @escalabilidad
  Escenario: Comer 1000 pepinos y esperar 10 horas
    Dado que he comido 1000 pepinos
    Cuando espero 10 horas
    Entonces mi estómago debería gruñir

  Escenario: manejar tiempos complejos
    Dado que he comido 50 pepinos
    Cuando espero "1 hora, 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir    

  Escenario: Comer muchos pepinos y esperar el tiempo suficiente
    Dado que he comido 15 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: comer suficientes pepinos y esperar el tiempo adecuado
    Dado que he comido 20 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir  

  Escenario: comer pocos pepinos y no esperar suficiente tiempo
    Dado que he comido 5 pepinos
    Cuando espero 1 horas
    Entonces mi estómago no debería gruñir   

  Escenario: comer más de 10 pepinos y esperar menos de 1 hora
    Dado que he comido 15 pepinos
    Cuando espero 0.5 horas
    Entonces mi estómago no debería gruñir

  Escenario: Saber cuántos pepinos he comido
    Dado que he comido 10 pepinos
    Cuando he comido 5 pepinos más
    Entonces debería haber comido 15 pepinos

  Escenario: Saber cuantos pepinos fraccionarios he comido
    Dado que he comido 1.5 pepinos
    Cuando he comido 0.5 pepinos más
    Entonces debería haber comido 2.0 pepinos

  Escenario: Verificar que el estómago gruñe tras comer suficientes pepinos y esperar
    Dado que he comido 20 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: Predecir si mi estómago gruñirá tras comer y esperar
    Dado que he comido 12 pepinos
    Cuando espero 1.5 horas
    Entonces mi estómago debería gruñir

  Escenario: Saber cuántos pepinos más puedo comer antes de gruñir
    Dado que he comido 8 pepinos
    Y he esperado 2 horas
    Cuando pregunto cuántos pepinos más puedo comer
    Entonces debería decirme que puedo comer 3 pepinos más

  Escenario: Ya estoy gruñendo
    Dado que he comido 20 pepinos
    Y he esperado 2 horas
    Cuando pregunto cuántos pepinos más puedo comer
    Entonces debería decirme que ya no puedo comer más

  Escenario: Aún no he esperado suficiente tiempo
    Dado que he comido 8 pepinos
    Y he esperado 0.5 horas
    Cuando pregunto cuántos pepinos más puedo comer
    Entonces debería decirme que debo esperar más
