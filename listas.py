import os

class Mascota:
    def __init__(self,nombre,raza,edad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        pass
    def __repr__(self) -> str:
        return "MASCOTA: " + self.nombre + "|Raza: "+ self.raza + "|Edad:" + str(self.edad)
        pass
    pass

class Nodo:
    def __init__(self,nombre,raza,edad) -> None:
        #Asignar valores
        self.mascota = Mascota(nombre, raza, edad)
        self.siguiente = None
        pass
    pass

def agregaMascota():
    print("Cual es el nombre de tu mascota: ")
    nombre = input()
    print("Cual es la raza de tu mascota: ")
    raza = input()
    print("Cual es la edad de tu mascota: ")
    edad = int(input())
    return Nodo(nombre,raza,edad)
    pass

def agregaNodo(lista,nodo):
    if lista.__len__() == 0:
        print("Lista Vacia \n")
        lista = nodo
    else:
        for elemento in lista:
            if elemento.siguiente != None:
                elemento.siguiente = nodo
        pass
    pass

def imprimeLista(lista):
    if lista.__len__() == 0:
        print("Lista Vacia")
        print("[ ]")
    else:
        for elemento in lista:
            print(elemento," \n")
    pass


def menu():
    # Menu principal
    menuTxt = "------------ Lista de Mascotas ------------------- \n"
    menuTxt+="1) Agregar Mascotas \n"
    menuTxt+="2) Eliminar Mascotas \n"
    menuTxt+="3) Ver Lista de Mascotas \n"
    menuTxt+="4) Salir \n"
    menuTxt+="Elije la opcion deseada: \n"
    opcion = "Inicial1"
    listaM = []
    while opcion != '4':
        print(menuTxt)
        opcion = input()
        if opcion == '1':
            print("Has elegido la opcion de agregar: \n")
            mascotaN = agregaMascota()
            agregaNodo(listaM,mascotaN)
        if opcion == '2':
            print("Has elegido la opcion de Eliminar: \n")
        if opcion == '3':
            print("Has elegido la opcion de Ver: \n")
            imprimeLista(listaM)
        if opcion == '4':
            print("Has elegido la opcion de Salir: \n")
            os._exit(4)
    pass

if __name__ == "__main__":
    menu()

