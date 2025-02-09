class Musica2:
    nome = ""
    artista = ""
    duracao = int

musica1 = Musica2()
musica1.nome= "Bohemia Rhapsody"
musica1.artista = "Queen"
musica1.duracao = 355
print(musica1.nome, musica1.artista, musica1.duracao)

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐' 
    
    def alternar_estado(self):
        self._ativo = not self._ativo


    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')



            
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()
