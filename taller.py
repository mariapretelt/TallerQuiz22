#Crear una matriz de Numpy aleatoria de 4 dimensiones y un size de 1200000

import numpy as np
import pandas as pd
from scipy.io import loadmat

matriz=np.random.rand(10,15,20,40)
print('Primer punto')
print(matriz)

#Crea una copia de la matriz creada en el ítem anterior (usar método copy) de solo 3 dimensiones (“Cortando una de las dimensiones”)
matriz_3d= matriz[:, 0, :, :].copy() #15
print('\n Segundo punto')
print(matriz_3d)

#De la matriz 3D, muestra todos los atributos propios de dicha matriz , dimensión, tamaño, etc..
print(f"\nForma: {matriz_3d.shape}")
print(f"Dimensión: {matriz_3d.ndim}") #num de dim
print(f"Tamaño: {matriz_3d.size}")
print(f"Tipo de datos: {matriz_3d.dtype}")
print(f"Tipo del objeto: {type(matriz_3d)}")
print(f"Tamaño en bytes de elementos: {matriz_3d.itemsize}")
print(f"Tamaño memoria: {matriz_3d.nbytes}")

#Modificar su forma y pasarla a 2D
matriz_2d= matriz_3d.reshape(matriz_3d.shape[0], -1)
print('\n 4to Punto')
print(matriz_2d)

# Crea una función que reciba la matriz anterior y la pase a un objeto tipo dataframe de 
# Pandas 

def dataframe(m):
    return pd.DataFrame(m)
df=dataframe(matriz_2d)
print('\n 5to Punto')
print(df)

# Crear una función que permita cargar un archivo .mat y .csv 

print('Punto 6')

def cargar_archivo(ruta):
    if ruta.endswith('.csv'):
            df = pd.read_csv(ruta)
            return df
    elif ruta.endswith('.mat'):
         datos = loadmat(ruta)
         return datos 
    else:
        print('Solo se permiten .csv y .mat')
        return None

         
#Crear funciones de suma, resta, multiplicación, división, logaritmo ,promedio, desviación 
# estándar NOTA: Estas funciones deben permitir hacer estos procesos a lo largo de un eje 
# (usando Numpy)

def suma(matriz, axis=None):
    return np.sum(matriz, axis=axis)

def resta(matriz, valor, axis=None):
    return np.subtract(matriz, valor)  

def multiplicacion(matriz, valor, axis=None):
    return np.multiply(matriz, valor) 

def division(matriz, valor, axis=None):
    return np.divide(matriz, valor)  

def logaritmo(matriz, base=np.e, axis=None):
    if base == np.e:
        return np.log(matriz) 
    else:
        return np.log(matriz) / np.log(base)  

def promedio(matriz, axis=None):
    return np.mean(matriz, axis=axis)

def desviacion_estandar(matriz, axis=None):
    return np.std(matriz, axis=axis)

