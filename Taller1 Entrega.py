#Presentado por Ivan Camilo Rosales Rodriguez y David Ricardo Guzmán Mora

#Numpy
import numpy as np # Importamos numpy como el alias np

#EJERCICIO
#Crear dos vectores de diez numeros aleatorios enteros entre 1 y 10:

#Sumarlos
a=np.random.randint(1,11,size=(10))
print(a)
b=np.random.randint(1,11,size=(10))
print(b)
#Suma de vector a+b
print(a+b)

#Concatenar
c=np.concatenate((a,b))
print(c)

#Sumatoria de los valores
print(sum(c))

#Media de los valores
from statistics import mean
print(sum(c)/len(c))
print(mean(c))

#Imprimir numeros mayores que 5
print(c[c>5])

#Determinar las posiciones que son iguales en los arrays
print(a)
print(b)
print(np.where(a==b))

#SQL

import sqlite3
# Create a SQL connection to our SQLite database
con = sqlite3.connect("guia_fasecolda.sqlite")
cur = con.cursor()


#AQUI Realize sus consultas sql de los datos (3 querys)

for row in cur.execute('SELECT * FROM carros WHERE Cilindraje <1200 and Cilindraje > 1000;'):
   print(row)

for row in cur.execute('SELECT Marca, Clase FROM carros WHERE Peso >1200 and Servicio=="Publico";'):
   print(row)

for row in cur.execute('SELECT * FROM carros WHERE TipoCaja <>"MT" and Nacionalidad=="IND";'):
   print(row)

#Be sure to close the connection.
#con.close()

#PANDAS Ejercicios

import pandas as pd
import sqlite3
from IPython.display import display, HTML


#Query
df = pd.read_sql_query('SELECT * FROM carros WHERE Peso >1200 and Servicio=="Publico"', con)

#Revise la distribución de sus datos
print(df.describe())

#Calcule la correlación
print(df.corr())

display(HTML(df.describe().to_html()))

display(HTML(df.corr().to_html()))


#Comprender los datos con visualización

#1. Cargar el dataset
data=pd.read_csv("guia_fasecolda.csv")

#2. Usar función columns para ver las columnas
print(data.columns)


#3 4 y 5 Filtre, describa y guarde los datos filtrados

data1=data[['Peso','Cilindraje','Potencia']]
print(data1.describe())
print(len(data1))
print(data1.shape)
data1.info()

data2=data[data.Marca=='FUSO']
print(data2.describe())
print(len(data2))
print(data2.shape)
data2.info()
print(data2['Servicio'].value_counts())

data3=data[data.Peso > 250]
print(data3.describe())
print(len(data3))
print(data3.shape)
data3.info()
print(data3['Nacionalidad'].value_counts())


#6 Gráficas de los datosmatplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np

plt.figure()
data['Bcpp'].plot(kind = 'box',ylim=(-1000,200000))
plt.title('mi primera grafica Bcpp')
plt.show()

data['Potencia'].plot(kind = 'box',ylim=(-10,1000))
plt.title('mi primera grafica Potencia')
plt.show()

plt.figure()
plt.hist(data['Potencia'], bins=5,color=('green'))
plt.show()


sns.kdeplot(data['Potencia'])
plt.title('Gráfico de densidad de la función Cilindraje')
plt.show()

plt.figure()
plt.hist(data['Clase'], bins=5,color=('purple'))
plt.show()


plt.scatter(data['Cilindraje'],data['Bcpp'],c="red")
plt.title('Scatter plot entre Cilindraje y Bcpp')
plt.axes
plt.show()


#CONCLUSIONES

#1.Preguntas de Análisis de datos con generación de valor
#¿Cuál es el modelo o tipo de vehículo más vendido?
#Esto permite al comercializador importar y darle prioridad a los modelos con mayor potencial de venta.
#¿De acuerdo al país, cuáles son las características más demandadas al comprar un vehículo?
#Al fabricante o ensamblador de vehículos le permite focalizar su esfuerzo de ventas hacia los países, dependiendo
#del tipo de modelo más demandado.

#2. Con qué otra base de datos se podría trabajar para obtener valor de estos datos
#Se plantean dos opciones:
    
#a. Base de datos de infracciones de tránsito, que permita identificar las características de los carros
#más proclives a cometer infracciones.
#Enlazado con lo anterior, se podrían geolocalizar en donde se encuentran estos vehículos, para focalizar la vigilancia en estas zonas.
#y priorizar la presencia de cámaras y agentes de tránsito en estas zonas.

#b.Base de datos de alertas ambientales, para relacionar los vehículos más contaminantes de la ciudad
#y focalizar la vigilancia y control en las zonas de mayor presencia, también con georreferenciación.
 

#3. Plantea preguntaa de ML Supervisado y No Supervisado que pienses generen valor a esta data

#No supervisado. 
#Desde un punto de vista de mercadeo, haríamos una agrupación o clustering con las 
#principales características de los vehículos de la base, para entender los distintos grupos y
#generar estrategias diferenciadas de venta para cada uno de los clúster que se creen.

#Supervisado. 
#Se proponen dos aproximaciones con modelos de regresión lineal, cuyo objetivo es:
 #1. Determinar el valor de unidades vendidas para un año x.
 #2. Determinar la cantidad estimada de CO2 que producen, para evitar la compra o importación de estos vehículos
    #lo que serviría para la orientación de políticas públicas para el reemplazo a vehículos híbridos o limitar la 
    #importación de los que sean más contaminantes.
