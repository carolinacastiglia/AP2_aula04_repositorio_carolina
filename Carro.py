from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, qtdPortas):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.qtdPortas = qtdPortas
    
    def imprimirInformacoes(self):
        Automovel.imprimirInformacoes(self)
        print("Possui", self.qtdPortas, "portas.")