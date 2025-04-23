# Actividad 8

## Ejercicio 1

- Agregamos el método `vaciar` en la clase `Carrito`.

    ![](imgs/1.1.png)

- Creamos pruebas que invoquen este nuevo método y luego lo testeamos.

    ![](imgs/1.2.png)

    ![](imgs/1.3.png)

## Ejercicio 2

- Agregamos un nuevo método `aplicar_descuento_condicional` en la clase `Carrito`.

    ![](imgs/2.1.png)

- Creamos pruebas que validen condición cumplida y no cumplida.

    ![](imgs/2.2.png)

    ![](imgs/2.3.png)
   
## Ejercicio 3

- Modificamos la clase `Producto` añadiendo un nuevo atributo que sea `stock` y actualizamos `factories.py` también para que genere un stock aleatorio.

    ![](imgs/3.1.png)

    ![](imgs/3.2.png)

- En `Carrito.agregar_producto`, antes de agregar o incrementar la cantidad, verificamps que la suma de cantidades en el carrito no supere el stock del producto.

    ![](imgs/3.3.png)

- Creamos pruebas que verifiquen estas implementaciones.

    ![](imgs/3.4.png)

    ![](imgs/3.5.png)

## Ejercicio 4

- Agregamos un método que devuelva la lista de items ordenados por criterios definidos.

    ![](imgs/4.1.png)

- Creamos pruebas que verifiquen esto.

    ![](imgs/4.2.png)

    ![](imgs/4.3.png)

## Ejercicio 5

- Creamos un archivo `conftest.py` donde creamos fixtures que se reutilizaran en instancias comunes de `Carrito` o de productos. Como un fixture para un carro vacío o para un producto genérico.

    ![](imgs/5.1.png)

- Creamos un fixture para cada producto creado en `test_carrito.py` y luego lo sustituimos en dicho archivo.

    ![](imgs/5.2.png)

- Acá un ejemplo de como es sustituido por el fixture de `producto_laptop`

    ![](imgs/5.3.png)

- Luego comprobamos que los test funcionan sin problemas.

    ![](imgs/5.4.png)

## Ejercicio 6

- Utilizamos la marca `@pytest.mark.parametrize`, para parametrizar pruebas para `aplicar_descuento`

    ![](imgs/6.1.png)

- Creamos su prueba y veremos que siendo solo un test se aplican como si fueran 4 en uno solo.

    ![](imgs/6.2.png)

- Ahora usamos la marca para `actualizar_cantidades`

    ![](imgs/6.2.png)

- Vemos lo mismo para las pruebas de este.

    ![](imgs/6.4.png)

## Ejercicio 7

- Creamos un nuevo archivo de pruebas `tests/test_impuestos.py`

    ![](imgs/7.1.png)

- Si hacemos la prueba en este punto fallará, ya que aún no se implementa el método `calcular_impuestos`.

    ![](imgs/7.2.png)

- Agregamos el método `calcular_impuestos`.

    ![](imgs/7.3.png)

- Y vemos que ahora si ejecutamos la prueba si pasará.

    ![](imgs/7.4.png)

## Ejercicio 8

- Creamos un nuevo archivo de pruebas `tests/test_cupón.py`.

    ![](imgs/8.1.png)
    
- Implemantamos el método `aplicar_cupon`.

    ![](imgs/8.2.png)

- Ejecutamos las pruebas.

    ![](imgs/8.3.png)

## Ejercicio 9

- Creamos un nuevo archivo de pruebas `tests/test_stock.py`.

    ![](imgs/9.1.png)
    
- Implemantamos el método `_busar_item` y `agregar_producto`.

    ![](imgs/9.2.png)

- Ejecutamos las pruebas.

    ![](imgs/9.3.png)

Ejecutamos pruebas y generamos el reporte de cobertura.

![](imgs/10.png)

O bien generamos un reporte HTML.

![](imgs/11.png)

