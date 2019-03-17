"""Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes

1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela oferece os
seguintes atributos
1) Valor de direção com valores possiveis: Norte, Sul, Leste, Oeste.
2) Método girar a direita
3) Método girar a esquerda

   N
O     L
   S
"""


class Carro:

    def __init__(self):
        self.motor = Motor(velociade=0)
        self.direcao = Direcao()

"""Por convenção do PE8 quanto temos constantes no python,
elas são escritas todas com letras maiusculas,"""
NORTE= 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
    """Criamos um atributo de classe para usarmos os valores de direção,
    para não usarmos muitos if, podemos criar um dicionario com os valores a
    serem setados, na forma de chave e valor, exemplo quando a chave for
    NORTE o valor será LESTE"""
    rotacao_a_direita_dict = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE:NORTE
    }
    rotacao_a_esquerda_dict = {
        NORTE: OESTE, LESTE: NORTE , SUL: LESTE, OESTE: SUL
    }
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        """Como temos o valor padrão para NORTE definido, quando chamamos a
        função girar_a_direita, carregamos o valor padrão em self.valor e
        chamamos a chave de self.valor para ser a proxima chamada"""
        self.valor = self.rotacao_a_direita_dict[self.valor]
        print(self.valor)

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_direita_dict[self.valor]

class Motor:
    print("entrou motor")

    def __init__(self, velociade):
        self.velocidade = velociade

    def acelerar(self):

        self.velocidade += 1
        print(self.velocidade)
        return self.velocidade

    def frear(self):
        """max(0, self.velocidade) , retorna o valor maior entre os dois
        valores, se self.velocidade for maior que zero retorna self.velocidade,
        se self.velocidade for menor que zero retorna zero"""
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

        return self.velocidade





if __name__ == '__main__':
    teste = Carro()
    teste.motor.acelerar()
    teste.motor.acelerar()
    teste.motor.acelerar()
    teste.motor.frear()
    teste.motor.frear()
    teste.motor.frear()
    teste.direcao.girar_a_direita()
    teste.direcao.girar_a_direita()
    teste.direcao.girar_a_direita()
    # teste.direcao.girar_a_direita()