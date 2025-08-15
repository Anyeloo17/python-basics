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



#FUNCION IMPUT





