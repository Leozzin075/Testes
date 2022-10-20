from DestinoRepository import DestinoRepositorio
from Destino import Destino

class InterfaceUsuario:
    def __init__(self, destino_repositorio: DestinoRepositorio):
        self.destino_repositorio = destino_repositorio
        
    def solicitar_input_usuario(self):
        result = int(input(
            "Informe o DDD que quer consultar: \n-->"))
        return result
    
    def exibir_destinos(self, ddd: Destino):
        return self.destino_repositorio.obter_destino_pelo_ddd(ddd)
    
    def saida_usuario(self):
        ddd = self.solicitar_input_usuario()
        
        if (self.destino_repositorio.checa_se_destino_existe(ddd) == False):

            return 'Invalid code!'
        
        return self.destino_repositorio.obter_destino_pelo_ddd(ddd)