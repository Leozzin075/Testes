from destino_Repositorio import destinoRepositorio
from Destino import destino
class interfaceUsuario:
    def __init__(self, destino_Repositorio: destinoRepositorio):
        self.destino_Repositorio = destino_Repositorio
    
    def solicitar_input_usuario(self):
        resultado = int(input("Digite o DDD q voce quer saber:\n--->"))
        return resultado
    
    def exibir_destinos(self):
        lugares = destinoRepositorio()
        lugares.adcionarDestino(61, "Brasilia")
        lugares.adicionarDestino(71, "Salvador")
    
    def saida_usuario(self):
        entrada = self.solicitar_input_usuario()
        if (self.destino_Repositorio.checarDestino(entrada) == False):
            return "DDD invalido"
        else:
            return self.obterPeloDDD(entrada)
        

