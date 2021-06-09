print("==== PAR OU IMPAR ==== \n")

n = input("Digite o numero para saber se ele é impar ou par : ")
re = n.isnumeric()
print()
print("-"*6)
print()

if (re != True):
    print("não é um numero inteiro  o que foi digitado ")
else:
    if (int(n)) % 2 == 0:
        print(f"[{n}] é par \n ")
    else:
        print(f"[{n}] é impar \n")
print("obrigado por usar nosso programa ")