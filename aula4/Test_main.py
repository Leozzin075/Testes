from Destino import Destino
from DestinoRepository import DestinoRepositorio
from InterfaceUsuario import InterfaceUsuario

def test_checar_se_item_existe():
    destino_repositorio = DestinoRepositorio()
    destino_repositorio.lista_destino = []
    destino1 = Destino('Salvador', 71)
    
    destino_repositorio.adicioanar_destino(destino1)
    resultOK = destino_repositorio.checa_se_destino_existe(71)
    resultNOK = destino_repositorio.checa_se_destino_existe(68)
    
    assert resultOK == True
    assert resultNOK == False
    
def test_solicitar_input_usuario():  
    destino_repositorio = DestinoRepositorio()
    Interface = InterfaceUsuario(destino_repositorio) 

    result= Interface.solicitar_input_usuario()

    assert result == 71 
    assert type(result) == int