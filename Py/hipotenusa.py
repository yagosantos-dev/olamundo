print("hipotenusa")

co = float(input("comprimento do cateto oposto: "))

ca = float(input("comprimento do cateto adjacente: "))

hi = (co ** 2 + ca ** 2) ** (1/2)

print("A hipotenusa vai medir {:.2f}".format(hi))

#agora usando o import para ficar mais simples 

#import math 

#ca = float(input("comprimento do cateto adjacente: "))

#co = float(input("comprimento do cateto oposto: "))

#hi = math.hypot(co,ca)

# voçe escolhe a melhor forma