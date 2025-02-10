from veiculo import Veiculo
from abc import ABC, abstractclassmethod

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, ano):
        super().__init__(marca, modelo, cor, ano)
        self.velocidade = 0; 
    def ligar(self):
        print(f"O {self.modelo} da marca {self.marca}, cor {self.cor}, ano {self.ano} está ligado")

    def acelerar(self):
        while self.velocidade <= 50:
            print(f"O {self.modelo} da marca {self.marca}, cor {self.cor}, ano {self.ano} está ligado e acelerando a {self.velocidade}")
            self.velocidade += 10