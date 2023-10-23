# Este programa recibe un texto y una palabra como entrada y los pasa a una función llamada search()

# Dicha función debe devolver "Palabra encontrada" si la palabra está presente en el texto, o "Palabra NO encontrada" si no lo está.

text = input(("Introduce texto: "))
word = input(("Introduce una palabra: "))

def search(text, word):
    if(word in text):
        print("Palabra encontrada")
    else:
        print("Palabra NO encontrada")
    
search(text, word)