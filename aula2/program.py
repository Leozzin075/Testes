from menu import Menu
from quadrant import Quadrant

menu = Menu()

while True:
    if (menu.show_menu() == True):
        break

    coordinates = menu.coordinates

    my_quadrant = Quadrant(coordinates)
    print(f"{my_quadrant.get_quadrant_coordinate()} quadrant.")