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
# while True:
#     print("socorro xD")
# print("fin?")
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

####

##ESTA TAL ELELENTO EN UNA LISTA?

print(7 in lista) #esto hace la pregunta
#Comolo hariamos sin in? Pues con bucles

existe= False #variable inicialización
valor=7 #el valor a comprobar
cuenta=0 #pa contar cuantas veces existe

for elemento in lista:
    print('estamos en el elemento ',elemento)
    if elemento==valor:
        existe=True
        cuenta=cuenta+1
        break #cuando se de el true, se acaba el bucle, y no mira todos los elementos,
        #al ver que ya existe uno, se para
print('Se acabo el loop')
print(existe)
print(cuenta)

#PROBELMAS DE MAYOR Y MENOR 
print(max(lista)) #comandos para hacerlo
print(min(lista)) #comandos para ahcerlo

#Con bucle lo harías así:
mayor= None #none pq poner 0 es malo pq si hay numeros negativos ya el 0 es mayor
menor= None 

for elemento in lista:
    if mayor==None or menor==None: #primera iteracion
        mayor=elemento
        menor=elemento
        #así, la primera iteracion es decir q el primer elementoe s mayor y menor, en
        #vez de inicializarlo directamente decarando eso.
    else: #esto es el rest de iteraciones
        if elemento>mayor: #el igual no es necesario, pq ya está guardado.
            mayor=elemento
        if elemento<menor:
            menor=elemento
print(mayor)
print(menor)


        #############################
##########MODULO 5 ############
##########################3##

##FUNCIONES

def suma(sumando1,sumando2): #definición de la función    
    print (f' el resultado es {sumando1+sumando2}')
    print(f'la lista anterior era {lista}')
suma(3,5) #llamada a la función
#OJO, aqui sí puedes acceder a las variables de fuera, no hace falta global, como en
#MATLAB.Esto en modo lectura.  Para modificarla sí ahce falta:
    
def funcion():
    global lista #para modificar el valor de la variable ya definida lista
    lista=[33,333,3333]
    print(lista)
funcion() 

#Return

def sumaa(sumando1, sumando2):
    total=sumando1+sumando2
    return total 
resultado=sumaa(5,7) #eso te guarda la variable, debido al return.
#recuerda q el return corta la funcion, y se sale, asi q debe ser lo último

def sumaaa(sumando1, sumando2):
    total=sumando1+sumando2
    return total,'mi mensaje' 
resultado,mensaje=sumaaa(5,7) #asi se guardarían ambas cosas, aunq es una forma rara 
#de guardar cosas, no te voy a mentir. 

##LIBRERIAS

import math #importas el paquete o librerías de mates
help(math) #te da todo lo que puede hacer

math.cos(math.pi) #cálculo del coseno de pi

#LLAMANDO A FUNCIONES DESDE OBJETOS

mitexto='fuck, its sunday'
#De help(str) veo todas las cosas q puedo hacer cone so, y una es:
    
str.title(mitexto) #esto pone Fuck, Its Sunday, mayus al principio de cada palabra
#Tb podría ahcer:
mitexto.title() #da lo mismo, y es mas simple. 

#Para encadenar llamadas:
mitexto.replace('Fuck','God') #cambia Fuck for God
#tb podría ahcer el title ahora:
mitexto.replace('Fuck','God').title()


##############################
##########MODULO 6############
##############################
 
#QUE SON LAS CADENAS DE TEXTO

refran='el perro de san roque no tiene rabo ' #caracteres encadenadosq se guardan
 #puede empezar tb por comilla doble, "
 #una operacion comun es concatenarlas:
refran=refran+'porque ramon rodriguez se lo ha cortado'
print(refran)
#las \ ayudan a organizarse para saber donde empieza y acaba la linea:
refran='el perro de san roque no tiene rabo \
    porque ramon tus muertos' 
    #tras la lines \ no debe encontrar nada, debes ir aparte, linea abajo
#la indentacion no importa una vez usada la barra, fijate en lo de arriba por 
#ejemplo

#para poner saltos de linea:
 refran='el perro de san roque no tiene rabo \n \
    porque ramon tus muertos'    
print(refran)
#otra forma es con ''',pero es peor pq considera los saltos de lineas y espacios
#tb como caracteres
 refran='''el perro de san roque no tiene rabo
        porque ramon tus muertos
        m'''    
