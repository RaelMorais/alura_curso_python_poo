from desafio_alura import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, marca, ano, categoria):
        super().__init__(modelo, marca, ano)
        self.categoria = categoria

    def __str__(self):
        return f"{super().__str__()} A moto é {self.categoria}"
    