def dividir(a, b):
  try:
    r = a/b
  except ZeroDivisionError:
    print ("Division por cero!")
  else:
    print ("El resultado es: " + str(r))
  finally:
    print ("Ejecutando la clausula finally")
a=int(input())
b=int(input())
dividir(a,b)
