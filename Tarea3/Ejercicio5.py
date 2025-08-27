import sys

def aparicion_caracter(cadena, caracter):
    if len(cadena) == 0:
        return 0
    else:
        if cadena[0] == caracter:
            return 1 + aparicion_caracter(cadena[1:], caracter) #Me genera una subcadena. 
        else:
            return aparicion_caracter(cadena[1:], caracter)

    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Uso correcto: python Ejercicio5.py "Cadena" "Caracter"')
    else:
        cadena = sys.argv[1]
        caracter = sys.argv[2]
        print(aparicion_caracter(cadena, caracter))
