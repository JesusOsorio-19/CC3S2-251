import pytest
from src.carrito import Carrito, Producto
from src.factories import ProductoFactory

"""
def test_agregar_producto_nuevo():
    
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 1.
    
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=1000.00)
    
    # Act
    carrito.agregar_producto(producto)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Laptop"
    assert items[0].cantidad == 1
"""

def test_agregar_producto_nuevo(carrito, producto_laptop):
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 1.
    """
    # Act
    carrito.agregar_producto(producto_laptop, cantidad=1)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Laptop"
    assert items[0].cantidad == 1

def test_agregar_producto_existente_incrementa_cantidad(carrito, producto_mouse):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se agrega el mismo producto nuevamente aumentando la cantidad.
    Assert: Se verifica que la cantidad del producto se incrementa en el item.
    """
    # Arrange
    
    carrito.agregar_producto(producto_mouse, cantidad=1)
    
    # Act
    carrito.agregar_producto(producto_mouse, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_remover_producto(carrito, producto_teclado):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    Act: Se remueve una unidad del producto.
    Assert: Se verifica que la cantidad del producto se reduce a 2.
    """
    # Arrange
    carrito.agregar_producto(producto_teclado, cantidad=3)
    
    # Act
    carrito.remover_producto(producto_teclado, cantidad=1)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo(carrito, producto_monitor):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se remueve la totalidad de la cantidad del producto.
    Assert: Se verifica que el producto es eliminado del carrito.
    """
    # Arrange
    carrito.agregar_producto(producto_monitor, cantidad=2)
    
    # Act
    carrito.remover_producto(producto_monitor, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0

def test_actualizar_cantidad_producto(carrito, producto_auriculares):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 5.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    carrito.agregar_producto(producto_auriculares, cantidad=1)
    
    # Act
    carrito.actualizar_cantidad(producto_auriculares, nueva_cantidad=5)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 5

def test_actualizar_cantidad_a_cero_remueve_producto(carrito, producto_cargador):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 0.
    Assert: Se verifica que el producto se elimina del carrito.
    """
    # Arrange

    carrito.agregar_producto(producto_cargador, cantidad=3)
    
    # Act
    carrito.actualizar_cantidad(producto_cargador, nueva_cantidad=0)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0

@pytest.mark.parametrize("cantidad_inicial, nueva_cantidad, cantidad_esperada", [
    (5, 3, 3),  # Reducir cantidad
    (3, 5, 5),  # Aumentar cantidad
    (2, 0, 0),  # Remover producto
])

def test_actualizar_cantidad_parametrizado(carrito, producto_laptop, cantidad_inicial, nueva_cantidad, cantidad_esperada):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con una cantidad inicial.
    Act: Se actualiza la cantidad del producto a una nueva cantidad.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    carrito.agregar_producto(producto_laptop, cantidad=cantidad_inicial)
    
    # Act
    carrito.actualizar_cantidad(producto_laptop, nueva_cantidad=nueva_cantidad)
    
    # Assert
    items = carrito.obtener_items()
    if nueva_cantidad == 0:
        # Si la cantidad es 0, el producto debe ser removido del carrito
        assert len(items) == 0
    else:
        # Si la cantidad es mayor a 0, el producto debe permanecer en el carrito
        assert len(items) == 1
        assert items[0].cantidad == cantidad_esperada

def test_calcular_total(carrito, producto_impresora, producto_scaner):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos con distintas cantidades.
    Act: Se calcula el total del carrito.
    Assert: Se verifica que el total es la suma correcta de cada item (precio * cantidad).
    """
    # Arrange
    carrito.agregar_producto(producto_impresora, cantidad=2) 
    carrito.agregar_producto(producto_scaner, cantidad=1)
    
    # Act
    total = carrito.calcular_total()
    
    # Assert
    assert total == 550.00


def test_aplicar_descuento(carrito, producto_tablet):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con una cantidad determinada.
    Act: Se aplica un descuento del 10% al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange

    carrito.agregar_producto(producto_tablet, cantidad=2)  # Total 1000
    
    # Act
    total_con_descuento = carrito.aplicar_descuento(10)
    
    # Assert
    assert total_con_descuento == 900.00


def test_aplicar_descuento_limites(carrito, producto_smartphone):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act y Assert: Se verifica que aplicar un descuento fuera del rango [0, 100] genere un error.
    """
    # Arrange
    carrito.agregar_producto(producto_smartphone, cantidad=1)
    
    # Act y Assert
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(150)
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(-5)
        
@pytest.mark.parametrize("descuento, total_esperado", [
    (0, 1000.00),  # Sin descuento
    (10, 900.00),  # Descuento del 10%
    (20, 800.00),  # Descuento del 20%
    (50, 500.00)    # Descuento del 50%
])

def test_aplicar_descuento_parametrizado(carrito, producto_laptop, descuento, total_esperado):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se aplica un descuento parametrizado al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    carrito.agregar_producto(producto_laptop, cantidad=1)  
    
    # Act
    total_con_descuento = carrito.aplicar_descuento(descuento)
    
    # Assert
    assert total_con_descuento == total_esperado

def test_vaciar_carrito(carrito, producto_laptop, producto_mouse):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan productos.
    Act: Se llama al método vaciar() para vaciar el carrito.
    Assert: Se verifica que el carrito está vacío y el total es 0.
    """
    # Arrange
    carrito.agregar_producto(producto_laptop, cantidad=1)
    carrito.agregar_producto(producto_mouse, cantidad=2)

    # Act
    carrito.vaciar()

    # Assert
    assert carrito.obtener_items() == []
    assert carrito.calcular_total() == 0

def test_aplicando_descuento_condicional_con_total_mayor_a_500(carrito, producto_laptop):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan productos que suman más de $500.
    Act: Se aplica un descuento del 15% si el total es mayor o igual a $500.
    Assert: Se verifica que el total con descuento sea correcto.
    """
    # Arrange
    carrito.agregar_producto(producto_laptop, cantidad=1)  

    # Act
    total_con_descuento = carrito.aplicar_descuento_condicional(15,minimo = 500)

    # Assert
    assert total_con_descuento == 850.00  

def test_aplicando_descuento_condicional_con_total_menor_a_500(carrito, producto_mouse):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan productos que suman menos de $500.
    Act: Se aplica un descuento del 15% si el total es mayor o igual a $500.
    Assert: Se verifica que el total con descuento sea igual al total original.
    """
    # Arrange
    carrito.agregar_producto(producto_mouse, cantidad=4)  # Total 200

    # Act
    total_con_descuento = carrito.aplicar_descuento_condicional(15,minimo = 500)

    # Assert
    assert total_con_descuento == 200.00  

def test_agregar_procucto_con_stock_suficiente(carrito, producto_laptop):
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto con stock suficiente.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 5.
    """

    # Arrange
    producto_laptop.stock = 10  # Aseguramos que el stock es suficiente

    # Act
    carrito.agregar_producto(producto_laptop, cantidad=5)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Laptop"
    assert items[0].cantidad == 5

def test_agregar_producto_con_stock_insuficiente(carrito, producto_laptop):
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto con stock insuficiente.
    Act: Se intenta agregar el producto al carrito.
    Assert: Se verifica que se lanza una excepción de ValueError.
    """
    # Arrange
    producto_laptop.stock = 3
    
    # Act y Assert
    with pytest.raises(ValueError):
        carrito.agregar_producto(producto_laptop, cantidad=5)

def test_obtener_items_ordenados_por_nombre(carrito, producto_laptop, producto_mouse, producto_teclado):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan productos con diferentes nombres.
    Act: Se obtienen los items del carrito ordenados por nombre.
    Assert: Se verifica que los items están ordenados correctamente.
    """
    # Arrange
    carrito.agregar_producto(producto_laptop, cantidad=1)
    carrito.agregar_producto(producto_mouse, cantidad=2)
    carrito.agregar_producto(producto_teclado, cantidad=1)

    # Act
    items_ordenados = carrito.obtener_items_ordenados("nombre")

    # Assert
    assert items_ordenados[0].producto.nombre == "Laptop"
    assert items_ordenados[1].producto.nombre == "Mouse"
    assert items_ordenados[2].producto.nombre == "Teclado"

def test_obtener_items_ordenados_por_precio(carrito, producto_laptop, producto_mouse, producto_teclado):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan productos con diferentes precios.
    Act: Se obtienen los items del carrito ordenados por precio.
    Assert: Se verifica que los items están ordenados correctamente.
    """
    # Arrange
    carrito.agregar_producto(producto_laptop, cantidad=1)
    carrito.agregar_producto(producto_mouse, cantidad=2)
    carrito.agregar_producto(producto_teclado, cantidad=1)

    # Act
    items_ordenados = carrito.obtener_items_ordenados("precio")

    # Assert
    assert items_ordenados[0].producto.precio == 50.00
    assert items_ordenados[1].producto.precio == 75.00
    assert items_ordenados[2].producto.precio == 1000.00

def test_obtener_items_ordenados_criterio_invalido(carrito, producto_laptop, producto_mouse):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan productos.
    Act: Se intenta obtener los items del carrito con un criterio de ordenación inválido.
    Assert: Se verifica que se lanza una excepción de ValueError.
    """
    # Arrange
    carrito.agregar_producto(producto_laptop, cantidad=1)
    carrito.agregar_producto(producto_mouse, cantidad=2)

    # Act y Assert
    with pytest.raises(ValueError):
        carrito.obtener_items_ordenados("color")