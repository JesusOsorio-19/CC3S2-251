import pytest
from iac_patterns.singleton import ConfigSingleton

def test_singleton_reset_preserves_created_at():
    """Test que verifica que reset() limpia settings pero preserva created_at"""
    c1 = ConfigSingleton("dev")
    created = c1.created_at
    c1.settings["x"] = 1
    
    c1.reset()
    
    assert c1.settings == {}        # Settings debe estar vacío
    assert c1.created_at == created # created_at debe preservarse

def test_singleton_reset_preserves_env_name():
    """Test adicional que verifica que reset() preserva env_name"""
    c1 = ConfigSingleton("production")
    original_env = c1.env_name
    c1.settings["key"] = "value"
    
    c1.reset()
    
    assert c1.settings == {}
    assert c1.env_name == original_env