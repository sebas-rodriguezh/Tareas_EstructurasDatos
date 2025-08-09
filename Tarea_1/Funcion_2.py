import time

def getFile():
    with open("large_text.txt", "w") as f:
        for _ in range(222630):  # ~10MB total
            f.write("The quick brown fox jumps over the lazy dog.\n")
    return open("large_text.txt","r") #Lo retorno abierto y de una vez que sea 'r' para read.


def leerLineaPorLinea():
    f = getFile()
    inicio = time.time()
    for line in f:
        pass #Como no quiero hacer nada, entonces solo lea cada linea en f y pase.
    final = time.time()
    print(f"Tiempo transcurrido linea por linea: {final-inicio}")

leerLineaPorLinea()

# def leerLineaPorLineaV2():
#     f = getFile()
#     inicio = time.time()
#     while True:
#         line = f.readline() #Lea la linea.
#         if not line:
#             break
#     final = time.time()
#     print(f"Tiempo transcurrido: {final-inicio}")
