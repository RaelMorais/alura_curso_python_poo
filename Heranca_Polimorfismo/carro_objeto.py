# carross.py
from desafio_alura import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, marca, ano, portas):
        super().__init__(modelo, marca, ano)
        self.porta = portas

    def __str__(self):
        return f"{super().__str__()}A quantidade de portas é {self.porta}"
