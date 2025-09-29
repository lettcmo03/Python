# Crie uma classe chamada Livro com os seguintes atributos: titulo, autor, disponivel (por padrão, começa como True), A classe deve ter os seguintes métodos: emprestar() → se o livro estiver disponível, muda para indisponível e mostra mensagem confirmando o empréstimo. Caso contrário, avisa que já está emprestado. devolver() → se o livro estiver emprestado, muda para disponível e mostra mensagem confirmando a devolução. informacoes() → mostra título, autor e se está disponível ou emprestado.

class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
    def emprestar(self):
        if self.disponivel == True:
            print(f'O livro {self.titulo} agora será seu até 14.10')
            self.disponivel = False
        else:
            print(f'O livro {self.titulo} está INDISPONÍVEL e só será liberado em 14.10')
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f'Obrigada por devolver o livro {self.titulo}')
        else: 
            print(f'O livro {self.titulo} já estava guardado')

    def informacoes(self):
        for i, livro in enumerate(biblioteca):
            print(f"[{i}] {livro.titulo} ({'Disponível' if livro.disponivel else 'Emprestado'})")
        # print(f'Nome: {self.titulo} \nAutor: {self.autor} \nStatus: {self.disponivel}')
biblioteca = [Livro('Dom Casmurro', 'Machado de Assis'), 
              Livro('O Pequeno Príncipe', 'Antoine de Saint-Exupéry'),
              Livro('1984', 'George Orwell'),
              Livro('Alice no País das Maravilhas', 'Lewis Carroll'),
              Livro('Cem Anos de Solidão', 'Gabriel García Márquez')
              ]

for i, livro in enumerate(biblioteca):
    print(f"[{i}] {livro.titulo} ({'Disponível' if livro.disponivel else 'Emprestado'})")

print('BEM VINDO A BIBLIOTECA')
for i in range (1,3):
    acao = 0
    while acao!= 4:
        acao = int(input(f'Gostaria de: \n[1] - Ver livros disponíveis \n[2] - Pegar emprestado \n[3] - Devolver \n[4] - sair\n'))
        match acao:
            case 1:
                # livro.informacoes()
                for i, livro in enumerate(biblioteca):
                    print(f"[{i}] {livro.titulo} ({'Disponível' if livro.disponivel else 'Emprestado'})")
            case 2:
                rent = int(input('Qual livro gostaria de pegar? '))
                biblioteca[rent].emprestar()    
            case 3:
                back = int(input('Qual livro gostaria de devolver? '))
                biblioteca[back].devolver()
            case 4:
                break
            case _:
                print('Ação inválida')