from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, partidaEletrica):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.partidaEletrica = partidaEletrica
    
    def imprimirInformacoes(self):
        Automovel.imprimirInformacoes(self)
        if self.partidaEletrica == 1:
            print("Com partida elétrica.")
        else:
            print("Sem partida elétrica.")