
class Veiculo:
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.ligado = False
    def ligar(self):
        self.ligado = True  
        return "Ligada" if self.ligado else "Desligada" 

    def __str__(self):
        status = "Ligado" if self.ligado else "Desligado"
        return f"O {self.modelo} da {self.marca} do ano de {self.ano} está {status} "
