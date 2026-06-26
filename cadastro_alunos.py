from rich import print
from rich.console import Console
from rich.table import Table


base_dados = []

# função que recebe os dados e criar um dicionario
def cadastro_aluno(nome,idade,nota):
   alunos = {
       'nome':nome,
        'idade':str(idade),
        'nota':str(nota)}
   # enviar o dicionario para uma lista
   base_dados.append(alunos)

        
def exibir_cadastro():
    print()
    #titulo da tabela
    tabela = Table(title="Lista de alunos", style='green')
    # adicionando as colunas com formatação e cores
    tabela.add_column("Nome", justify="right", style="cyan", no_wrap=True)
    tabela.add_column("Idade", style="magenta")
    tabela.add_column("Nota", justify="right", style="green")
    
    # inserindo os dados na tabela
    [tabela.add_row(base['nome'],base['idade'],base['nota']) for base in base_dados]
    # ------------------------------------------------------
    # mesmo codico acima escrito de maneira diferente
    #for base in base_dados:
    #    table.add_row(base['nome'],base['idade'],base['nota'])   
    # ------------------------------------------------------
    
    console = Console()
    console.print(tabela)
    

        
cadastro_aluno('fernando gomes',32,10)
cadastro_aluno('Joao',32,5.8)
cadastro_aluno('maria',5,5.6)

exibir_cadastro()

