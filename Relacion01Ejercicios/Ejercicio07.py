#Queremos hacer un programa que calcule el factorial de un número entero positivo.

n = int(input("Escribe un entero:"))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)