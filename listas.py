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

    def __repr__(self) -> str:
        return "MASCOTA: " + self.mascota.nombre + "|Raza: "+ self.mascota.raza + "|Edad:" + str(self.mascota.edad)
        pass

def validarNombre(listaM,nombre):
    aux = listaM
    while aux != None:
        if aux.mascota.nombre == nombre:
            print(" !---- NOMBRE REPETIDO -----!\n")
            return False
        aux = aux.siguiente
    return True
    pass

def agregaMascota(listaM):
    repetido = False
    while repetido != True:
        print("Cual es el nombre de tu mascota: ")
        nombre = input()
        repetido = validarNombre(listaM,nombre)

    print("Cual es la raza de tu mascota: ")
    raza = input()
    print("Cual es la edad de tu mascota: ")
    edad = int(input())
    return Nodo(nombre,raza,edad)
    pass

def agregaNodo(lista,nodo):
    if lista == None:
        print("Lista Vacia \n")
        lista = nodo
    else:
        aux = lista
        print('Agrega Nodo Recorrido')
        while aux != None:
            print(aux)
            aux = aux.siguiente
            pass
        aux = nodo
        nodo.siguiente = None
    pass

def imprimeLista(lista):
    if lista == None:
        print("Lista Vacia")
        print("[ ]")
    else:
        aux = lista
        while aux != None:
            print(aux)
            aux = aux.siguiente
    pass

def eliminaNodo(listaM):
    nombre = input("Ingresa el nombre de la mascota a eliminar: ")
    aux = listaM
    aux2 = listaM
    if listaM == None:
        print("Lista vacia, no hay elementos")
    else:
        bandera = False
        contador = 0
        while aux != None:
            if aux.mascota.nombre == nombre:
                print(" !---- MASCOTA ENCONTRADA ---!\n")
                print(aux, "contador: ",contador,aux.siguiente)
                if contador == 0:
                    listaM = None
                else:
                    aux2.siguiente = aux.siguiente
                bandera = True
            aux2 = aux
            aux = aux.siguiente
            contador += 1
        if bandera == False:
            print("MASCOTA NO ENCONTRADA ")
        return listaM
    pass

def eliminaCola(listaM):
    if listaM == None:
        print("Lista vacia, no hay elementos")
    else:
        aux = listaM
        print("Nodo eliminado: ",aux)
        listaM = aux.siguiente
        aux = None
        return listaM
    pass

def eliminaPila(listaM) ->Nodo:
    actual = listaM
    sgt = listaM
    if listaM == None:
        print("Lista Vacia, no hay elementos a eliminar")
        return listaM
    if actual.siguiente == None:
        listaM = None
        print("Nodo eliminado: ", actual)
        return listaM
    else:
        while actual.siguiente != None:
            sgt = actual
            actual = actual.siguiente
        sgt.siguiente = None
        print("Nodo Eliminado: ",actual)
        return listaM
    pass

def menu():
    # Menu principal
    menuTxt = "------------ Lista de Mascotas ------------------- \n"
    menuTxt+="1) Agregar Mascotas \n"
    menuTxt+="2) Eliminar Mascotas \n"
    menuTxt+="3) Ver Lista de Mascotas \n"
    menuTxt+="4) Atender por Cola \n"
    menuTxt+="5) Atender por Pila \n"
    menuTxt+="6) Salir \n"
    menuTxt+="Elije la opcion deseada: \n"
    opcion = "Inicial1"
    listaM = None
    while opcion != '6':
        opcion = input("Presiona Enter para avanzar")
        os.system("cls")
        print(menuTxt)
        opcion = input()
        if opcion == '1':
            print("Has elegido la opcion de agregar: \n")
            mascotaN = agregaMascota(listaM)
            if listaM == None:
                print("Lista Vacia \n")
                listaM = mascotaN
                print(listaM)
            else:
                aux = listaM
                print('Agrega Nodo Recorrido\n')
                while aux != None:
                    print(aux)
                    aux2 = aux
                    aux = aux.siguiente
                    pass
                aux2.siguiente = mascotaN
                mascotaN.siguiente = None
            pass
        if opcion == '2':
            print("Has elegido la opcion de Eliminar: \n")
            listaM = eliminaNodo(listaM)

        if opcion == '3':
            print("Has elegido la opcion de Ver: \n")
            imprimeLista(listaM)
        if opcion == '4':
            print("Has elegido atender por cola")
            listaM = eliminaCola(listaM)
        if opcion == '5':
            print("Has elegido atender por pila")
            listaM = eliminaPila(listaM)
        if opcion == '6':
            print("Has elegido la opcion de Salir: \n")
            os._exit(4)
    pass

if __name__ == "__main__":
    menu()

