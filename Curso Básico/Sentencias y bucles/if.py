num = int(input('Escribe un numero: '))

if num<0:
    print('El numero que escribiste es negativo.')
elif num==0:
    print('El numero que escribio es 0.')
elif num>0:
    print('El numero que escribio es positivo.')

#Aqui haremos un ejemplo del uso de if pero ahora con variables ya dadas.

i= int(input('Escribe un numero: '))

j= int(input('Escribe... otro numero xd: '))

print('\n')

if(i==j):
    print('Los numeros son iguales')
else:
    print('Los numeros no son iguales')

print('\n')

if(i<j):
    print('El primer numero es menor que el segundo.')
else:
    print('El primer numero es mayor que el segundo.')

print('\n')

if(i>=j):
    print('El primer numero es mayor o igual que el segundo.')
else:
    print('El segundo numero es mayor que el primero.')

#Aqui haremos un ejemplo con las variables leidas anteriormente pero con
#operadores logicos

print('\n')

if (i and j)==10:
    print('Los numeros son iguales a 10.')
else:
    print('Los numeros no son iguales a 10.')

print('\n')

if (i or j)==10:
    print('Uno de los numeros es 10.')
else:
    print('Ningun numero es 10.')
