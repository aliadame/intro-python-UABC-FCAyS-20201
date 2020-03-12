# El siguiente algoritmo resuelve el problema
# para realizar la suma o multiplicaciones
# de dos numeros dependiendo su valor
a = 0
b = 0
c = 0
a = float(input("Ingrese el primer numero:"))
b = float(input("Ingrese el segundo numero:"))
if a > 0 or b > 0 :
  print("Suma de numeros")
  c = a + b
else :
  print("Multiplicacion de numeros")
  c = a * b
print("El resultado de la operacion es: ", c)