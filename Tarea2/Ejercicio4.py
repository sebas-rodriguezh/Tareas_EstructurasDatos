#Al ser diccionarios, puedo aprovecharme de los valores key-value de los diccionarios.
import json

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  

class Stack:
    def __init__(self):
        self.top = None 

    def push(self, value): 
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self): 
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value
    
    def is_empty(self):
        return self.top is None

    def peek(self): 
        return None if self.top is None else self.top.value

    def display(self):
        current = self.top
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def popInvertido (self, filename): 
        with open(filename, 'r') as file:
            instrucciones = json.load(file)
            if not instrucciones:
                print("Lista de instrucciones vacía.")
                return None
        
        stackOrdenes = Stack()

        for instruccion in instrucciones: #Como todas las instrucciones tienen cmd. 
            if instruccion["cmd"] == "MOVE":
                stackOrdenes.push(f"MOVE_BACK x {instruccion['x']}") 
            elif instruccion["cmd"] == "TURN_LEFT":
                stackOrdenes.push("TURN_RIGHT") 
            elif instruccion["cmd"] == "TURN_RIGHT":
                stackOrdenes.push("TURN_LEFT")
            elif instruccion["cmd"] == "DROP":
                continue 
            elif instruccion["cmd"] == "RETURN":
                while not stackOrdenes.is_empty():
                    instruccionInvertida = stackOrdenes.pop() 
                    print(instruccionInvertida) 
                break


if __name__ == "__main__":
    archivoInstrucciones = "dron.json"
    s = Stack()
    s.popInvertido(archivoInstrucciones)
    