import sys

def division(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    if a < b:
        return 0
    if a == b:
        return 1
    return 1 + division(a - b, b)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Uso correcto: python Ejercicio3.py a b')
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print(division(a,b))

