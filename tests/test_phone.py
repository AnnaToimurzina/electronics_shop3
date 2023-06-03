import pytest
from src.phone import Phone

@pytest.fixture
def phone():
    return Phone("iPhone 14", 120000, 5, 2)

def test_phone_number_of_sim_setter():
    with pytest.raises(ValueError):
        Phone("iPhone 14", 120000, 5, -1)
    with pytest.raises(ValueError):
        Phone("iPhone 14", 120000, 5, 1.5) # Number of SIM cards should be integer
        Phone("iPhone 14", 120000, 5, 2)
        phone.number_of_sim = 3
        assert phone.number_of_sim == 3

def test_phone_repr():
    assert Phone("iPhone 14", 120000, 5, 2)