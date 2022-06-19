#### Ejercicio 4 - Cociente de dos parametros y salida por consola

from bienvenida import bienvenida

def cociente ():
    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    if num2!=0:
      cociente= num1/num2
    else:
      num2=int(input("Ingrese un número distinto de cero: "))
      cociente= num1/num2
      
    print("El resultado del cociente es:",str(cociente))
    
bienvenida()
cociente()

##### Fin ejercicio 4