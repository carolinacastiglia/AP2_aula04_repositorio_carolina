from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, numMarcha, bagageiro):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.numMarcha = numMarcha
        self.bagageiro = bagageiro
    
    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        if self.bagageiro == 1:
            print("Possui ", self.numMarcha, " marchas e possui bagageiro.")
        else:
            print("Ppossui ", self.numMarcha, " marchas e não possui bagageiro.")