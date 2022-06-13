#7- función radicación, retorna la raiz del primero respecto del segundo.
def radicacion ():
    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    radicacion= num1 ** (1/num2)
    print("El resultado de la radicación es:",str(radicacion))
radicacion()
