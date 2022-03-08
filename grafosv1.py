def imprime(grafo,nNodos):
    if nNodos == 0:
        print("El grafo esta vacio \n")
        return None
    aux = []
    for i in range(nNodos):
        aux.append(grafo[i][0])
    print("----",aux)
    for i in range(nNodos):
        print(grafo[i])
    pass

def buscaNodo(grafo,nodo,nNodos):
    if grafo.__len__() == 0:
        return None
    for i in range(nNodos):
        if (grafo[i][0] == nodo):
            return i
    return None

def existeArista(grafo,nodoI,nodoF):
    if(grafo[nodoI][nodoF] == 1):
        return True
    else: 
        return False
    pass

def creaArista(grafo,nodoI, nodoF,resp):
    if resp == '2':
        grafo[nodoF -1][nodoI + 1] = 1
    grafo[nodoI][nodoF] = 1
    pass
def menu():
    nNodos = 0
    opcion = None
    grafo =[]
    txtMenu = 'PROGRAMA DE GRAFOS ESTATICO \n'
    txtMenu += "1. Crear Nodos \n"
    txtMenu += "2. Crear Aristas \n"
    txtMenu += "3. Ver Grafo \n"
    txtMenu += "4. Salir \n"

    while opcion != 4:
        print(txtMenu)
        opcion = input("Ingresa la opción deseada: \n")
        if opcion == '1':
            nNodos = int(input("Cuantos nodos tiene el grafo:"))
            i = 0
            for i in range(0,nNodos):
                aux = [None] * (nNodos+1)
                nuevo = None
                while nuevo == None:
                    nombre = input("Ingrese el nombre del Nodo: ")
                    nuevo = buscaNodo(grafo,nombre,i)
                    if nuevo == None:
                        nuevo = aux[0] = nombre
                    else:
                        print("El nombre ya existe... \n")
                        nuevo = None
                grafo.append(aux)
            imprime(grafo,nNodos)
        if opcion == '2':
            nodoF = nodoI = None
            resp = input("La arista es dirigida(1.SI / 2. NO)")
            while nodoI == None:
                origen = input("Ingresa el nombre del nodo Origen: ")
                nodoI = buscaNodo(grafo, origen,nNodos) 
            print(nodoI)
            while nodoF == None:
                destino = input("Ingresa el nombre del nodo Destino: ")
                nodoF = buscaNodo(grafo, destino, nNodos) + 1
            print(nodoF)
            bandAris = existeArista(grafo,nodoI, nodoF)
            if bandAris:
                print("La Arista ya existe","\n No se creo la arista")
            else:
                creaArista(grafo,nodoI,nodoF,resp)
            
            pass
        if opcion == '3':
            imprime(grafo,nNodos)
    pass


if __name__ == "__main__":
    menu()