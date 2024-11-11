#Inicialize uma lista de 20 números inteiros. Armazene
os números pares em uma lista PAR e os números
ímpares em uma lista IMPAR. Imprima as listas PAR
e IMPAR.

# Inicializando uma lista com 20 números inteiros
numeros = [10, 23, 34, 45, 56, 67, 78, 89, 90, 21, 32, 43, 54, 65, 76, 87, 98, 19, 30, 41]

# Listas para armazenar os números pares e ímpares
par = []
impar = []

# Separando os números pares e ímpares
for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

# Imprimindo as listas
print("Lista de números pares:", par)
print("Lista de números ímpares:", impar)



