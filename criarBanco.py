import sqlite3

conector = sqlite3.connect("aula3.db")
cursor = conector.cursor()

sql = "create table cadastro (nome text, idade integer, endereco text)"

cursor.execute(sql)
cursor.close()
conector.close()

print("Abra a pasta do programa e veja se o arquivo está lá")
print("Fim do programa")