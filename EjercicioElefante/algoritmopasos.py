# El elefante está en una posición inicial de 0. La cantidad máxima de metros que puede dar en un paso es 5.
# Se debe calcular la cantidad mínima de pasos para llegar a la posición final x.



import math

lugarinicial = 0


try:
    lugarfinal = int(input("Diguite el lugar donde quieres llegar en candidad de metros:"))

    
except ValueError:
    print("¡Debe ingresar un número entero!")
    exit()


distancia =abs(lugarfinal - lugarinicial)
CantidadPasos = math.ceil(distancia /5)
print(f"El elefante da una cantidad de pasos evaluado en {CantidadPasos} pasos para llegar al final del objetivo {distancia} metros.")






#COMO FUNCIONA LA FUNCION CEIL DEF
def mi_ceil(numero):
    parte_entera = int(numero)  # Trunca el número (elimina decimales)
    if numero > 0 and numero != parte_entera:
        return parte_entera + 1
    elif numero < 0 and numero != parte_entera:
        return parte_entera  # Para negativos, el "techo" es el entero truncado
    else:
        return parte_entera  # Si ya es entero, se devuelve igual