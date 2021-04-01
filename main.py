from Veiculo import Veiculo
from Bicicleta import Bicicleta

v1 = Veiculo("Honda", 4, "Civic", 100)
v1.imprimirInformacoes()
v1.acelerar(20)
v1.frear(50)

print("----------------------------------------------")

b1Bag = Bicicleta("Caloi", 2, "elite", 70, 4, 1)
b1Bag.imprimirInformacoes()
b1Bag.acelerar(5)
b1Bag.frear(15)

print("----------------------------------------------")

b2NaoBag = Bicicleta("Caloi", 2, "super", 85, 6, 0)
b2NaoBag.imprimirInformacoes()