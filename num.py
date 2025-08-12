import numpy as np # np es un aleas para recortar el nombre de numpy

vector = np.array([1, 2, 3, 4, 5])#Creamos un vector de numpy
print(vector) #Imprimimos el vector
#Quiero imprimir el tercer elemento del vector
print(vector[2])

"""
 Los vectores no son como las listas, no tienen un método append()
 para agregar elementos y no tienen un método pop() para eliminar elementos,
 pero sí tienen método reshape() para cambiar su forma, adicionalmente despues
 de creado no se puede cambiar el tamaño del vector

"""

vector1 = np.zeros(5)# Imprimimos el vector de ceros
print(vector1)
vector2 = np.ones(5)# Imprimimos el vector de unos
print(vector2)
vector3 = np.arange(1,10)# Imprimimos el vector de rango del 1 al 10
print("rango",vector3)
vector4 = np.linspace(1, 10, 5) #Creamo un vector de 5 números entre 1 y 10
print("linspace",vector4)
vector5 = np.random.rand(10)#Numeros aleatorias del 0 a 100
print(vector5)
vector6 = np.random.randint(1, 10, 10)
print(vector6)