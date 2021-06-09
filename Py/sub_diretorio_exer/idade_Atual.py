nome = input("qual o seu nome ? ")
nascimento = int(input("qual a data do seu nascimento ? "))
anoAtual = int(input("qual o ano atual ? "))

idade =  anoAtual - nascimento 

print(f"ola {nome} sua idade atual é de {idade} anos de idade !")

# a varialvel idade foi usado para armazenar o valor da idade atual caso seja necessario usar esse valor em outro local do programa
#porem podemos fazer a idade atual dele direto pelo print

#print(f" ola {nome} sua idade atual é de  {anoAtual - nascimento} anos de idade ")

#voçe escolhe qual print usar 