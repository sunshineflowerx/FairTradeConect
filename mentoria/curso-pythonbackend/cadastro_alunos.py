alunos = []

def cadastrar_aluno():
    try:
        nome = input("Digite o nome do aluno: ")
        matricula = int(input("Digite a matrícula do aluno: "))
        curso = input("Digite o curso do aluno: ")
        aluno = {
            "nome": nome,
            "matricula": matricula,
            "curso": curso
        }
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")
    except:
        print("Erro no cadastro: número da matricula deve ser inteiro!")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, Curso: {aluno['curso']}")
            
def buscar_matricula():
    try:
        matricula_busca = int(input("Digite a matrícula do aluno que deseja buscar: "))
        for aluno in alunos:
            if aluno['matricula'] == matricula_busca:
                print(f'aluno encontrado: Nome: {aluno["nome"]}, Matrícula: {aluno["matricula"]}, Curso: {aluno["curso"]}')
                return
            print("Aluno não encontrado.")
            
    except:
        print("Erro na busca: número da matricula deve ser inteiro!")

def menu():
    while True:
        print("Menu de Cadastro de Alunos")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Buscar Aluno por Matrícula")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cadastrar_aluno()
        elif escolha == '2':
            listar_alunos()
        elif escolha == '3':
            buscar_matricula()
        elif escolha == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.") 
            
menu()
