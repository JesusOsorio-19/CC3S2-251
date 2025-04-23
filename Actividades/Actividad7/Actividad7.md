# Actividad 7

## Ejercicios

- Añadimos soporte para minutos y segundos en tiempos de espera. También manejo de cantidades fraccionarias de pepinos.

    ![](imgs/3.png)

- Soporte para idiomas en Inglés.
    -   Definimos los números en ing y tambien la expresión para extrare horas, minutos y segundos en inglés.
    ![](imgs/4.1.png)

    ![](imgs/4.2.png)

    - Añadimos escenarios en tiempos con inglés y vemos que si pasan.

    ![](imgs/4.png)

- Manejamos tiempos aleatorios.

    - Creamos una función que genere un tiempo aleatorio.

    ![](imgs/5.1.png)

    - Añadimos el escenario para esta función.

    ![](imgs/5.png)

- Validamos cantidades no válidas.

    - Añadimos un rango entre 0 y 100 pepinos como cantidad válidas para comer

    ![](imgs/6.1.png)

    - Validamos los nuevos escenarios.

    ![](imgs/6.png)

- Escalabilidad con grandes cantidades

    - Para esto añadimos un escensario de prueba para que ignore la validación anterior.

    ![](imgs/7.1.png)

    - Verificamos este escenario con una etiqueta `@escalabilidad`.

    ![](imgs/7.2.png)

    - Vemos que pasó la prueba con normalidad.

    ![](imgs/7.png)

- Descripciones de tiempos complejas

    - Lo implementamos

    ![](imgs/10.1.png)

    - Lo comprobamos con este escenario

    ![](imgs/10.png)


- Covertimos requisitos técnicos a pruebas con Gherkin.

    - Implementamos test unitarios. 

    ![](imgs/11.png)

    (test de prueba, en el repositorio se encuentran todos los tests implementados.)
   
   - Ejemplo de Gherkin:

   ![](imgs/11.1.png)

- Identificamos criterios de aceptación para historia de usuarios.

    >"Como usuario que ha comido pepinos, quiero saber si mi estómago va a gruñir después de esperar un tiempo suficiente, para poder tomar una acción."

    - Para interpretar esta historia, creamos 3 escenarios.

    ![](imgs/12.png)

- Escribimos pruebas unitarias antes de escenarios BDD.

    - Un ejemplo de test unitario.

    ![](imgs/13.png)

    - Un escenario implementado

    ![](imgs/13.1.png)

- Refactorizamos por TDD y BDD

    - Ejemplo de test unitario.

    ![](imgs/14.png)

    - Escenario 

    ![](imgs/14.1.png)

- Añadimos una nueva funcionalidad para ciclo completo de TDD a BDD

    - Implementamos un test que predecirá si el estómago gruñirá.

    ![](imgs/15.1.png)

    - Escenario

    ![](imgs/15.2.png)

- Añadimos criterios de aceptación claros.

    - Implementamos una nueva historia de usuario.
    > "Ver cuántos pepinos me faltan para gruñir"

    - Identificamos 3 criterios de aceptación y lo convertimos en escenarios BDD:

    ![](imgs/16.png)

- Integramos con Mocking, Stubs y Fakes.

    - Creamos el archivo `clock.py`.

    ![](imgs/17.png)

    - Modificamos `Belly` para que acepte un `clock_service`.

    ![](imgs/17.1.png)

    - Creanos un test unitario que use `unittest.mock`.

    ![](imgs/17.2.png)

    - En Behave usamos `environment.py` para inyectar un mock.
 
    ![](imgs/17.3.png)

    Acá tambien está implementado la nueva clase de prueba que ignora la cantidad válida de pepinos que definimos entre 1 - 100.


- Comprobamos que todos nuestros escenarios(Behave) implementados se ejecutan normalmente.

    ![](imgs/18.png)

- De igual manera los test unitarios que desarrollamos.

    ![](imgs/18.1.png)

- Y por último el despliegue y validación continua en un entorno de integración (CI/CD) en GitActions

    ![](imgs/19.png)

    Se adjuntan los reportes generados en .txt.