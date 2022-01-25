# Este es un comentario en una linea
'''
Este es un comentario multilinea
Es decir se escriben varias lineas
'''
class Persona:
    def __init__(self,nombre,edad,lista) -> None:
        self.nombre = nombre
        self.edad = edad
        self.lista = lista
        pass

    def __repr__(self) -> str:
        return "nombre: " + self.nombre + " - edad: "+ str(self.edad)+ " - lista: " + str(self.lista)
        pass

    def funcion(self):
        
        pass
    pass



# Datos primitivos
a = 1
print(a," - ",type(a))
a = "Hola Mundo"
print(a," - ",type(a))
a = 1.5
print(a," - ",type(a))
a = True
print(a," - ",type(a))
# Datos compuestos
a =[1, 2, 3, 4]
print(a," - ",type(a))
a = (1, 2, 3, 4)
print(a," - ",type(a))
a = [1 , 2, 3, 4 ,['a','b','c','d']]
print(a," - ",type(a))
a1 = {'nombre':'Josue','edad':45, 'lista':a}
print(a1," - ",type(a1))
# Datos Abstractos
a = Persona('Josue',45,a)
print(a," - ",type(a))