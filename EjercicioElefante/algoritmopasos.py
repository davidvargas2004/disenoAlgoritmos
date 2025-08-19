# El elefante está en una posición inicial de 0. La cantidad máxima de metros que puede dar en un paso es 5.
# Se debe calcular la cantidad mínima de pasos para llegar a la posición final x.



# import math

# lugarinicial = 0


# try:
#     lugarfinal = int(input("Diguite el lugar donde quieres llegar en candidad de metros:"))

    
# except ValueError:
#     print("¡Debe ingresar un número entero!")
#     exit()


# distancia =abs(lugarfinal - lugarinicial)
# CantidadPasos = math.ceil(distancia /5)
# print(f"El elefante da una cantidad de pasos evaluado en {CantidadPasos} pasos para llegar al final del objetivo {distancia} metros.")













import math 

lugarstart= 0
try:
    lugarfinal=int(input("digite el numero de comienzo:"))
except ValueError:
    print("debe poner numeros enteros:")
    exit();


recorrido= (lugarfinal - lugarstart)
pasos=math.ceil(recorrido / 5)
print(f"el elefante da una cantidad de {pasos} en una distancia de {recorrido}")