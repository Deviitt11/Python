# Este programa recibe dos años como entrada e imprime el rango de años entre dichos números

# La secuencia de salida comienza con el primer número introducido por teclado y finaliza en el segundo año introducido, sin incluirlo.

a = int(input("Introduce un año: ")) # Pedimos al usuario que introduzca un año
b = int(input("Introduce otro año: ")) # Pedimos que introduzca otro

nums = list(range(a,b));
print(nums);