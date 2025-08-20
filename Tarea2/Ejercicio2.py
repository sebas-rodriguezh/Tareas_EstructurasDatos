import json

class Node:
    def __init__(self, value):
        self.obj = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        listaNativa = []
        current = self.head
        while current:
            listaNativa.append(current.obj)
            current = current.next
        return listaNativa #Retorno una lista nativa de Python.

class Evento:
    def __init__(self, inicio, duracion, sala):
        self.inicio = inicio
        self.duracion = int(duracion)
        self.sala = sala

    def mostrar(self):
        return {
            "inicio": self.inicio,
            "duracion": self.duracion,
            "sala": self.sala
        }

    def inicio_en_minutos(self):
        h, m = map(int, self.inicio.split(':'))
        return h * 60 + m #Lo que hice fue convertir la hora en minutos. Enteros, para poder hacer cálculos.

    def fin_en_minutos(self):
        return self.inicio_en_minutos() + self.duracion #Hora de inicio + duración = hora de fin.

def filtrarLista(listaEventos):
    current = listaEventos.head
    while current and current.next:
        actual = current.obj        
        siguiente = current.next.obj   

        if actual.sala == siguiente.sala and siguiente.inicio_en_minutos() == actual.fin_en_minutos():
            actual.duracion += siguiente.duracion #Unifico en actual lo del siguiente. Mantengo la hora de inicio.
            current.next = current.next.next
        else:
            current = current.next

def leer_eventos(filename):
    listaEventos = SinglyLinkedList()
    try:
        with open(filename, 'r') as file:
            eventosCargados = json.load(file)
            for eventosjson in eventosCargados:
                evento = Evento(eventosjson['inicio'], eventosjson['duracion'], eventosjson['sala']) #Es como un casteo para tener un objeto Evento.
                listaEventos.insert(evento)
    except FileNotFoundError:
        print(f"El archivo {filename} no existe.")
    return listaEventos

if __name__ == "__main__":
    nombre_archivo = "eventos.json"  
    
    listaLoca = leer_eventos(nombre_archivo)
    print("Antes de unificar:")
    for e in listaLoca.to_list(): #Este es para hacer que mi lista sea iterable.
        print(e.mostrar())

    filtrarLista(listaLoca)

    print(" ")
    print("Despues de unificar:")
    for e in listaLoca.to_list():
        print(e.mostrar())