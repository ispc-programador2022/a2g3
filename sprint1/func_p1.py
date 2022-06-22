##Sprint2##
####funcionp1, retorna la suma de los 2 primeros por el 3er parámetros, usando las funciones anteriores.####
from func_suma import suma
from func_producto import producto
def func_p1 (num1,num2,num3):
    suma= suma(num1,num2)
    ope= producto((suma, num3))
    return ope