
import pickle

def guardar_lista(lista, filename = "planillaCSH.dat"):
    with open(filename, "wb") as file:
        pickle.dump(lista, file)
    print("Lista guardada con exito.")


def recuperar_datos(filename = "planillaCSH.dat"):
    try:
        with open(filename, "rb") as file:
            lista = pickle.load(file) #Cargar los datos binarios de file.
            return lista
    except FileNotFoundError:
        print("No se encontro ningun archivo.")
        return []


def mostrarJugadores(lista):
    for jugador in lista:
        print(f"Nombre del jugador: {jugador['Nombre']}, Dorsal: {jugador['Dorsal']}, Posicion: {jugador['Posicion']}")

def mostrarJugadorPorDorsal(lista, dorsal):
    for jugador in lista: #Por cada jugador en la lista, haga:
        if jugador['Dorsal'] == dorsal: #Es como decir -> if vec[i].getDorsal() == dorsal. Ese vec[i] seria el jugador.
            print(f"Jugador con el dorsal {dorsal}: {jugador['Nombre']}")
            break
    else: #Este else es del for y se ejecuta solo si NO hubo break en el ciclo, útil para detectar que no se encontró algo durante la iteración.
        print(f"No hay jugador con el dorsal {dorsal}.")

if __name__ == "__main__":

    biblioteca_CSH = [
        {"Nombre": "Elias Aguilar", "Dorsal": 10, "Posicion": "MC"},  # B1
        {"Nombre": "Marcel Hernandez", "Dorsal": 9, "Posicion": "DC"},  # B2
        {"Nombre": "Allan Cruz", "Dorsal": 8, "Posicion": "MC"},  # B3
        {"Nombre": "Keyner Brown", "Dorsal": 99, "Posicion": "DFC"},  # B4
    ]

    guardar_lista(biblioteca_CSH)
    listaRecuperada = recuperar_datos()
    print("Lista Recuperada del CSH:")
    print(" ")

    mostrarJugadores(listaRecuperada)
    print(" ")
    print(listaRecuperada)
    mostrarJugadorPorDorsal(listaRecuperada, 99)












