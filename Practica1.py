# Codigo que solicita una variable
nombre = input("Como te llamas?") 
print("Hola " + nombre)

edad = input("Cuantos años tienes?") 
x = int(edad) # Forzamos edad a ser un valor entero
if x < 18 :
  print("Eres menor de edad")
if x >= 18 :
  print("Eres mayor de edad")
  
print("Buen día!")