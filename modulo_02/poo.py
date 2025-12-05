# POO


# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."    

# Objetos
pessoa1 = Pessoa("Aline", 30)
mensagem = pessoa1.saudacao()
print(mensagem)
#print("Nome:", pessoa1.nome)
#print("Idade:", pessoa1.idade)

pessoa2 = Pessoa(nome="Marcelo", idade=45)
mensagem = pessoa2.saudacao()
print(mensagem)