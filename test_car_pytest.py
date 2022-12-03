import pytest
from Car import Car

@pytest.fixture
def testcar():
    return Car(50)

def test_car_accelerate(testcar):
    testcar.accelerate()
    assert testcar.speed == 55

def test_car_brake():
    car = Car(50)
    car.brake()
    assert car.speed == 45

def test_car_odometer(testcar):
    testcar.accelerate()
    testcar.step()
    assert testcar.odometer == 55

def test_car_speed(testcar):
    testcar.accelerate()
    assert testcar.speed == 55
