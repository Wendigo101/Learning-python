a="Predicado Tus muertos"
print(a)

#Esto es un coment
"""esto

tambien es un comment, pero de varias lineas"""


############
a=10
c=a/5
str(c)

#Tipos de variables
numero=0
cadena="Hola putos"
lista=[1,2,3,4]
lista[3] #Da el tercer elemento de lista
lista[0] #Da el primer elemento!!!!!!!

tupla=("adios","hola")
diccionario={"nombre":"puto"}

diccionario["nombre"] 
#Esto reporta "puto"

##########################

print("conhesumadre")
34 #034 no le vale, el 0 a la izq no lo puedes poner

#########Funciones varias

type(1234) #int=integer
type(55.5) #float=real
type(6+4j) #complex
type("hello") #hello
type([1,2]) #List
type({"a":"b"}) #dictionary
type((1,2)) #Tuple

help(int) #Te da aiuda del tipo de dato 
dir([1,2]) #Te da las funcionalidades disponibles para esa clase.

##Fuciones de conversion
AB=345
3+float(AB) #Esto funciona, y da 348

#Funciones input
edad=input("dime tu edad, puto: ") #Esto te pide el numero, y lo guarda en edad

#Expresiones
3+2
3-2
3*2
3/2
3%2 #Esto es el resto de la división
3**2 #Esto es el elvado (WTF python)
-3
+3
#Operaciones con cadenas
"hola "+"mundo" #las une
"puto "*10 #las une 10 veces

#Logic operations
1>2
1<1
1==3

"aa" is "a"*2 #Esto es como el ==, pero mas fuerte. Da true

letra="a"
"aa" is letra*2 #Esto da false, aunq sean lo mismo, y es pq no son el mismo objeto, 
#aunq valgan lo mismoç
"aa"==letra*2 #Esto da true

not False #esto da true
False or True #Esto da True
False or False #Esto da false
False and True # Esto da false
True and True # Esto da True


#############################
##########MODULO 3, FLUJO VARIABLE############
##########################3##

A=2

if A==4:
    print("A=4")
elif A>2:
    print("2<A<4")
else:
    print("A<2")
print("end del condicional")


########Playing with loops

palabra='Oraleputo'

for letra in palabra:
    print(letra)
print("fin loop estandar")

#Para hacer un for loop con index, se puede con la función range:
    
range(5)
range(0,5) #esto da lo mismo que lo de arriba
list(range(0,5)) #esto da [0,1,2,3,4]
list(range(2,7)) #esto da [2,3,4,5,6]

for i in range(0,len(palabra)):
    print(palabra[i])
print("fin bucle con index")

#Continue
for i in range(0,len(palabra)):
    if palabra[i]=='o':
        continue
    print(palabra[i])
print("fin bucle con index y continue")

#Infinite loop with while
while True:
    print("socorro xD")
print("fin?")
#Crtx+c to end the loop

####################3
###################

print(3+4)
33

print("tus muertos",33)
print("tus muertos",4,"es mejor que",33) #podrias poner una variable, claro. Para
#controlar los espacios podrías hacer
print(f"tus muertos:{4} es mejor que {33}") #no espacio entre : y 4.


##########

edad=20
if edad>=18:
    print('a beber ijoputa')
  #print('esto cone spacios mamon') #Esto da error, por tener espacios y no estar a la
  #par
    print('esto con espacios hasta alinear')  #esto funciona
print('end')
#Ejemplo con funciones

def funcionSuma():
    a=5
    b=3
    print(a+b)
funcionSuma()

#####################
##Bloques try y except

try:
    valor=input("escribe un número: ")
    valor_numerico=int(valor)
    resultado=valor_numerico+3
    print(resultado)
except Exception as e:
    print("Hemos sufrido un error debido a que: ",str(e))
print("fin")

#otra opcion sería en el except redefinir valor_numerico, de modo que si
#introduces algo malo, uso ese de except. 

#ejemplo discriminando según errores

try:
    valor=input("escribe un número: ")
    valor_numerico=int(valor)
    resultado=3/valor_numerico
    print(resultado)
except ArithmeticError:
    print('Error aritmético (divide by 0)')
except ValueError: #no has metido numero, sino letras
    valor_numerico=0
except Exception as e: #esto es un error mas general
    print("Hemos sufrido un error debido a que: ",str(e))
print(valor_numerico)
print(resultado)
print("fin")

#Ahora incluimos el bloque finally

try:
    valor=input("escribe un número: ")
    valor_numerico=int(valor) #lo convierte de caracteres a numero (un numero)
    resultado=3/valor_numerico
    print(resultado)
except ValueError: #no has metido numero, sino letras
    valor_numerico=0
finally:
    print(valor_numerico)
print("fin")

#############################
##########MODULO 4 RESOLVIENDO COSAS############
##########################3##

#pAR O IMPAR?

num= input("introduce numero, zorra: ") #esto es una cadena
numInt=int(num) #esto ya sí es un número

if numInt%2==0:
    print("el número es par")
else:
    print("es impar")

#ESCRIBE LOS DIVISBLES ENTRE 5 Y 7 MENORES O IGUALES QUE EL NUMERO(
#EL NUMERO DEBER SER ENTERO Y POSITIVO)

num= input("introduce numero, zorra: ") #esto es una cadena
numInt=int(num) #esto ya sí es un número
#Para hacer un bucle entre el 0 y el numero usaremos range
list(range(0,numInt)) #no se incluye el número
for numero in range(0,numInt+1): #el +1 para incluir el numero introducido
    if numero%5==0 or numero%7==0:
        print('el número',numero, 'cumple con los requisitos')

#CONTAR LOS ELEMENTOS        

#cpntar elementos de una lsita
lista=[1,2,3,45,5,6,7,7]
print(len(lista))
#Y sin usarla? 

cuenta=0 #inicializacion

for elemento in lista: #Bucle
    cuenta=cuenta+1
    print(f'el elemento que estamos añadiendo es el {elemento} y ocupa el orden {cuenta}')
    
print('en total hay',cuenta,'elementos') #Fin

#SUMAR VALORES
lista=[1,2,3,45,5,6,7,7]
print(sum(lista)) #Esto suma los valores fasi y sensillo
#Sin usarla, podriamos usar un bucle:

suma=0
for elemento in lista:
    suma=suma+elemento
print('la suma total es',suma)

#CALCULANDO MEDIAS
 lista=[1,2,3,45,5,6,7,7]
print(sum(lista)/len(lista)) #Esto da la media de la lista

#Como lo hariamos sin sum ni length?Pues tendríamos que contar los elementos,
#por otro sumarlos, y listo.

cuenta=0
suma=0

for elemento in lista:
    cuenta=cuenta+1 #contar elementos
    suma=suma+elemento #sumar elementos
media=suma/cuenta
print('la media es',media)