import time

def getFile():
    with open("large_text.txt", "w") as f:
        for _ in range(222630):  # ~10MB total
            f.write("The quick brown fox jumps over the lazy dog.\n")
    return open("large_text.txt","rb") #Lo retorno abierto y de una vez que sea 'rb' para read binary OJO. Para que las lecturas sean de bytes exactos.


def leerPorBloquesDeBytes(bloque = 4096):
    f = getFile()
    inicio = time.time()
    while True:
        bloqueLeido = f.read(bloque)
        if not bloqueLeido: #Si ya NO es bloque y no se pudo leer.
            break
    final = time.time()
    print(f"Tiempo transcurrido por bloque de bytes: {final-inicio}")


leerPorBloquesDeBytes()

'''
R1:

Me sorprenden los resultados, ya que pensaba que la lectura de caracter por caracter
podria tomar más tiempo, sin embargo, aunque sean muchos caracteres, el tiempo entra 
dentro de un rango razonable, sin embargo, con respecto a los otros dos metodos. Los 
resultados me llaman la atención ya que son tiempos que no superan los 0.0x. En algunos casos
optimos. 

R2:

La razón por la que esto ocurre es la siguiente, en la F1, el sistema debe de llamar
una vez por cada caracter, generando llamadas de entrada y salida, el sistema debe de entrar
y salir por cada byte. Generando muchas llamadas en el archivo. 

La funcion linea por linea, tiene menos llamadas, ya que una linea es un conjunto de caracteres.
Haciendo en una iteracion lo que la F1 hacia en x caracteres, por eso es un poco más lenta que la F2. 
Ahora, las lineas pueden ser de diferentes logitudes e igual debe ir linea por linea leyendo, lo que lo hace
un poco lenta para bloques en donde hayan demasiadas lineas por leer. 

Con respecto a la F3, lee bloques por tamaño, en cada operación se lee mucho más que en las dos anteriores. 
Ya que no es lo mismo leer una linea, o un caracter, que leer un bloque de 4KB que contiene bastantes lineas en el ese bloque
lo que hace este función la más rapida. Su procesamiento es mucho más eficiente. 

'''