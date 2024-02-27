## OPERADORES Y ESTRUCTUTRAS DE CONTROL ##

'''
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan en tu lenguaje:
Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos
'''

# 1 Operadores aritmeticos, logicos, de comparación, asignación, identidad, pertenencia y bits.
# Aritméticos
a, b, c = 5, 10, 2
x =  a + b - c
y =  a * (b / c) ** b
# Comparación
z = x < y     
z != x
# Lógicos
4>3 and "Hybrid"<"Host"  # Devuelve False
5>2 or 2<5               # Devuelve True
not z                    # Devuelve False
# Asignación
w = x             # Asignar el valor de x a w
w += 3             # Sumarle 3 al nuevo valor de w
w *= 2             # Multiplicar por 2 el nuevo valor de w
# Identidad
a = [1, 4, 8, 10]
b = [1, 4, 8, 10]
c = a
print(b is a)
print(b == a)  
print(a is c)
print(c is not a)    
print(b == c) 
# Pertenencia 
print("a")
a = [1, 4, 8, 10]
if 1 in a:
    print(True)
else:
    print(False)
if 4 is not a:
    print(True)
else:
    print(False)
# Bits
a = 60  # en binario: 111100
b = 13  # en binario: 00001101
# AND bit a bit
c = a & b  # en binario: 00000000, en decimal: 0
print(f"a & b = {c}")
# OR bit a bit
c = a | b  # en binario: 11111101, en decimal: 251
print(f"a | b = {c}")
# XOR bit a bit
c = a ^ b  # en binario: 11111100, en decimal: 252
print(f"a ^ b = {c}")
# NOT bit a bit
c = ~a  # en binario: -61, en decimal: -61
print(f"~a = {c}")
# Desplazamiento a la izquierda
c = a << 2  # en binario: 11110000, en decimal: 240
print(f"a << 2 = {c}")
# Desplazamiento a la derecha
c = a >> 2  # en binario: 00111100, en decimal: 15
print(f"a >> 2 = {c}")

