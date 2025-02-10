from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida("Suco Melancia", 5.99, "Grande")
bebida_suco.aplicar_desconto()
prato_paozinho = Prato("Pãozinho", 0.60, "Pão doce")
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()