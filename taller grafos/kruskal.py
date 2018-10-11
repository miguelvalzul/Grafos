
class WGraph(object):
    def __init__(self,Vertex,Edges):
        self.v=Vertex
        self.e=Edges


    def weightmatrix(self):
        matriz=[[0 for p in range(len(self.v))] for q in range(len(self.v))]
        cont1=0
        cont2=0
        for i in self.v:
            for j in self.v:
                if (i,j) in self.e:
                    matriz[cont1][cont2]=self.e[(i,j)]
                    matriz[cont2][cont1]=self.e[(i,j)]
                cont2+=1
            cont2=0
            cont1+=1
        #self.printmatrix(matriz)
        return matriz

    def kruskal(self):
        nodos = []
        lados = []
        for i in self.v:
            nodos.append(i)

        for i in self.e:
            lados.append(i)
        cont1 = 0

        for i in lados:#se ordenan las tuplas en una lista dependiendo de su peso de menor a mayor
            cont2=0
            for j in lados:
                temp = ''
                if self.e[i] < self.e[j]:
                    temp = j
                    lados[cont2] = lados[cont1]
                    lados[cont1] = j
                cont2+=1
            cont1+=1
        

G = WGraph(["q","r","t"] , {("q","r"):1,("r","t"):15,("q","t"):8})
print G.kruskal()

#print G.weightmatrix()
