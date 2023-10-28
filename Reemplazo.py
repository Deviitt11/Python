# Este programa recibe un texto y reemplaza los símbolos de # incluidos en el texto por espacios (' ')
#
msg = input("Introduce un texto con #: ") # Pedimos al usuario que introduzca el texto con dichas condiciones

msg = msg.replace('#', ' ') # La función se encarga de realizar el reemplazo

print(msg)