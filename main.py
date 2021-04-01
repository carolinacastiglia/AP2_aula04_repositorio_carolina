from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Moto import Moto

print()

v1 = Veiculo("Honda", 4, "Civic", 100)
v1.imprimirInformacoes()
v1.acelerar(20)
v1.frear(50)

print("\n----------------------------------------------\n")

b1Bag = Bicicleta("Caloi", 2, "elite", 70, 4, 1)
b1Bag.imprimirInformacoes()
b1Bag.acelerar(5)
b1Bag.frear(15)

print("\n----------------------------------------------\n")

b2NaoBag = Bicicleta("Caloi", 2, "super", 85, 6, 0)
b2NaoBag.imprimirInformacoes()

print("\n----------------------------------------------\n")

auto1 = Automovel("Fiat", 4, "Uno", 80, 25)
auto1.imprimirInformacoes()
auto1.acelerar(2)
auto1.frear(10)

print("\n----------------------------------------------\n")

m1PartidElet = Moto("Suzuki", 2, 125, 200, 75, 1)
m1PartidElet.imprimirInformacoes()
m1PartidElet.acelerar(25)
m1PartidElet.frear(20)

print("\n----------------------------------------------\n")

m2SemPartElet = Moto("Suzuki", 2, 75, 140, 140, 0)
m2SemPartElet.imprimirInformacoes()