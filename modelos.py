class Aluno:
    def __init__(self):
        self.nome = ''
        self.email = ''
        self.nota1 = 0.0
        self.nota2 = 0.0

    def imprimirInformacoes(self):
        print(f"""Nome: {self.nome}
                  E-mail: {self.email}
                  Nota 1: {self.nota1}
                  Nota 2: {self.nota2} """)
        
class Curso:
    def __init__(self, c, v):
        self.nome = c
        self.valor = v