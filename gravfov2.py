from igraph import Graph
import igraph as ig
import cairo
import matplotlib.pyplot as plt
ifg, aux = plt.subplots()

print("Hola Graph")
#Se crea un grafo vacio
g = Graph()
#Se añaden 7 vertices/nodos al grafo
g.add_vertices(7)
print(g.vs,g.es)
nombres = ['ene','feb','marzo','abril','mayo','junio','julio'] 
g.vs['nombre']= nombres
#Se crean 10 arístas dentro del grafo
g.add_edges([(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,5),(2,5),(3,4),(5,6)])
g.add_vertices(3)
nombresAux = ['agos','sept','oct']
nombres.extend(nombresAux)
g.vs['nombre']= nombres
g.add_edges([(9,8),(7,6),(8,0),(7,9)])
print(g)
#Borrado de vertices
g.delete_vertices(0)
#Borrado de aristas
print(g)
nodoI = 7
nodoF = 8
eId = g.get_eid(nodoI,nodoF)
print("Arista encontrada: ",eId)
g.delete_edges(eId)
print(g)
for i in range (9):
    print(g.vs[i])
print(g.get_adjacency())
layout = g.layout_kamada_kawai()
layout = g.layout('kamada_kawai')

layout = g.layout_reingold_tilford( root =[2])
layout = g.layout("rt",2)

layout = g.layout('kk')
ig.plot(g,layout = layout)