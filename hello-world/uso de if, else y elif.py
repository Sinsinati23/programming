# Uso de if
a = 97
b = 100
# test expression
if a < b:
    # statement to be run
    print(b)

# Escritura de instrucciones if

# if test_expression
# statement(s) to be run
a = 93
b = 27
if a >= b:
    print(a)

a = 24
b = 44
if a <= 0:
    print(a)
print(b)

# Uso de else
a = 27
b = 93
if a >= b:
    print(a)
else:
    print(b)

# if test_expression:
    # statement(s) to be run
# else:
    # statement(s) to be run

# Uso de elif
a = 27
b = 93
if a <= b:
    print("a is less than or equal to b")
elif a == b:
    print("a is equal to b")

# if test_expression:
#     # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run

#Combinación de instrucciones if, elif y else 
a = 27
b = 93
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else: 
    print ("a is equal to b")

# if test_expression:
#     # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run
# else:
#     # statement(s) to be run

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

# if test_expression:
#     # statement(s) to be run
#     if test_expression:
#         # statement(s) to be run
#     else: 
#         # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run
#     if test_expression:
#         # statement(s) to be run
#     else: 
#         # statement(s) to be run
# else:
#     # statement(s) to be run

# Operadores booleanos 

# Operador or

a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

# Operador and

a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)

# Diferencia entre and y or 

# Tabla de verdad para and 

# subexpression1        # Operador                # subexpression2       # Resultado
# True                    and                       True                   True
# True                    and                       False                  False
# False                   and                       True                   False
# False                   and                       False                  False

# Tabla de verdad para or 

# subexpression1        # Operador                # subexpression2       # Resultado
# True                    or                        True                   True
# True                    or                        False                  True
# False                   or                        True                   True
# False                   or                        False                  False
