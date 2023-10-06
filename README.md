# Programming

# Aplicacion

from datetime import date
from dateutil.relativedelta import datetime.now() # type: ignore
now = datetime.now()
print(now)
relativedelta = months = 1 
now = now + relativedelta(months=1, weeks=1, hour=10) # type: ignore

print(now)

# Copia de seguridad 

 import sys

 print(sys.argv)
 print(sys.argv[0]) 
 print(sys.argv[1])

 print("Welcome to the greeter program")
 name = input("Enter your name: ")
 print("Greetings " + name)

 print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
 print(first_number + second_number)
print(int(first_number) + int(second_number))

# Creación de un entorno virtual

 python -m venv env
 /env
   /include
   /lib
   /Scripts
 /env
 /src
   program.py

# Active el entorno virtual

 C:\ .. \env\Scripts\activate
 (env) -> path/to/project
 pip install python-dateutil
 /env
   /lib
     /dateutil
path/to/project

# Cadenas

 Cadena simple

fact = "The Moon has no atmosphere."
print(fact)

Inmutabilidad de cadenas

fact = "The Moon has no atmosphere."
fact = "No sound can be heard on the Moon."

fact = "The Moon has no atmosphere."
fact = 'No sound can be heard on the Moon.'
print(fact)

fact = "The Moon has no atmosphere."
two_facts = fact + "No sound can be heard on the Moon."
print(two_facts)

# Acerca del uso de comillas 

moon_radius = "The Moon has a radius of 1,080 miles."

'The "near side" is the part of the Moon that faces the Earth.'

"We only see about 60% of the Moon's surface."

 'We only see about 60% of the Moon's surface.'
   File "<stdin>", line 1
     'We only see about 60% of the Moon's surface.'
                                        ^
 SyntaxError: invalid syntax

"""We only see about 60% of the Moon's surface, this is known as the "near side"."""

# Texto multilínea

multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

multiline = """Facts about the Moon: There is no atmosphere. There is no sound."""
print(multiline)

# Métodos de cadena en Python

print("temperatures and facts about the moon".title())

heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)

# División de una cadena

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures .split()
print(temperatures_list)

temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures .split('\n')
print(temperatures_list)

# Búsqueda de una cadena

print("Moon" in "This text will describe facts and challenges with space travel")

print("Moon" in "This text will describe facts about the Moon")

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))

print("The Moon And The Earth".lower())

print("The Moon And The Earth".upper())

# Comprobación del contenido

temperatures = "Mars Average Temperature: -60 C"

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
print("-60".startswith('-'))

if "30 C".endswith("C"):
 print("This temperature is in Celsius")

# Transformar texto

print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))

# Fechas

from datetime import date
date.today()
print(date.today())

# Conversión de tipos de datos

print("Today's date is: ", date.today())

print("Today's date is: " + date.today())

print("Today's date is: " + str(date.today()))

# Hola
print('hola mundo')

# Operadores

#<left side> <operator> <right side>
left_side = 10
right_side = 5

# Operadores aritméticos

suma = 1 + 1

resta = 1 - 2

division = 10 / 2

multiplicación = 2 * 2 

# Operadores de asignación

x = 2 # x ahora contiene 2

x += 2 # 2 incrementa a 4

x -= 2 # 2 disminuye de 2 a 0

x /= 2 # 2 dividido de 2 es 1

x *= 2 # 2 multiplicado de 2 es 4

# Programa

 program.py

sum = 1 + 2
print(sum)

print('show this in the console')

# Tipos de datos

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string
distance_to_alpha_centauri = 4.367 # looks like a float
type(distance_to_alpha_centauri) ## <class 'float'>

# Uso de if, else y elif
Uso de if
a = 97
b = 100
 test expression
if a < b:
    # statement to be run
    print(b)

# Escritura de instrucciones if

 if test_expression
 statement(s) to be run
a = 93
b = 27
if a >= b:
    print(a)

a = 24
b = 44
if a <= 0:
    print(a)
print(b)

Uso de else

a = 27
b = 93
if a >= b:
    print(a)
else:
    print(b)

 if test_expression:
    # statement(s) to be run
 else:
    # statement(s) to be run

 Uso de elif
 
a = 27
b = 93
if a <= b:
    print("a is less than or equal to b")
elif a == b:
    print("a is equal to b")

 if test_expression:
     # statement(s) to be run
 elif test_expression:
     # statement(s) to be run

# Combinación de instrucciones if, elif y else 

a = 27
b = 93
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else: 
    print ("a is equal to b")

 if test_expression:
     # statement(s) to be run
 elif test_expression:
     # statement(s) to be run
 elif test_expression:
     # statement(s) to be run
 else:
     # statement(s) to be run

# Uso de lógica condicional añadida 

a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")

 if test_expression:
     # statement(s) to be run
     if test_expression:
         # statement(s) to be run
     else: 
         # statement(s) to be run
 elif test_expression:
     # statement(s) to be run
     if test_expression:
         # statement(s) to be run
     else: 
         # statement(s) to be run
 else:
     # statement(s) to be run

# Operadores booleanos 

 Operador or

a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

 Operador and

a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)

 Diferencia entre and y or 

 Tabla de verdad para and 

 subexpression1         Operador                 subexpression2        Resultado
 True                    and                       True                   True
 True                    and                       False                  False
 False                   and                       True                   False
 False                   and                       False                  False

 Tabla de verdad para or 

 subexpression1         Operador                 subexpression2        Resultado
 True                    or                        True                   True
 True                    or                        False                  True
 False                   or                        True                   True
 False                   or                        False                  False

# Variables

sum = 1 + 2 # 3
product = sum * 2
print(product)
