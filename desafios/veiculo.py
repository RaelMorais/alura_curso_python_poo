from abc import ABC, abstractclassmethod
class Veiculo:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self. ano = ano


    @abstractclassmethod
    def ligar(self):
        pass    

    @abstractclassmethod
    def acelerar(self):
        pass