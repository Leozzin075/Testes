from Coordinate import Coordinate
from menu import Menu
import program
from quadrant import Quadrant


def test_menu_test():
    a = 3
    b = 4
    menu = coordinates(a,b)
    
    result = menu.show_menu()
    
    assert result == 3,4
    
def test_