import sys

def convertir_a_decimal(numero):
    def recursivo(num, i): #Utilice el wwrapper para iniciar i en 0 y no poder mandarlo por parametro.
        if num <= 0:
            return 0
        return (num % 10) * pow(2, i) + recursivo(num // 10, i + 1) #A lo Majid.
    return recursivo(numero, 0) 


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Uso correcto: python Ejercicio1.py numeroBinario')
    else:
        numero = int(sys.argv[1])
        print(convertir_a_decimal(numero))



   
