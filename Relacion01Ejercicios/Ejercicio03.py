# Escribe un programa que muestre por pantalla los n�meros m�ltiplos de 7 entre el
# 1 y el 1000.

for i in range(1, 1001):
	if(i %7 == 0):
		print(i)