print(refran)
aa='''s'''

#TRABAJANDO CON LAS CADENAS
refran='Predicado tus muertos'
len(refran) #longitud cadena, espacios incluidos
refran[0] #primer elemento
refran[len(refran)-1] #esto da error, el ultimo elemento es len-1. eso es pq empiezas
#a  contar en el 0
refran[0:10] #muestra los elementos del 0 al 10
refran[:5] #del principio al 5
refran[10:] #del 10 al final
refran[:-5] #del principio hasta el final menos los 5 ultimos caracteres
refran[-5:] #desde los ultimos 5 hasta el final


#FUNCIONALIDADES DE LAS CADENAS

help(str) #te da el resto de cosas que se pueden ahcer
#algunos de los mas usado son:
refran.lower() #lo pone en minuscila todo    
refran.upper() #lo pone en mayus todo  
refran.capitalize() #pone mayus la priemra letra de la linea
refran.replace('tus','mis') #cambia la primera palabra por la segunda
refran.find('tus') #busca la palabra, y dice la posición, donde empieza
    #find da -1 cuando no la encuentra. Distingue mayus de minus!
refran.strip() #esto quita espacias al comienzo y al final
refran.split() #crea una lista separando las palabras
refran.split('tus') #escoge este elemento, lo quita, y parte la cadena en ese punto,
    #teniendo 2 elementos, los de antes de la palabra, y los de despues

frase='Tengo una casa roja'
frase[frase.find('casa'):frase.find('casa')+len('casa')] #así extraes casa, y 
#lo pones

#EXTRAER TROZOS DE UNA CADENA

#estamos trabajando con una serie de datos los cuales vienen almacenados en cadenas
#tipo: 'categoria':'valor numerico'.Crea funcion q usando el find de la posicion del
#¢aracter : y en el return devuelva un float con el valor conteindo tras dicho caracter

datoProblema="Peso : 82.3"

def EncuentraValor(dato):
    posicion=dato.find(':')
    #return posicion #eso devuelve la posicion
    valor=dato[posicion+1:] #q dé desde la posicion hasta el final
        #el +1 pa q no de los :
    valor=float(valor) #pa q lo convierta en un real
    return valor

EncuentraValor(datoProblema)

#comprobacion:
assert EncuentraValor(datoProblema)==82.3,'Ejercicio completo'

#CODIGOS DE CARACTERES

 letra="a"
 ord(letra) #da el caracter alfanumerico de una letra. En este caso,la a la 
#representa un 97 
 #los caracteres, poner 1, etc
 chr(89) #da la letra que representa el caracter alfanumerico, lo inverso de antes
 #En este caso, da Y
 
 cadena="Hola hola niños jujujujajaja"
 for letra in cadena:
     print(ord(letra),end=" ") #el end=" " te lo pone en fila, en vez de en columna
     #y con un espacio
print('fin')

#Esto sería una forma de encriptar de forma muy sencilla, llamado cifrado César
#en roma se usaba algo así, pero con A=1, B=2, etc.

#vamos a crear una cadena codificada con un despalzamiento de 5:
cadenacodificada="" #inicializacion de la cadena codificada
desplazamiento=5
for letra in cadena:
    cadenacodificada=cadenacodificada+chr(ord(letra)+desplazamiento)

print(cadena)
print(cadenacodificada)

#y para decodificar:
cadenadecodificada="" #inicializacion de la decodificacion
    
for letra in cadenacodificada:
    cadenadecodificada=cadenadecodificada+chr(ord(letra)-desplazamiento)
print(cadenadecodificada) #y la ha decodificado

###Ejercicio 6.3(no evaluable)
#Escribe una función enelmedio que dadas dos cadenas nos devuelva una sola cadena
# de modo que la segunda quede en el medio de la primera tal y como se muestra 
#en los ejemplos.
"""
    enelmedio('[::]','polipo')
    -> '[:polipo:]'
    enelmedio('rocodromo','XXX')
    -> 'rocoXXXdromo'
    enelmedio('-:..:-','Título')
    -> '-:.Título.:-'
"""

import math #tu use the trunc function to truncate, vital for the function

