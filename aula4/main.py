from destino import Destino
from interfaceUsario import interfaceUsuario
from destinoRepositorio import destinoRepositorio

menu = destinoRepositorio()

user_interface = destinoRepositorio(menu)

while user_interface.saidaUsuario():
    pass