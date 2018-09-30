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
    def subdistancia(self,u,v):
        if ((u,v) or (v,u)) in self.edges:
            print "hoyos es gay"
            return 1
        else:
            for i in self.edges:
                
                if u in i:
                    if i[0] == u:
                        u = i[1]
                        return 1 + self.subdistancia(u,v)
                    else:
                        u = i[0]
                        return 1 + self.subdistancia(u,v)
    def distancia(self,u,v):
        assert u and v in self.vertex, \
               "invalid vertex"
        return self.subdistancia(u,v)
##        for i in self.edges:
##            if u in i:
##                if i[0]==u:
##                    for j in self.edges:
##                        if i[1] in j and u not in j:
##                elif i[1] == u:
##                    
                            
    
                

G = Graph(["a","b","c","d","e"],[("c","d"),("b","c"),("d","e"),("a","e"),("a","b")])
K = Graph(["a","b","c","d"],[("a","b"),("a","d"),("c","d")])
H = Graph(["j","o","k","p"],[("p","j"),("j","k"),("k","o")])
#F = Graph(["d","e","f"], [("a","b"),("e","f")]) #Esto muestra que el constructor verifica que los lados correspondan a los nodos definidos
J = Graph(["a","b","c","d"],[("a","b"),("b","c"),("c","d"),("d","b")])
print "Matriz de adyacencia de G: ", (G.AdjacencyMatrix())
print "Matriz de adyacencia de H: ", (H.AdjacencyMatrix())
print "G es isomorfo a H? ", G.isIsomorphTo(H)
print G.distancia("a","c")
print "-----------------------------------------------------"

print "Matriz de adyacencia de J: ", (J.AdjacencyMatrix())
print "J es isomorfo a H? ", J.isIsomorphTo(H)

#Miguel Valencia Z.

