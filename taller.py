#Crear una matriz de Numpy aleatoria de 4 dimensiones y un size de 1200000
import numpy as np
matriz=np.random.rand(10,15,20,40)
# print(matriz)

#Crea una copia de la matriz creada en el ítem anterior (usar método copy) de solo 3 dimensiones (“Cortando una de las dimensiones”)
matriz_3d= matriz[:, 0, :, :].copy() #15
print(matriz_3d)