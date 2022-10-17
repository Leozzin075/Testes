from destino import Destino

class destino_Repositorio:
    listaDestino: Destino = []
    
    def __init__(self):
        pass
    
    def adicionarDestino(self, destino: destino):
        self.listaDestino.append(destino)
    
    def checarDestino(self, ddd: destino):
       for item in self.listaDestino:
            if (ddd.ddd == item.ddd): 
                return True

            return False
    
    def obterPeloDDD(self, ddd: destino):
        for item in self.listaDestino:
            if (destino.ddd == item.ddd):
                return item.destino