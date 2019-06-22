numero=int(input("Que numero quieres saber si es primo? "))
valor=(range(2,numero))
print(valor)
contador=0

for n in valor:
    if (numero % n) == 0:
        contador +=1
        print("Divisor: " + str(n))

if contador > 0:
    print("El numero no es primo.")

else:
    print("EL numero es primo.")
