class Pessoa:
    def __init__(self, nome, idade, cpf, profisao):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.profisao = profisao

    def __str__(self):
        return f'Olá, me chamo {self.nome}, tenho {self.idade} anos e meu cpf é {self.cpf}'
    
    def fazer_aniversario(self):
        self.idade += 1
    
    def saudadao(self):
        return f"Saudações, eu sou um {self.profisao}"

pessoa1 = Pessoa("João", 23, "456.787.890-90", "Eng. Software")
pessoa1.fazer_aniversario()

print(f"{pessoa1}\n{pessoa1.saudadao()}")
        