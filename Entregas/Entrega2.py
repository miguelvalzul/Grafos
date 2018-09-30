# -*- coding: utf-8 -*-
from itertools import permutations
    
class Graph(object):
    def __init__(self,vertex,edges):
        self.edges = edges
        self.vertex = vertex
        for i in edges:
            for j in i:
                assert j in vertex, \
                "invalid edge!"
    
    def isIsomorphTo(self,H):
        if(self.AdjacencyMatrix() == H.AdjacencyMatrix()):
            return True
        if((len(self.vertex) != len(H.vertex)) or (len(self.edges) != len(H.edges))):
            return False
        if(len(self.vertex)==len(H.vertex) and len(self.edges) == len(H.edges)):
            indxi = 0
            for i in self.AdjacencyMatrix():
                permut = [x for x in permutations(self.AdjacencyMatrix()[indxi])]
                for j in H.AdjacencyMatrix():
                    if tuple(j) in permut:
                        indxi += 1
                        break
                else:
                    return False
            return True
    
    def AdjacencyMatrix(self):
        matrix=[[0 for p in range(len(self.vertex))] for q in range(len(self.vertex))] #inicializa con ceros un arreglo doble de n x n, donde n es el número de nodos del grafo
        for i in range(len(self.vertex)):
        
            for j in range(len(self.vertex)):
    
                if((self.vertex[i],self.vertex[j]) in self.edges):
                    matrix[i][j]=1
                    matrix[j][i]=1
        return matrix



    def neighbors (self, u): #Retorna una lista de los vertices vecinos a 'u'
        neigh = []
        for i in self.edges: 
            if u in i:
                if i[0] == u: #Si u está en la primera posición de la tupla...
                    neigh.append(i[1])
                elif i[1] == u: #Si u está en la segunda posición de la tupla...
                    neigh.append(i[0])
        return neigh

    def distance(self,u,v): #va recorriendo el grafo a través de los vecinos de cada nodo y guarda los nodos visitados en una lista. Cuando el nodo 'v' ya está en la lista, se acaba y retorna la distancia
        assert u and v in self.vertex, \
               "Invalid vertex!!"
        current = [u] # el nodo, o los nodos actual(es). Se ve al grafo por capas
        visited = [u] #todos los nodos visitados
        dist = 1
        if u == v:
            return 0
        while 1:
            tmp = []
            for i in current:
                for k in (self.neighbors(i)): #Añade los elementos de la lista de vecinos 
                    if k not in visited:
                        visited.append(k)
                        tmp.append(k) 
                if v in visited: #si ya llegamos a la capa del grafo donde está 'v'...
                    return dist
            if not tmp: #if tmp is empty...
                return -1

            current=tmp
            dist += 1
    def connected(self): #Recorre todas las parejas de nodos y mira si alguna distancia de esas parejas es infinita        
        for i in self.vertex:
            for j in self.vertex:
                if self.distance(i,j) == -1:
                    return False
        return True
    def isTree(self):
        if (self.connected == True) and (len(self.edges) == len(self.vertex)-1): #Si el grafo está conectado y el # de lados es igual al # de nodos - 1
            return True
        return False
    def eccentricity(self,u): #retorna la mayor distancia del nodo u a todos los otros nodos
        assert u in self.vertex, \
               "Invalid vertex!!"
        ecc = 0
        if(not self.connected()): #si el grafo está desconectada, le excentricidad de todos los nodos es infinito
            return -1
        for i in self.vertex:
            func = self.distance(u,i)
            if func > ecc: #Actualiza el valor de 'ecc' cada que encuentra una distancia mayor
                ecc = func
        #if ecc == 0: #
         #   return -1
        return ecc
    def radius(self): # retorna la menor excentricidad entre los nodos del grafo 
        vertex= self.vertex[0] #cogemos un vertice cualquiera (siempre va a ser el primero de la lista de vertices, pero podria ser cualquier otro)
        rad = self.eccentricity(vertex) #inicializamos 'rad' con la excentricidad de ese vertice
        for i in self.vertex:
            #print "Excentricidad de ", i, ": ",self.eccentricity(i)
            func = self.eccentricity(i)
            if func < rad: #Si encuentra alguna excentricidad menor...
                rad = func
        return rad

    def diameter(self): #retorna la mayor distancia entre dos nodos del grafo 
        diam = 0
        for i in self.vertex:
            for j in self.vertex:
                func = self.distance(i,j)
                if func > diam: #Si esa distancia es mayor que la actual...
                    diam = func
        return diam

    def eulerian(self):
        for i in self.vertex:
            if (len(self.neighbors(i))) % 2 == 1: #Si algún nodo es de grado impar...
                return False
        return True
        
        
            
        
K = Graph(["a","b","c","d"],[("a","b"),("a","d"),("c","d")])
H = Graph(["j","o","k","p"],[("p","j"),("j","k"),("k","o")])
#F = Graph(["d","e","f"], [("a","b"),("e","f")]) #Esto muestra que el constructor verifica que los lados correspondan a los nodos definidos
J = Graph(["a","b","c","d"],[("a","b"),("b","c"),("c","d"),("d","b")])

G = Graph(["a","b","c","d","e","f","g","h"],[("a","b"),("a","d"),("c","d"),("d","e"),("e","f"),
                                             ("f","g"),("b","h"),("h","g"),("c","h"),("d","h")])
print " La distancia entre los nodos b y e es :"
print G.distance("b", "e")
print ""
print " Esta el grafo G conectado?:"
print G.connected()
print ""
print "El grafo G es isomorfo a un arbol?:"
print G.isTree()
print ""
print "excentricidad de un nodo h"
print G.eccentricity("h")
print ""
print "radio del grafo"
print G.radius()
print ""
print "diametro del grafo"
print G.diameter()
print ""
print "el grafo g contiene un camino euleriano?"
print G.eulerian()
print ""
#Miguel Valencia Z.
#Juan Camilo Hoyos