def enelmedio(cadena_a_introducir,cadena):
    #lo primero es distinguir si la cadena es par o impar. En caso de par, la 
    #division es facil: ej: con 6, 3, cadena a introducir, y 3
    #recuerda que empieza por el 0 a contar!
    if len(cadena)%2==0: #cadena par
        cadena_nueva=cadena[0:int(len(cadena)/2)] #primera mitad
            #el int es pq devuelve un float, 2.0, y quiero 2
        cadena_nueva=cadena_nueva+cadena_a_introducir
        cadena_nueva=cadena_nueva+cadena[int(len(cadena)/2):] #segunda mitad
    else: #cadena impar
        #en este podemos partirlo como: 5, 2 y luego 3==>medio-1, cosa a añadir,
        #y luego medio+1
        cadena_nueva=cadena[0:int((len(cadena))/2)] #primera mitad
            #int() tb trunca!!!
        cadena_nueva=cadena_nueva+cadena_a_introducir
        cadena_nueva=cadena_nueva+cadena[int(len(cadena)/2):] #segunda mitad
    return cadena_nueva
    
enelmedio('X','holaa')   


#Solucion de los profes
def enelmedio(primera,segunda):
    mitad = len(primera)//2
    principio = primera[:mitad]
    final = primera[mitad:]
    resultado = principio+segunda+final
    print(f'el resultado de tu llamada es {resultado}')
    return resultado

enelmedio('holaa','X')
#No tengo ni puta idea de por qué le funciona, si si meto una palabra impar,
#mitad es impar, y ya se jode todo. Pero no se jode, y npi pq

mitad=len('holaa')/2
principio='holaa'[:mitad]
final='holaa'[mitad:]
resultado=principio+'X'+final

#He preguntado a ver si me dicen qué pasa¿??¿¿?¿??¿?¿¿??¿

###ACT 6.4
#Escribe una función cambiamayus que dadas una cadena nos devuelva la misma 
#cadena cambiando las mayusculas por minúsculas y viceversa.
"""
Ejemplo:

    cambiamayus('Castilla')
    -> 'cASTILLA'
    cambiamayus('ENTretenido')
    -> 'entRETENIDO'
    cambiamayus('PaliNdrOmo')
    -> 'pALInDRoMO'
"""
#Una forma que se me ocurre es un loop, que cada palabra la cambie de mayus a minus

def cambiamayus(palabra):
    palabra_new='' #Vacio, inicializaicon
    for letra in palabra:
        if letra.lower()==letra: #letra en minuscula==> ponla en mayus
            letra_nueva=letra.upper()
        else: #letra en mayus==> la pongo en minus
            letra_nueva=letra.lower()
        palabra_new=palabra_new+letra_nueva
    return palabra_new
cambiamayus('OrAle')

#Sol del profe:
def cambiamayus(cadena):
    resultado=''
    for letra in cadena:
        if letra.islower():
            resultado += letra.upper()
        else:
            resultado += letra.lower()
    return resultado        
#Vmos que es una forma mas guay de preguntar si es mayus o minus. en help(str) te viene
        
#################################
########MODULO 7################3 
################################3

###DOCUMENTO DE TEXTO

#Para acceder a un archivo de texto, como ejercicio.csv (comma separated values)
#hacemos:
    
archivo=open('ejercicio.csv','r') #ela rchivo en nuestra carpeta. r read
archivo.read() #esto abrira el archivo y lo convierte en una cadena
archivo.close() #esto lo cierra
#y tras cerrarlo no podrias abrilo con .read(). Si no lo cierras, no lo puedes abrir
#con otra cosa, como por ejemplo excel
#

#read: lo abro, guardo el contenido, lo imprimo, y lo cierro
archivo=open('ejercicio.csv','r') 
contenido=archivo.read() 
print(contenido)
archivo.close() 
#el print es bueno, una linea detras de otra, los saltos de line \n los ha puesto
#como saltos. Al final se mete otro salto de linea

#Readline: leer linea a linea
archivo=open('ejercicio.csv','r') 
linea0=archivo.readline() #ir leyendo linea a cada, cada vez q lo ejecutas es una linea
linea1=archivo.readline()
print(linea0) #eso es primera linea
print(linea1) #eso la segunda
print(linea0.strip()) #para quitar saltos de lineas y caracteres invisibles
print(linea1.strip()) 
archivo.close() 

