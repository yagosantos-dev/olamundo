print("calculo do desconto")
produto = float(input("Qual o valor do produto ? "))
desconto = float(input("Qual o valor do desconto? "))

resu = produto * desconto / 100

preco_final = produto - resu

print(f"o produto custava {produto} com o desconto de {desconto}% o preço final é de {preco_final:.2f}")