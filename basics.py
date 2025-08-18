#el modulo print() sirve para mostrar informacion en la cosola
print('hola mundo')
#los tipos de texto strings o str siempre van entre comillas o dobles comillas
#con la funcion print tambien se pueden  imprimir varios valores distintos
print('hola','soy','nuevo')
#se opueden agregar parametros all final de la funcion print como por eejemplo:SEP (indica con simbol se va a separar una palabra de la otra ) y END (indica un salto de linea y ademas podemos agregar un 
# simbolo o no para q aparezca algo en el espacio de la primera cadena de texto y la segunda)
print("hola","mundo", sep="-")
print("hola", "mundo", end="?")
print('eesto continua en la misma liena por el parametro end')
#TIPOS DE DATOS EN PYTHON:INT(ENTEROS (SON LOS NUIMEROS SIN COMA)),STR(STRINGS (SON LAS LETRAS O PALABRAS)),(FLOAT(SON LO SNUMEROS CON COMA)) BOOL( cualquier accion logica coomo falso  verdadero o la comparacion de valores),
#  NONETYPE ( REPRESENTA AL AUSENCIA DE VALOR ) LIST,TUPLE,DICT,RANGE,SET,COMPLEX
print("int:")
print(231)
print(-5)
print(31232314342423422131)

print('srt:')
print('hola')
print('234dawdaw')

print("bool:")
print(type(True))
print(type(False))
print(type(1 < 5))

print("nonetype:")
print(type(None))
#podemos usar la funcion TYPE para saber q tipo de datos es cada cual escribiendo el comando type dentrro de al funcion print yy encerrando en parentesis el dato q queremos saber
print(type(5))
print(type('hola mundo'))
print(type(0.5))
print(type(1 < 6))
print(type(None))

#VARIABLES
#son espacios de memoria donde se guardan datos y se les asigna un nombre
#para crear  uan variable se  usa el signo igual(=) y se le asigan un nombre o valor
x=5
name="anyelo la bestia la maquina el animal"
print(x)
print(name)
#tipado dinamico: en python no es necesiario declarar el tipo de dato en una variable ya q lo hace automaticamente
#y podemoscambair el tipo de dato de uan variable en cuanquier momento 

# tipado fuerte:python no hace conversiones de tipos de datos automaticamnete, por lo q sisumamos un int y un str nos dara un error
#para cambiar el tipo de dato de una variable se usa la funcion srt() o int() ofloat() o bool() segun el tipo de dato q queramos cambiar
x=5

print(type(x))
print(type(str(x)))

pan=54
print(pan)
#asi convertimos un int en str
pan=str(pan)
print(type(pan))
#la funcion f-strings permite crear cadenas de texto con variables dentro de ellas Y cada variable va encerrada entra llaves{}
nombre="anyelo"
edad=18
ciudad="miami"
print(f"hola me llamo {nombre}, tengo {edad} y vivo en {ciudad}")


#FUNCION IMPUT
# Para obtener datos del usuario se usa la función input()
# La función input() recibe un mensaje que se muestra al usuario
# y devuelve el valor introducido por el usuario
nombre = input("Hola, ¿cómo te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

# Ten en cuenta que la función input() devuelve un string
# Así que si queremos obtener un número se debe convertir el string a un número
age = input("¿Cuántos años tienes?\n")
age = int(age)
print(f"Tienes {age} años")

# La función input() también puede devolver múltiples valores
# Para hacerlo, el usuario debe separar los valores con una coma
print("Obtener múltiples valores a la vez")
country, city = input("¿En qué país y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")


#CONDICINALES (if, else, elif)
print("\n Sentencia simple condicional")
# Podemos usar la palabra clave "if" para ejecutar un bloque de código
# solo si se cumple una condición.
edad = 18
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

# Si no se cumple la condición, no se ejecuta el bloque de código
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

# Podemos usar el comando "else" para ejecutar un bloque de código
# si no se cumple la condición anterior del if
print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

print("\n Sentencia condicional con elif")
nota = 5

# Además de usar "if" y "else", podemos usar "elif" para determinar
# múltiples condiciones, ten en cuenta que sólo se ejecutará el primer bloque
# de código que cumpla la condición (o la del else, si está presente)
if nota >= 9:
  print("¡Sobresaliente!")
elif nota >= 7:
  print("Notable!")
elif nota >= 5:
  print("¡Aprobado!")
else:
  print("¡No está calificado!")

#podemos uasar operadores logicos como AND, OR , NOT para combinar condiciones

print("\n sentencia condicinal con operadores logicos")

edad =3
if edad >= 18 and edad < 60:
  print("eres un adulto")

if edad ==18 or edad==60:
  print("eres mayor de edad")

if edad ==3:
  print('eres  muy joven')
else:
  print('eres un adulto mayyotr')


