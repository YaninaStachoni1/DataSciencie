import numpy as np
import pandas as pd

#Crear un arreglo de ceros de longitud 12
arreglo1=np.zeros(12)
print('Ejercicio 1:', arreglo1)
#Crear un arreglo de longitud 10 con ceros en todas sus posiciones y un 10 en la posición número 5
arreglo2=np.zeros(10)
arreglo2[4]=10
print('Ejercicio 2:', arreglo2)
#Crear un arreglo que tenga los números del 10 al 49
arreglo3=np.arange(10,50)
print('Ejercicio 3:', arreglo3)
#Crear una arreglo 2d de shape (3, 3) que tenga los números del 0 al 8
arreglo4=np.arange(0,9)
arreglo=np.array(arreglo4)
arreglo_2d=arreglo4.reshape(3,3)

print('Ejercicio 4:')
print(arreglo_2d)
print(type(arreglo_2d))

#Crear un arreglo de números aleatorios de longitud 100 y obtener su media y varianza
arreglo5=np.random.random(100)

print('Ejercicio 5:')
print('Arreglo de números aleatorios', arreglo5)

media=np.mean(arreglo5)
varianza=np.var(arreglo5)

print('La media es:', media)
print('La varianza es:', varianza)

#Calcular la media de un arreglo usando np.sum
arreglo6=np.random.random(50)
suma=np.sum(arreglo6)
tamano=np.size(arreglo6)
media2=suma/tamano

print('La media del arreglo usando np.sum es:', media2)
#Calcular la varianza de un arreglo usando np.sum y np.mean
arreglo7=np.random.random(10)
media3=np.mean(arreglo7)
suma3=np.sum((arreglo7-media3)**2)

varianza3=suma/len(arreglo7)

print('Ejercicio 7')
print('La varianza de un arreglo usandp np.sum y np.mean es:', varianza3)

#Crear un array de números aleatorios usando np.random.randn.
arreglo8=np.random.randn(10)
print('Ejercicio 8:', arreglo8)