import numpy as np
import pandas as pd

#Leo el archivo de datos
expvida=pd.read_csv('life_expectancy_data.csv', delimiter=',')

print(expvida.index)

# Obtengo el tipo de estructura de datos

tipo=expvida.dtypes
print('El tipo de estructura de datos es:')
print(tipo)

# Uso .shape para obtener cantidad de filas y columnas
print('La cantidad de filas y columnas es:')
print(expvida.shape)
# Obtengo el nombre de las columnas
print('Los nombres de las columnas son:')
print(expvida.columns)

# Inspecciono las primeras filas
filas=expvida.head(10)
print('Las primeras 10 filas son:')
print(filas)

# Inspecciono las ultimas 10 filas
filas2=expvida.tail(10)
print('Las últimas 10 filas son:')
print(filas2)


# Obtengo la cantidad de datos faltantes en cada columna
faltantes=expvida.isnull().sum()
print('Hay valores faltantes?')
print(faltantes)

# Obtengo el maximo valor de datos faltantes y lo guardo en la variable masnan
masnan=max(faltantes)
print('El máximo valor de datos faltantes es:')
print(masnan)

# Obtengo la cantidad de filas total y divido el maximo valor de datos faltantes por este numero
# y lo multiplico por 100

cantidad_de_filas=len(expvida)

print('La cantidad de filas es:', cantidad_de_filas)

variable1=(masnan/cantidad_de_filas)*100

print('El resultado del ejercicio 10 es:', variable1)

# Imprimo el maximo porcentaje de datos faltantes. Uso f-strings.

#primero calculo el porcentaje de datos faltantes por columna
porcentaje_colum=(faltantes/cantidad_de_filas)*100

#calculo el porcentaje maximo de datos faltantes
max_faltantes=porcentaje_colum.max()

#escribo el porcentaje maximo en un f-string
max_porcentaje=f"{max_faltantes:.2f}%"

print(f"El porcentaje máximo de datos faltantes en la tabla es: {max_porcentaje}")

# Renombro columnas del DataFrame


expvida.rename(columns={'Life expectancy ': 'life_expectancy', ' BMI ': 'bmi', 'Measles ': 'measles'}, inplace=True)


# Obtengo el promedio de la columna

promedio = expvida['life_expectancy'].mean()


print('El promedio total de la columna life_expectancy es:', promedio)

# Obtengo el promedio por pais
promedio1 = expvida.groupby('Country')['life_expectancy'].mean()

print('El promedio de expectativa de vida usando pandas por país es:')
print(promedio1)

# Maxima expectativa de vida usando pandas
maxima1=promedio1.max()
print('El valor maximo de expectativa de vida usando pandas es:')
print(maxima1)

# Maxima expectativa de vida usando numpy
maxima2=np.max(promedio1)
print('El promedio de expectativa de vida usando numpy por país es:')
print(maxima2)

# Minima expectativa de vida usando numpy
minima1=np.min(expvida['life_expectancy'])
print('La mínima expectativa de vida usando NumPy es:')
print(minima1)

# Minima expectativa de vida usando pandas
minima2=expvida['life_expectancy'].min()
print('La mínima expectativa de vida usando pandas es:')
print(minima2)

# Filtro las columnas para mostrar solo las filas que tengan valor igual al maximo

filamax= expvida.loc[expvida['life_expectancy'] == maxima1]
print('La fila con el valor máximo de expectativa de vida es:')
print(filamax)
# Filtro las columnas para mostrar solo las filas que tengan valor igual al minimo
filamin= expvida.loc[expvida['life_expectancy'] == minima1]
print('La fila con el valor minimo de expectativa de vida es:')
print(filamin)

# Obtengo los valores unicos de la columna status
valores_unicos=expvida['Status'].unique()
print('Los valores unicos de la columna Status son:')
print(valores_unicos)

# Cuento cuantos valores hay de cada categoria
paises_status=pd.Series(expvida['Status']).value_counts()

print("Cantidad de países en cada categoría de 'Status':")
print(paises_status)

# Cuento cuantas filas tienen valores distintos de cero

expvida_2015=expvida[expvida['Year'] == 2015]
paises_con_sarampion_2015=expvida_2015[expvida_2015['Measles '] != 0]['Country'].count()

print('Los países que presentaron algún caso de sarampion son:')

print(paises_con_sarampion_2015)