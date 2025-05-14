#Crear una matriz de Numpy aleatoria de 4 dimensiones y un size de 1200000

import numpy as np
import pandas as pd
from scipy.io import loadmat
import matplotlib.pyplot as plt

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

# Buscar en Kaggle un archivo .csv relacionadas con alguna patología, descargar y hacer 
# funciones como las propuestas en el ítem anterior, pero implementándolas usando Pandas 
# y que permitan tambien elegir columnas.

# Cargar el archivo CSV

df = pd.read_csv("diabetes.csv")
print(df.head()) #priemras filas de dataframe

def suma(df, columnas=['Glucose', 'BMI']):
   
    if columnas:
        return df[columnas].sum()
    return df.sum()

def resta(df, columnas=None, valor=0):

    if columnas:
        return df[columnas] - valor
    return df - valor

def multiplicacion(df, columnas=None, valor=1):
   
    if columnas:
        return df[columnas] * valor
    return df * valor

def division(df, columnas=None, valor=1):
   
    if columnas:
        return df[columnas] / valor
    return df / valor

def logaritmo(df, columnas=None, base=np.e):
   
    if columnas:
        return np.log(df[columnas]) / np.log(base)
    return np.log(df) / np.log(base)

def promedio(df, columnas=None):
    
    if columnas:
        return df[columnas].mean()
    return df.mean()

def desviacion_estandar(df, columnas=None):
   
    if columnas:
        return df[columnas].std()
    return df.std()
print("\nPromedio de Age:")
print(promedio(df, columnas=['Age']))

#Usar matplotlib para graficar la señal del archivo mat del punto 6 y crear funciones para 
# graficar histogramas, stems, barras, pies 

# def graficarmat(ruta, nombre_variable='signal'):
#     datos = loadmat(ruta)
#     if nombre_variable in datos:
#         senal = datos[nombre_variable]
#         plt.figure(figsize=(10, 4))
#         plt.plot(senal)
#         plt.title(f'Señal de {nombre_variable} del archivo')
#         plt.xlabel('Tiempo')
#         plt.ylabel('Amplitud')
#         plt.grid(True)
#         plt.tight_layout()
#         plt.show()
#     else:
#         print(f"La variable no se encontró en el archivo.")

# def histograma(datos, titulo="Histograma", bins=10):
#     plt.figure()
#     plt.hist(datos, bins=bins, color='skyblue', edgecolor='black')
#     plt.title(titulo)
#     plt.xlabel('Valores')
#     plt.ylabel('Frecuencia')
#     plt.grid(True)
#     plt.show()
# def graficar_stem(datos, titulo="Gráfico Stem"):
#     plt.figure()
#     markerline, stemlines, baseline = plt.stem(datos, use_line_collection=True)
#     plt.setp(markerline, color='blue')
#     plt.setp(stemlines, color='green')
#     plt.title(titulo)
#     plt.xlabel('Índice')
#     plt.ylabel('Valor')
#     plt.grid(True)
#     plt.show()
# def graficar_barras(labels, valores, titulo="Gráfico de Barras"):
#     plt.figure()
#     plt.bar(labels, valores, color='orange')
#     plt.title(titulo)
#     plt.xlabel('Categoría')
#     plt.ylabel('Valor')
#     plt.grid(axis='y')
#     plt.show()
# def graficar_pie(labels, valores, titulo="Gráfico de Pastel"):
#     plt.figure()
#     plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
#     plt.title(titulo)
#     plt.axis('equal')  # Para que el gráfico sea circular
#     plt.show()

#Las funciones de graficación deben pedir al usuario los títulos de gráficos y los ejes, activar 
# leyendas , activar la cuadricula.

def graficarmat(ruta, nombre_variable='signal'):
    datos = loadmat(ruta)
    if nombre_variable in datos:
        senal = datos[nombre_variable].squeeze()

        titulo = input("Título del gráfico: ")
        xlabel = input("Etiqueta del eje X: ")
        ylabel = input("Etiqueta del eje Y: ")

        plt.figure(figsize=(10, 4))
        plt.plot(senal, label=nombre_variable)
        plt.title(titulo)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print(f"La variable '{nombre_variable}' no se encontró en el archivo.")
def histograma(datos, bins=10):
    titulo = input("Título del gráfico: ")
    xlabel = input("Etiqueta del eje X: ")
    ylabel = input("Etiqueta del eje Y: ")
    leyenda = input("Nombre de la leyenda para la serie: ")

    plt.figure()
    plt.hist(datos, bins=bins, color='skyblue', edgecolor='black', label=leyenda)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()
def graficar_stem(datos):
    titulo = input("Título del gráfico: ")
    xlabel = input("Etiqueta del eje X: ")
    ylabel = input("Etiqueta del eje Y: ")
    leyenda = input("Nombre de la leyenda para la serie: ")

    plt.figure()
    markerline, stemlines, baseline = plt.stem(datos, use_line_collection=True, label=leyenda)
    plt.setp(markerline, color='blue')
    plt.setp(stemlines, color='green')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()
def graficar_barras(labels, valores):
    titulo = input("Título del gráfico: ")
    xlabel = input("Etiqueta del eje X: ")
    ylabel = input("Etiqueta del eje Y: ")
    leyenda = input("Nombre de la leyenda para la serie: ")

    plt.figure()
    plt.bar(labels, valores, color='orange', label=leyenda)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(axis='y')
    plt.show()
def graficar_pie(labels, valores):
    titulo = input("Título del gráfico: ")
    plt.figure()
    plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title(titulo)
    plt.axis('equal')
    plt.show()




