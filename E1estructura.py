# A CONTINUACION PROFE VERA TODOS LOS RESULTADOS A LOS EJERCICIOS QUE MANDO ALGUNOS EJERCICIOS NO FIGURAN QUE QUE ESTABAN RESUELTOS 
#EN EL COLAB 

#EJERCICIOS RESULTOS POR Larrea Hugo 



# **1 - GANÁ MILLAS PARA EL DESTINO PYTHON**

#¿Cómo vamos a validar si lo que ingresa el usuario por teclado es un número?

#Responde "A es mejor" o "B es mejor":


#Tus comentarios (opcional):

#-------------------------------------------------
""""
OPCION A

cadena=input("Ingrese un número entero:")
try:
  numero = int(cadena)
  print(f"El usuario ingresó: {cadena}")
  print(f"Convertido a número entero es: {numero}")
except:
  print(f"{cadena} no es un número entero")

"""

#------------------------------------------------

"""
OPCION B

numero=int(input("Ingrese un número entero:"))

"""

#----------------------------------------------

#Respuesta  = para mi la opcion A es la correcta



#---------------------------------------------

# **2 - GANÁ MILLAS PARA TU DESTINO PYTHON**

#¿Es cierto que ambos algoritmos hacen lo mismo?

#Responde "VERDADERO, ambas opciones hacen lo mismo" o "FALSO, no hacen lo mismo":



#Tus comentarios (opcional):


#Para los dos algoritmos siguientes la respuesta el  VERDADERO


#-------------------------------------------------- 
# **3 - Ganá millas para tu destino Python**

#Este algoritmo solicita al usuario que ingrese 10 números enteros y calcula la suma de todos los números enteros ingresados.

#Responde cuál es la opción correcta:

#Tus comentarios (opcional):

#Ganás millas opcionales extra, si te animás a hacer el diagrama de flujo, con la opción que consideras correcta.


#Respuesta = opcion C

#-----------------------------------------
# Imagen del diagrama de flujo adjuntada 
#-----------------------------------------
 
#----------------------------------------

# Ejercico 4


# Paso 2: Pedir al usuario que ingrese el valor a.
# Paso 3: Pedir al usuario que ingrese el valor b.
# Paso 4: Mostrar todos los números enteros en el rango desde a hasta b.


# Respuesta en funcio a ejercios 2,3,4

A=int(input("ingresa un numeoro A= "))
B=int(input("ingresa un numero B= "))


for i in range(A,B):
  print (i)

#--------------------------------------------------------

#Ejercicio 5


# **5 - Ganá millas para tu destino Python**

#Mirá este desarrollo paso a paso, y completá en cada parte del código donde dice completar, reemplazá la palabra "pass" por lo que consideres adecuado.

#Tus comentarios (opcional):

# Paso 1: Dado un número entero, veamos si es positivo, en caso contrario, es negativo o cero.

numero=int(input("ingrese numero "))
if numero > 0:
  print(f'El número {numero} es positivo.')
else:
  print(f'El número {numero} es negativo o cero.')
#---------------------------------------------------------------------

#segun codigo complete defienendo en la funcion  numero dandole ingreso

# Paso 2: Definimos una función positivo() que recibe un número entero
#         Devuelve 1 si la entrada es positivo.
#         Devielve 0 si la entrada es un número negativo o cero.

numero_entrada=int(input("numero "))
def positivo(numero_entrada):
 
  if numero_entrada > 0:
    salida=1
  else:
    salida=0
  return salida

print(positivo(numero_entrada))

#-------------------------------------------------------------------

# Paso 3: Modificamos la función anterior para que en vez de un número,
#         recibe una cadena como parámetro de entrada.
#         Intentamos ver si esa cadena es un número, antes de ver si es positivo.
#         Si el número es positivo, la función devuelve 1.
#         Si no es un número, o bien, es negativo o es cero,
#         La función devuelve 0.


cadena=input("Escriba aqui..")

def positivo(cadena):
  try:
    numero_entrada=int(cadena)
    if numero_entrada > 0:
      salida=1
    else:
      salida=0
  except:
    salida=0
  return salida

print(positivo(cadena))

#--------------------------------------------------------------


# Paso 4: Solicitamos al usuario que ingrese un número entero
#         Llamamos a la función positivo para que nos devuelva
#          1 si es un número entero positivo
#          0 si es negativo o cero o no es un número.
#         Recuerda que la función que quedó definida en el paso anterior,
#         No hace falta volver a definirla, la podemos usar en este paso.

algo=input("Ingrese un número entero a continuacion: ")

espositivo=positivo(algo)

if espositivo:
  print(f"El usuario ingresó un número positivo: {algo}")
else:
  print(f"El usuario ingresó algo que no es un número positivo.")

#-----------------------------------------------------------------

# Paso 6: Pasamos en limpio lo que desarrollamos hasta ahora

# Definimos la función positivo

cadena=input ( "ingrese numero:")
def positivo(cadena):
  try:
    numero_entrada=int(cadena)
    if numero_entrada > 0:
      salida=1
    else:
      salida=0
  except:
    salida=0
  return salida
print(positivo(cadena))

# Llamamos la función positivo

algo=input("Ingrese un número entero: ")

n=positivo(algo)

if espositivo > 0 :
    print(f"El usuario ingresó un número positivo: {n}")
else:
    print(f"El usuario ingresó algo que no es un número positivo.")

#-----------------------------------------------------------------------

# Paso 7: Llamamos a la función positivo mientras el usuario ingrese números positivos.

algo=input("Ingrese un número entero: ")

espositivo=positivo(algo)

while espositivo:
  if espositivo > 0:
    print("Resultado positivo")
  else:  
    pass
print("Termina porque no ingresa número entero positivo")






