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


#####Flujo condicional

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