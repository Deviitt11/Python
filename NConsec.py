# Este programa toma un número (n) como entrada e imprime por pantalla la suma de todos los números desde 1 hasta N (N incluido)

n = int(input("Introduce un número: ")) # Pedimos al usuario que introduzca un número

suma = 0 # Creamos una variable para almacenar la suma y la inicializamos a 0

for x in range(1, n+1): # Bucle for para realizar la suma, n+1 para que incluya n
    suma += x

print(suma) # Imprime la suma