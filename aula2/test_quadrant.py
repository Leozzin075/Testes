from Coordinate import Coordinate
from quadrant import Quadrant


def test_should_get_quadrant_coordinate():
    # Arrange / Setup
    a = 10
    b = 20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "First"
    

def test_should_get_quadrant_coordinate1():
    # Arrange / Setup
    a = -10
    b = 20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Second"
    
    
def test_should_get_quadrant_coordinate2():
    # Arrange / Setup
    a = 10
    b = -20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Fourth"
    

def test_should_get_quadrant_coordinate3():
    # Arrange / Setup
    a = -10
    b = -20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Third"