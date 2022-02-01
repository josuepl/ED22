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

def menu():
    # Menu principal
    menuTxt = "------------ Lista de Mascotas ------------------- \n"
    menuTxt+="1) Agregar Mascotas \n"
    menuTxt+="2) Eliminar Mascotas \n"
    menuTxt+="3) Ver Lista de Mascotas \n"
    menuTxt+="4) Salir \n"
    menuTxt+="Elije la opcion deseada: \n"
    print(menuTxt)
    opcion = input()
    if opcion == '1':
        print("Has elegido la opcion de agregar: \n")
    if opcion == '2':
        print("Has elegido la opcion de Eliminar: \n")
    if opcion == '3':
        print("Has elegido la opcion de Ver: \n")
    if opcion == '4':
        print("Has elegido la opcion de Salir: \n")
        os._exit(4)
    pass

if __name__ == "__main__":
    menu()

