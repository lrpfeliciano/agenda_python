from modelos import Aluno

estudante = Aluno()
estudante.nome = "Juan"
estudante.email = "juan@teste.com"
estudante.nota1 = 8.0
estudante.nota2 = 6.5

estudante.endereco = 'Rua 10'
print(estudante.nome)
print(estudante.endereco)
estudante.imprimirInformacoes()

estudante2 = Aluno()
estudante2.nome = "Pedro"
estudante2.email = "pedro@teste.com"
estudante2.nota1 = 10.0
estudante2.nota2 = 8.0
estudante2.imprimirInformacoes()


estudante3 = Aluno("Maria")
print(estudante3.nome)
