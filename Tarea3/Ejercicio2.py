import sys

def convertir_a_binario(numero):
    if numero < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    if numero <= 1:
        return numero
    return convertir_a_binario(numero // 2) * 10 + (numero % 2)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Uso correcto: python Ejercicio2.py numeroDecimal')
    else:
        numero = int(sys.argv[1])
        print(convertir_a_binario(numero))
