hora = float(input("qual o hora? "))

if (hora == 0 or hora <= 11):
    print("bom dia")
elif (hora == 12 or hora <= 17):
    print("boa tarde")

elif(hora == 18 or hora <= 23):
    print("boa noite")
else:
    print("hora invalida")