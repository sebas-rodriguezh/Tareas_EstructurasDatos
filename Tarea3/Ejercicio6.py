import sys

def permutaciones_cadena (cadena):
    if len(cadena) == 1: 
        return [cadena]
    
    resultado = []
    for i in range(len(cadena)):
        letra = cadena[i]
        restante = cadena[:i] + cadena[i+1:] #Agarro, lo que está antes todo, y luego todo lo que está después. 

        for combs in permutaciones_cadena(restante):
            resultado.append(letra + combs)

    return resultado

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso correcto: python Ejercicio6.py <cadena>")
    else:
        cadena = sys.argv[1]
        print(permutaciones_cadena(cadena))

