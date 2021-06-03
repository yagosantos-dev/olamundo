from random import choice 
print("quem vai apagar a loja !")

aluno1 = input("qual o nome do aluno? ")

aluno2 = input("qual o nome do aluno? ")

aluno3 = input("qual o nome do aluno? ")

aluno4 = input("qual o nome do aluno? ")

lista = [aluno1,aluno2,aluno3,aluno4]

print("o aluno sorteado foi {}".format(choice(lista)))