#tb podría leerse todas las lineas con bucle for, claro:
archivo=open('ejercicio.csv','r') 
for linea in archivo.readlines():
    print(linea.strip())
archivo.close()
#Esto es útil para archivos muy grandes, pq .read() le cuesta mucho al ordenador.

#Tell te dice en que caracter del archivo está:
archivo=open('ejercicio.csv','r')    
print(archivo.tell())
linea0=archivo.readline()
print(archivo.tell())
archivo.close()

#Seek te busca un punto del archivo
archivo=open('ejercicio.csv','r')    
archivo.read()
print(archivo.tell()) #te dice q estás en el ultimo caracter, y por ello si ahces
#de nuevo read, no te da nada. PAra volver al 0, puedes usar el seek:
archivo.seek(0) #si pones 4, va al 4, y así
print(archivo.tell())
archivo.close()

#Write
archivo=open('Archivo.extension','w+') #no existe, así q me lo creo
#archivo.write('nueva cadena en el archivo') #añadimos esa linea
archivo.write('nueva cadena en el archivo\n') #añadimos esa linea, con salto de linea
archivo.close()

#Para añadirle cosas a ese archivo debemos de abrilo con a
archivo=open('Archivo.extension','a+')
archivo.write('cadena para flushear hermano')
archivo.flush() #leer descripcion abajo
archivo.close()
#puntero al final, por eso se añaden cosas al final de la cadena. Con el w+, se
#añaden al principio. Cada vez que ejecutes esto con a+ añade lineas. al cerrarlo 
#se ponen las lineas en el archivo. TB se podria frzar la ejecucion sin cerrarlo
#diciendole: archivo.flush()

#Otra forma de abrir archivos es with open. LA ventaja es que cuando falla algo cierra
#el archivo. Y el manejador soloe stará disponible dentro de entorno:
with open('Archivo.extension','r') as archivo:
    print(archivo.read())
print(archivo.read()) #esto daría error por estar fuera, pq el archivo está cerrado.  
#aunq hubiese errores, al acabar por los errores se cerraría.  

###TRABAJANDO CON CADENAS DE FICHEROS DE TEXTO

#Ejercicios con documentos I

#1) Cuenta las lineas que tiene el archivo.csv con python
#lo primero es abrirlo
manejador=open('ejercicio.csv') #si no se pone nada es como poner 'r'
#para leer habria q usar un bucle for

cuenta=0 #inicializacion
for linea in manejador:
    cuenta=cuenta+1
print(f'el archivo ejercicio.csv tiene {cuenta} líneas')
manejador.close()

'''
Una forma de contar palabras del archivo:
    manejador=open('prueba.txt') 
    data=manejador.readlines() 
    cuenta=0 
    for linea in data:
        for palabra in linea.split(' '): 
            cuenta=cuenta+1 
    print(cuenta)
OJO, ES READLINES, QUE LEE TODAS LAS LINEAS Y LAS PONES ASÍ EN LINEAS, POR ESO
ESTO CUENTA TODAS LAS PALABRAS, Y NO LAS PALBRAS DE UNA LINEA!
'''

#2) Encontrar palbras en un archivo: en el ejercicio anterior, ahz que se muestren
#las lineas que contienen run

manejador=open('ejercicio.csv') 
for linea in manejador:
    if 'run' in linea: #buscará run, q encontrará con running
        print(linea.strip()) #lo del strip par quitar saltos
manejador.close()

#3) Seleccionando archivos: modifica 1) para que nos permita seleccionar qué
#archivo queremos utilizar al contar las lienas usando el comando input

nombre_archivo=input('Introduce el nombre del archivo a abrir: ')
manejador=open(nombre_archivo) 
cuenta=0 #inicializacion
for linea in manejador:
    cuenta=cuenta+1
print(f'el archivo {archivo} tiene {cuenta} líneas')
manejador.close()

#4) Protección de errores: modifica el ejercicio anterior para evitar errores si
#el usuario escribe mal el nombre del archivo, cuando falle mostraremos un mensaje
#que diga: No se ha encontrado el archivo {nombre de archivo}.
#Esto se peude hacer con try except

try:   
    nombre_archivo=input('Introduce el nombre del archivo a abrir: ')
    manejador=open(nombre_archivo) 
    cuenta=0 #inicializacion
    for linea in manejador:
        cuenta=cuenta+1
    print(f'el archivo {archivo} tiene {cuenta} líneas')
    manejador.close()
