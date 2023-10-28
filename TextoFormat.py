# Este programa define una función prin, que recibe un string como argumento e imprime por pantalla texto formateado

text = input("Introduce texto: ") # Pedimos al usuario que introduzca texto

def textoFormat(text): # Definimos la función, imprime el texto entre barras
  print("======")
  print(text)
  print("======")

textoFormat(text) # Imprime el resultado de la función
