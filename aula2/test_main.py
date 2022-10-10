from Coordinate import Coordinate
from menu import Menu



def test_get_user_coordinate():
    a = 3
    b = 4
    menu = Coordinate(a,b)
    
    result = menu.get_user_coordinate()
    
    assert result == 3,4
    
def test_cordinate_is_valid():
    a = 1
    b = 0
    test = Coordinate(a, b)
    
    result = test.coordinate_is_valid(a,b)
    
    assert result == False
    

def test_cordinate_is_valid1():
    a = 0
    b = 1
    test = Coordinate(a, b)
    
    result = test.coordinate_is_valid(a,b)
    
    assert result == False
    
def test_cordinate_is_valid2():
    a = 3
    b = 1
    test = Coordinate(a, b)
    
    result = test.coordinate_is_valid(a,b)
    
    assert result == True
    
    