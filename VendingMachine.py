products = ["Water", "Chocolate", "Chips", "Soda", "Sandwich"]
choice_index = int(input())

# Write a try-except block to display the selected product
# or print "wrong index" if the input index is out of range

try: # la acción que intento hacer
    print(products[choice_index])
except IndexError: # si el índice fuera de rango, imprimo error
    print("wrong index")