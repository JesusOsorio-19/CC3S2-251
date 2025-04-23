import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory

@pytest.fixture
def carrito():
    return Carrito()

@pytest.fixture
def producto_generico():
    return ProductoFactory(nombre="Genérico", precio=100.0)

@pytest.fixture
def producto_laptop():
    return ProductoFactory(nombre="Laptop", precio=1000.0)

@pytest.fixture
def producto_mouse():
    return ProductoFactory(nombre="Mouse", precio=50.0)

@pytest.fixture
def producto_teclado():
    return ProductoFactory(nombre="Teclado", precio=75.0)

@pytest.fixture
def producto_tablet():
    return ProductoFactory(nombre="Tablet", precio=500.0)

@pytest.fixture
def producto_smartphone():
    return ProductoFactory(nombre="Smartphone", precio=800.0)

@pytest.fixture
def producto_monitor():
    return ProductoFactory(nombre="Monitor", precio=300.0)

@pytest.fixture
def producto_impresora():
    return ProductoFactory(nombre="Impresora", precio=200.0)

@pytest.fixture
def producto_scaner():
    return ProductoFactory(nombre="Escáner", precio=150.0)

@pytest.fixture
def producto_auriculares():
    return ProductoFactory(nombre="Auriculares", precio=150.0)

@pytest.fixture
def producto_cargador():
    return ProductoFactory(nombre="Cargador", precio=25.0)



