import sys

def invertir_numero(n, inverso = 0):
    if n == 0:
        return inverso
    else:
        return invertir_numero(n // 10, inverso * 10 + n % 10)
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Uso correcto: python Ejercicio4.py numeroAInvertir')
    else:
        numero = int(sys.argv[1])
        print(invertir_numero(numero))
