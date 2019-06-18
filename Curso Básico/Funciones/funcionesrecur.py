def factorial(x):
    if x== 1:
        return 1
    elif x== 0:
        return 1
    else:
        x=(x*factorial(x-1))
    return x

n=int(input('Numero del que desea sacar el factorial: '))

print('El factorial de ' + str(n) + ' es: ' + str(factorial(n)))
