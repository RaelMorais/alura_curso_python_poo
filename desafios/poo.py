class Musica:
    def __init__(self, nome, artista, duracao, cantar=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        self.cantar = cantar
        self._atividade = False
    
    @property
    def atividade(self):
        return 'Em turne' if self._atividade else 'Não esta em turne'
    
    def alterar_estadp(self):
        self._atividade = True

    def cantando(self):
        self.cantar += 1
        print(f"Estou cantando a musica {self.nome} do artista {self.artista} com duração de {self.duracao} e o artista está em: {self.atividade}")
    
musica = Musica("Pelados em Santos", "Mamonas Assasinas", 3.5)
musica.alterar_estadp()
musica.cantando()

