from Destino import Destino
from InterfaceUsuario import InterfaceUsuario
from DestinoRepository import DestinoRepositorio

destino_repositorio = DestinoRepositorio()
destino_repositorio.adicioanar_destino(Destino('salvador', 71))
destino_repositorio.adicioanar_destino(Destino('acre', 68))

print(destino_repositorio)

interface_usuario = InterfaceUsuario(destino_repositorio)

while True:
    retorno = interface_usuario.saida_usuario()
    if retorno == 'Invalid code!':
        break
    
    print(retorno)