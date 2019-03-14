class Pessoa():
    # criando atributo de classe
    # quando tivermos um atributo com valor defaul criamos fora,
    # do __init__, deste geito poupamos memoria
    olhos = 2 # atributo defaul ou atributo de classe
    def __init__(self, *filhos, nome=None, idade=49):
        # criando primeiro atributo
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos) # atributo variavel

    # criamos o primeiro metodo
    def cumprimentar(self):
        return f"Olá{id(self)}"

if __name__ == '__main__':
    gerson = Pessoa(nome="Gerson")
    luciano = Pessoa(gerson, nome='Luciano')
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del  luciano.filhos
    print(luciano.__dict__)
    print(gerson.__dict__)