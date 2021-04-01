class Veiculo:
    def __init__(self, marca, qtdRodas, modelo, velocidade):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade
    
    def imprimirInformacoes(self):
        print("Veículo da marca ", self.marca, " com ", self.qtdRodas, " rodas do modelo ", self.modelo, " com velocidade de ", self.velocidade,"Km/h")

    def acelerar(self, valorAcelerar):
        print("Acelerou. Valor atual da velocidade: ", self.velocidade + valorAcelerar)

    def frear(self, valorFrear):
        print("Freou. Valor atual da velocidade: ", self.velocidade - valorFrear)