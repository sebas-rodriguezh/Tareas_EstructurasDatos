import time

def getFile():
    with open("large_text.txt", "w") as f:
        for _ in range(222630):  # ~10MB total
            f.write("The quick brown fox jumps over the lazy dog.\n")
    return open("large_text.txt","r") #Lo retorno abierto y de una vez que sea 'r' para read.


def leerCharPorChar():
    f = getFile()
    inicio = time.time()
    while True:
        caracter = f.read(1) #Lea de uno en uno.
        if not caracter: #Estoy vacio (Termine)
            break #Cuando llegue al fin, salga del ciclo.
    final = time.time()
    print(f"Tiempo transcurrido caracter por caracter: {final-inicio}")

leerCharPorChar()

#Ver respuesta preguntar en Funcion_3.py
