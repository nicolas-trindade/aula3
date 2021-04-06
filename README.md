# aula3
Este programa é um exercício da cadeira de linguagem de programação, onde foi passado a linguagem python.

O exercicío proposto era:

Crie um banco de dados SQL e uma tabela, denominada clientes, com o Python. A tabela
clientes, deve ter os seguintes dados:

• Nome;
• Idade;
• Endereço;

Após a criação do banco e da tabela, adicione pelo menos dois registros nesta tabela. Para
verificar se os registros foram mesmo adicionados, apresente-os para o usuário.
Use módulos para separar a criação do banco das demais funcionalidades.

Como estávamos aprendendo sobre classes, metódos, funções e objetos juntamente a manipulação de banco da dados resolvi dar uma incrementada no exercicio:

1- Criei o banco de dados com a tabela cadastro ao invés clientes (nada que interferisse no resultado final)

2- Resolvi fazer um arquivo main e uma classe para mandar as funções de SQL diretamente pela classe (para me desafiar no aprendizado)

3- Fazendo uma classe, criei as funções nesta classe e no main pego os dados do usuário e encaminho para as funções.

Resultado:

Temos 3 arquivos: 

- criarBanco.py onde cria o banco de dados e a tabela através do sqlite3

- main.py onde o programa principal roda

- Classe.py onde estão todas as funções do programa


O programa em si é bem simples, consiste em adicionar dados, consultar todos os dados da tabela, consultar dados por nome e excluir dados por nome também.
Fiz controle de algumas situações:

1 - Se existe algum registro na tabela

2 - Se o existe o nome consultado

3 - Se o existe o nome para excluir (Caso não tenha, aparece mensagem relatando que não foi possível deletar)

Algumas observações:

- Não encontrei como deixar o resultado formatado, para aparecer mais apresentável para o usuário na hora de imprimir o resultado.
 
- Quando há pessoas com o mesmo nome, o registro apaga todos registros com o mesmo nome.

- Pode se desenvolver melhor o programa. Como o exercício proposto ja era bem simples e resolvi deixá-lo com um pouco mais dificuldade,
me atentei a fazer a classe e as funções funcionarem e não tanto nos outros testes que podem ser feitos. As funções me fizeram pensar muito
e por muitas vezes me vi perdido com questões de como fazer para declarar as variáveis e de como mandar os valores para as funções e classe.

É ISTO, ESTE README TERMINA POR AQUI.
