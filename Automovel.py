from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.potenciaDoMotor = potenciaDoMotor

    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        print("Potência do motor de ", self.potenciaDoMotor)