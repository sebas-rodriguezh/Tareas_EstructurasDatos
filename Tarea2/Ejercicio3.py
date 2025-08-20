import json

class Node:
    def __init__(self, value):
        self.obj = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def mostrarTodo(self):
        current = self.head
        while current:
            print(current.obj.mostrar())
            current = current.next 

    def insertarAlFinal(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        
        if value.tipo == "VIP":
            current = self.head
            if (current.obj.tipo != "VIP"):
                new_node.next = self.head
                self.head = new_node
                return
            while (current.next and current.next.obj.tipo == "VIP"):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        elif value.tipo == "NORM":
            current = self.head
            while (current.next and current.next.obj.tipo != "BULK"):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        else: 
            self.insertarAlFinal(value)
            return  
        
    def atender(self):
        if self.head is None:
            return None
        value = self.head.obj
        self.head = self.head.next
        return value


class Cliente:
    def __init__(self, tipo, nombre):
        self.tipo = tipo 
        self.nombre = nombre
    
    def mostrar(self):
        return {
            "tipo": self.tipo,
            "nombre": self.nombre
        }
    
    def mostrarSimple(self):
        return f"{self.tipo} - {self.nombre}"


def leerClientesJson(filename):
    listaClientes = SinglyLinkedList()
    try:
        with open(filename, 'r') as file:
            clientesCargados = json.load(file)
            for clientejson in clientesCargados:
                clienteRecuperado = Cliente(clientejson["tipo"], clientejson["nombre"]) #Lo creamos como Cliente recuperando del diccionario json.
                listaClientes.insert(clienteRecuperado) #Acá es donde le hace el toque del insert por priordad.
    except FileNotFoundError:
        print(f"El archivo {filename} no existe.")
    return listaClientes
    

if __name__ == "__main__":
    nombre_archivo = "comedor.json"  
    
    lista = leerClientesJson(nombre_archivo)
    lista.mostrarTodo()

    