import sqlite3
conector = sqlite3.connect("aula3.db")
cursor = conector.cursor()

class Funçao:

    def cadastro(self, nome, idade, endereco):
        cursor.execute("""
        INSERT INTO cadastro (nome, idade, endereco) VALUES (?, ?, ?)
        """, (nome, idade, endereco))
        conector.commit()
        print('Dados cadastrados com sucesso!')

    def consulta(self):
        cursor.execute("""
        SELECT * FROM cadastro""")
        conector.commit()
        dados = cursor.fetchall()
        if len(dados) == 0:
            print('Não há resultados para esta pesquisa!')
        else:
            for d in dados:
                print(d[0],' | ', d[1],' | ', d[2])

    def consultaNome(self, nome):
        cursor.execute("""
            SELECT * FROM cadastro WHERE nome = ?
            """, [nome]) #COLOCAR VARIAVEL NOME ENTRE COLCHETES, POIS SENAO ELE CONSIDERA O NUMERO DE CARACTERES
        conector.commit()# DA VARIAVEL E NAO O VALOR EM SI
        dados = cursor.fetchall()
        if len(dados) == 0:
            print('Não há resultados para esta pesquisa!')
        else:
            for d in dados:
                print(d[0],' | ', d[1],' | ', d[2])


    def excluir(self, nome):
        cursor.execute("""
                    SELECT nome FROM cadastro WHERE nome = ?
                    """, [nome])
        conector.commit()
        dados = cursor.fetchall()
        if len(dados) == 0:
            print('Não foi possível deletar estes dados pois não foi encontrado resultados para este nome"!')
        else:
            cursor.execute("""
                delete from cadastro where nome = ?
                """, [nome])
            conector.commit()
            print('Dados excluídos com sucesso!')

    def fechar(self):
        cursor.close()
        conector.close()
"""
 QUANDO TENTEI FAZER DESTE JEITO, NÃO FUNCIONAVA, APRESENTAVA ESTE ERRO:
 
 valueerror operation parameter must be str
 
 PROCUREI EM ALGUNS LUGARES E NADA DE RESOLVER, DA FORMA QUE FICOU LÁ EM CIMA NO CADASTRO RESOLVEU.
 
 sql = "INSERT INTO cadastro (nome, idade, endereco) VALUES (?, ?, ?)"
print(sql, nome, idade, endereco)
cursor.execute(sql, (nome, idade, endereco)) """