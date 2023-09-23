#Nombres: Ernesto Starck Y Sebastian Bustamante#
#Fecha: 19/09/2023
#Asignatura: Seguridad Informatica


import hashlib
from cryptography.fernet import Fernet

#ROT 21#
with open('mensajedeentrada.txt') as archivo_entrada:
    mensaje = archivo_entrada.read()

# Saco el modulo de la cantidad de letras del abecedario 
def custom_abs(x):
    if x >= 0:
        return x % 26
    return 26 + x

# Giro la letra segun el parametro n
def rot(r, n):
    if 'a' <= r <= 'z':
        return chr(custom_abs(ord(r) + n - ord('a')) + ord('a'))
    if 'A' <= r <= 'Z':
        return chr(custom_abs(ord(r) + n - ord('A')) + ord('A'))
    return r

# Creo un string con el mensaje completo rotado n veces
def Rot(string, n):
    str_new = ""
    for char in string:
        str_new += rot(char, n)
    return str_new

# Obtengo el texto cifrado
texto_original = mensaje
texto_rotado = Rot(texto_original, 21)
print("El texto claro es:", mensaje)
print("El texto cifrado es:", texto_rotado)

# Guardar el texto cifrado en un archivo de texto
with open('mensajeseguro.txt', 'w') as archivo_salida:
    archivo_salida.write(texto_rotado)
    
#====================================================================
#====================================================================

#ROT -21#
with open('mensajeseguro.txt') as archivo_entrada:
    mensajecifrado = archivo_entrada.read()
    
# Saco el modulo de la cantidad de letras del abecedario  
def custom_abs(x):
    if x >= 0:
        return x % 26
    return 26 + x

# Giro la letra segun el parametro n
def rot(r, n):
    if 'a' <= r <= 'z':
        return chr(custom_abs(ord(r) + n - ord('a')) + ord('a'))
    if 'A' <= r <= 'Z':
        return chr(custom_abs(ord(r) + n - ord('A')) + ord('A'))
    return r
# Se crea un string con el mensaje completo rotado n veces 
def Rot(string, n):
    str_new = ""
    for char in string:
        str_new += rot(char, n)
    return str_new

# Obtengo el texto descifrado
textodescifrado = Rot(mensajecifrado, -21)
print("El texto descifrado es :",textodescifrado)


# Guardar el texto descifrado en un archivo de texto
with open('mensajeseguro.txt', 'w') as archivo_salida:
    archivo_salida.write(textodescifrado)


#====================================================================
#====================================================================


#HASH MENSAJE ORIGINAL

# Leer el mensaje de entrada desde el archivo
with open('mensajedeentrada.txt', 'rb') as archivo_entrada:
    MensajeEntrada = archivo_entrada.read()

# Calcular el hash del mensaje original
HashEntrada = hashlib.sha256(MensajeEntrada).hexdigest()

# El hash del texto original
HashEnt = HashEntrada.encode()
print("El Hash del mensaje original es :\n",HashEntrada.encode())


#===============================================================================
#===============================================================================


#HASH MENSAJE CIFRADO Y DESCIFRADO
    
# Leer el mensaje de entrada desde el archivo
with open('mensajeseguro.txt', 'rb') as archivo_entrada:
    MensajeDescifrado = archivo_entrada.read()

# Calcular el hash del mensaje descifrado
HashDescifrado = hashlib.sha256(MensajeDescifrado).hexdigest()

# El hash del texto descifrado
HashDes = HashDescifrado.encode()
print("El Hash del mensaje descifrado es :\n",HashDescifrado.encode())

# Se crea el comparador de ambos hash para verificar si son identicos o no
if HashDes == HashEnt:
    print("El mensaje cifrado no a sido adulterado :)")
    
else: print("El mensaje a sido adulterado :(")