except:
    print(f'No se ha encontrado el archivo {nombre_archivo}')
#Y esto es mucho más bonito.

###TRABAJANDO CON CODIGOS DE CARACTERES EN FICHEROS DE PYTHON

#Creamos una funcion que abra un fichero y borre todos los parrafos menos uno
def parrafo(numero_de_parrafo):
    
    #fichero=open('quijote.txt','r',encoding='utf-8')      #otra opcion es ansi
    fichero=open('quijote.txt','r',encoding='ansi')
        #la codificacion es para asegurar que se lee bien. E texto está en utf8, pero
        #el pc a lomejor usa otra. Ej: windows usa ansi, asi q no daría las comas
        
    texto=fichero.read()                #lo leemos
    parrafos= texto.split('\n') #dividimos en parrafo por salto de linea \n
    while '' in parrafos: #para quitar lineas en blanco
        parrafos.remove('')
    parrafo_seleccionado=parrafos[numero_de_parrafo] #el parrafo seleccionado
    fichero.close() #cerrar e fichero
    return (parrafo_seleccionado)

parrafo(8)

###7.1, EJERCICIO NO EVALUABLE
#En el archivo adjunto 'quijote.txt' hemos dejado los primeros párrafos del 
#libro que comparte nombre con el archivo. La función 
#primerafrase(numerodeparrafo) deberá abrir el archivo y devolver el contenido
# de la primera frase del párrafo indicado (siendo 0 el primer párrafo). 
#La primera frase estará definida por los caracteres que se encuentran en 
#el párrafo hasta llegar al primer símbolo de puntuación 
#(cualquiera del grupo ,.:;), tal y como se muestra en el ejemplo a continuación.
'''
    primerafrase(0)
    -> 'En un lugar de la Mancha'
    primerafrase(2)
    -> 'Con estas razones perdía el pobre caballero el juicio'
'''

def primerafrase(numero_de_parrafo):
    fichero=fichero=open('quijote.txt')                 #read only
    texto=fichero.read()
    parrafos= texto.split('\n')     #da una lista, con elementos alternos:
        #el 0 primer parrafo, el 1 nada, el 2 segundo parrafo, y así
    #para eliminiar los parrafos vacios del list, se hace:
    while '' in parrafos:           #para quitar lineas en blanco de parrafos
        parrafos.remove('')   
        parrafo_seleccionado=parrafos[numero_de_parrafo]    #este es el parrafo
        #del que debemos extraer las palabras hasta un punto. Podriamos hacerlo
        #con un bucle, rompiendolo al encontrar el punto
    frase=''                                            #inicialización
    for letra in parrafo_seleccionado:
        if letra=='.' or letra==',' or letra==':' or letra==';':
            break
        frase=frase+letra
    return frase
    fichero.close()
primerafrase(2)

#Y la solucion del profe, mucho más rara:
def primerafrase(parrafo):
    #primero cargamos el fichero
    fichero = open('quijote.txt')
    #lo leemos
    texto = fichero.read()
    #y seleccionamos el párrafo indicado en el parámetro 
    parrafos = texto.split('\n')
    #eliminamos los párrafos vacios tras el split 
    while '' in parrafos: 
        parrafos.remove('')    
    parrafoseleccionado=parrafos[parrafo]
    #vamos a buscar donde acabaría la primera frase buscamos los delimitadores que nos han pedido 
    #y añadimos sus posiciones a una lista
    delimitadores =[]
    delimitadores.append(parrafoseleccionado.find(','))
    delimitadores.append(parrafoseleccionado.find('.'))
    delimitadores.append(parrafoseleccionado.find(':'))
    delimitadores.append(parrafoseleccionado.find(';'))
    #quitamos los -1 que son delimitadores no encontrados y nos puede dar lugar a errores
    while -1 in delimitadores: 
        delimitadores.remove(-1)
    #y obtenemos el primero que aparece con el comando min (el menor es el primero)
    finfrase = min(delimitadores)

#nuestra frase sera pues
frase = parrafoseleccionado[:finfrase]
print(frase)
#acordaros de cerrar el fichero si no lo habeis abierto con un with
fichero.close()    
return(frase)    