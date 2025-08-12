# El elefante está en una posición inicial de 0. La cantidad máxima de metros que puede dar en un paso es 5.
# Se debe calcular la cantidad mínima de pasos para llegar a la posición final x.

import math

posicion_inicial = 0
posicion_final = int(input("Ingrese la posición final (x): "))

distancia = abs(posicion_final - posicion_inicial)
pasos = math.ceil(distancia / 5)

print(f"El elefante necesita {pasos} paso(s) para llegar a la posición {posicion_final}.")