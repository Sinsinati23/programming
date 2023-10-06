# Cadena simple
fact = "The Moon has no atmosphere."
print(fact)

# Inmutabilidad de cadenas
fact = "The Moon has no atmosphere."
fact = "No sound can be heard on the Moon."

fact = "The Moon has no atmosphere."
fact = 'No sound can be heard on the Moon.'
print(fact)

fact = "The Moon has no atmosphere."
two_facts = fact + "No sound can be heard on the Moon."
print(two_facts)

#Acerca del uso de comillas 
moon_radius = "The Moon has a radius of 1,080 miles."

'The "near side" is the part of the Moon that faces the Earth.'

"We only see about 60% of the Moon's surface."

# 'We only see about 60% of the Moon's surface.'
#   File "<stdin>", line 1
#     'We only see about 60% of the Moon's surface.'
#                                        ^
# SyntaxError: invalid syntax

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