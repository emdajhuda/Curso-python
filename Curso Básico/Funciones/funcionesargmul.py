def promedio(*args):
    total=0
    for i in args:
        total+=i
    resultado=total/len(args)
    return resultado

a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())

p=promedio(a,b,c,d,e)

print('El promedio es:')
print(p)
