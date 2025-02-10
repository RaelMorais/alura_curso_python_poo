from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida("Suco Melancia", 5.99, "Grande")
prato_paozinho = Prato("Pãozinho", 0.60, "Pão doce")

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()