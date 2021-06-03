print(" maior de idade ")
idade = int(input("qual a sua idade ? "))

if (idade == 18):
    print("voçe é maior de idade , ja pode dirigir ")
elif (idade >=16 and idade < 18 ):
    print("nos EUA é permitido tirar a CNH para maiores de 16 mas por enquanto voẽ ainda não tem 18 anos ")
    print(f"espere mais  {18 - idade} anos para completar 18 anos e poder dirigir ")
elif(idade > 100):
    print("voçe é maior de idade porem nessa idade não é seguro continuar dirigindo ...")
else:
    print(" não pode dirigir ainda ")
    print(f"ainda falta {18 - idade} anos ainda para completar 18 anos e poder dirigir ")
