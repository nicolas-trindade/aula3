import Classe

op = 1
dados = Classe.Funçao()
while op != 0:
    x = int(input("DIGITE UMA OPÇÃO: \n 1 - ADICIONAR DADOS \n 2 - CONSULTAR TODOS DADOS \n "
                  "3 - CONSULTAR P/ NOME \n 4 - EXCLUIR DADOS POR NOME \n 0 - SAIR \n"))

    if x == 1:
        nome = str.upper(input("DIGITE UM NOME : "))
        idade = int(input("DIGITE UMA IDADE : "))
        endereco = str.upper(input("DIGITE UM ENDEREÇO : "))
        dados.cadastro(nome, idade, endereco)


    elif x == 2:
        dados.consulta()

    elif x == 3:
        nome = str.upper(input("DIGITE UM NOME PARA CONSULTAR: "))
        dados.consultaNome(nome)

    elif x == 4:
        nome = str.upper(input("DIGITE UM NOME PARA EXCLUIR OS DADOS: "))
        dados.excluir(nome)

    elif x > 4 or x < 0:
        print("ESTA OPÇÃO NÃO É VÁLIDA")

    else:
        dados.fechar()
        break

