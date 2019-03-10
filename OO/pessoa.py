class Pessoa():
    def __init__(self, nome=None, idade=49):
        # criando primeiro atributo
        self.idade = idade
        self.nome = nome
    # criamos o primeiro metodo
    def cumprimentar(self):
        return f"Olá{id(self)}"

if __name__ == '__main__':
    p = Pessoa("Gerson")
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome, p.idade)