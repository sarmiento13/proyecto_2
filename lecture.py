# ejercisios de operadores lógicos 
 
# Ejercicio 1: Verificar si un número está entre 10 y 20 (inclusive) o si es igual a 0

numero = int(input("Ingrese un número: "))

if (numero >= 10 and numero <= 20) or numero == 0:
    print("El número está entre 10 y 20 o es igual a 0")
else:
    print("El número no cumple las condiciones")
 

# Ejercicio 2: Imprimir los números pares entre 1 y 10 utilizando un bucle while

numero = 1
while numero <= 10:
    if numero % 2 == 0:
        print(numero)
    numero += 1
 
# Ejercicio 3: Verificar si una lista contiene al menos un número par y un número impar

lista = [1, 2, 3, 4, 5]

hay_par = False
hay_impar = False

for numero in lista:
    if numero % 2 == 0:
        hay_par = True
    else:
        hay_impar = True

if hay_par and hay_impar:
    print("La lista contiene al menos un número par y un número impar")
else:
    print("La lista no cumple las condiciones")
 
 
