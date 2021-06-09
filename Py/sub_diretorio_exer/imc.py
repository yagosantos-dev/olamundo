print("calculo do imc ")

nome = str(input("qual o seu nome ? "))

peso = float(input("qual o seu peso atual? "))

altura = float(input(" qual a sua altura? "))

imc = peso / (altura * altura)  


print(f" ola {nome} seu imc é de {imc:.2f}")

if (imc < 18.5):
    print("sua classificação na tabela imc é de magreza ")
elif (imc == 18.5 or imc <= 24.9):
    print(" sua classficação na tabela imc esta como normal")
elif (imc >= 25.0):
    print("voçe ja inicou na classificação da tabela imc como sobrepesso deve se cuidar mais cuidado ")
