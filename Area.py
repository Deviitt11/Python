# Cálculo del area de un rectángulo

# El programa pide al usuario que introduzca el ancho y largo de dicho rectángulo

# Con la función area, que toma el ancho y largo como argumentos, se calcula y devuelve el area

# Defino la función area (ancho y largo como argumentos)
def area(x, y):
	# Devuelve el área
	return(x*y)
   
# Le pedimos al usuario que introduzca tanto el ancho como el largo
w = int(input("Introduce el ancho: "))
h = int(input("Introduce el largo: "))

# Llamada a la función que devuelve el área
print(area(w,h))