from Edges import G, addNodes,edges, G1,positions1
import math
def get_neighbors(G, v):
    return G[v]
# This is heuristic function which has an equal values for all nodes
def h(n,G={},start=0,end=0):
    H=addNodes(edges,1)
    return H[n]
# def h(n,stop,positions):
#     for i in positions:
#         if i[0]==n:
#             x1=i[1][0]
#             y1=i[1][1]
#         if i[0]==stop:
#             x2=i[1][0]
#             y2=i[1][1]
#     return int(math.sqrt(abs(x2 - x1)**2 + abs(y2 - y1)**2))
def a_star_algorithm(G, start, stop, edges, positions):
#open_lst: a list of nodes which have been visited, but who's neighbours haven't all been always inspected, It starts off with the start node
#closed_lst: a list of nodes which have been visited and who's neighbors have been always inspected
    open_lst = set([start])
    closed_lst = set([])
    # the default value is +infinity
    dist={}#dist has present distances from start to all other nodes
    dist[start]=0
    path={}# path contains an adjac mapping of all nodes
    path[start]=start
    while len(open_lst) > 0:
        n=None
        for lowfv in open_lst:# it will find a node with the lowest value of f()
            if n==None or dist[lowfv]+h(lowfv,edges)<dist[n]+h(n,edges):
                n=lowfv
        if n==None:
            print('Path does not exist!')
            return None
        # if the current node is the stop then we start again from start
        if n==stop:
            reconst_path=[]
            while path[n]!=n:
                reconst_path.append(n)
                n=path[n]
            reconst_path.append(start)
            reconst_path.reverse()
            print('Path found:{}'.format(reconst_path))
            return reconst_path
        # for all the neighbors of the current node do
        for a in get_neighbors(G, n):
            m,weight=a[0],a[1]
# if the current node is not presentin both open_lst and closed_lst add it to open_lst and note n as it's path
            if m not in open_lst and m not in closed_lst:
                open_lst.add(m)
                path[m]=n
                dist[m] = dist[n] + weight
# otherwise, check if it's quicker to first visit n, then m and if it is, update path data and poo data
# and if the node was in the closed_lst, move it to open_lst
            else:
                if dist[m]>dist[n]+weight:
                    dist[m] = dist[n] + weight
                    path[m] = n
                    if m in closed_lst:
                        closed_lst.remove(m)
                        open_lst.add(m)
#remove n from the open_lst, and add it to closed_lst because all of his neighbors were inspected
        open_lst.remove(n)
        closed_lst.add(n)
    print('Path does not exist!')
    return None
a_star_algorithm(G,'Gate 2', 'Tapal 1',edges, positions1)







# from collections import deque
 
# "Graph Helper Functions"

# def addNodes(G, nodes): # Takes a list of nodes, adds them to the graph. No edges
#     for i in nodes:
#         G[i] = []
#     return G

# def listOfNodes(G):
#     return list(G.keys())


# """works without addNodes too"""
# def addEdges(G, edges, directed = False): #Wtakes a list of edges, adds them to graph. 
#     if directed:
#         for i in edges:
#             if i[0] in G:
#                 G[i[0]].append(i[1:])
#             else:
#                 G[i[0]] = [i[1:]]
#     else:
#         for i in edges:

#             if i[0] in G:
#                 G[i[0]].append(i[1:])
#             else:
#                 G[i[0]] = [i[1:]]

#             if i[1] in G:     
#                 G[i[1]].append((i[0],i[-1]))
#             else:
#                 G[i[1]] = [(i[0],i[-1])]

#     return G


# def listOfEdges(G, directed): #has to be fixed, doesn't accept directed
#     accu = []
#     for i in G:
#         q = G[i]
#         for x in G[i]:

#             if (x[0], i, x[1]) not in accu:

#                 accu.append((i, x[0] ,x[1]))

#     return accu


# def out_edges(Graph, i):
#     accu = []
#     for edge in Graph[i]:
#         accu.append(edge[0])
#     return accu

# def printDegree(G):
#     for i in G:
#         x = G[i]
#         print(i ,  "=>"     , len(x))



# def printIn_OutDegree(G):
#     out_degree,in_Degree=[],[]
#     for a in G:
#         out_degree.append(len(G[a]))
#         for b in G[a]:

#             in_Degree.append(b[0])
#     count = 0
#     for a in G:
        
#         print(a," => In Degree: ",in_Degree.count(a),", Out Degree:",out_degree[count])
#         count += 1

# def getNeighbours(G,node):
#     nodes = []
#     keys = G[node]

#     for a in keys:

#         nodes.append(a[0])
#     return nodes

# def getInNeighbours(G,node):
#     lst_neigh = []

#     for i in G:

#         for j in G[i]:

#             if j[0]==node:

#                 lst_neigh.append(i)

#     return lst_neigh



# def NearestNeighbour(G,node):
#     index = []
#     weight = []

#     for p in G[node]:
#         index.append(p[0])
#         weight.append(p[1])



#     p = weight.index(min(weight))
#     return index[p]

# def isNeighbor(G, Node1, Node2):


#     for x in G[Node1]:

#         if x[0] == Node2:
#             return True

#         else:
#             return False

# def removeNode(G, node):
#     G.pop(node)

#     for i in G:
#         for v in G[i]:

#             if v[0] == node:

#                 G[i].remove(v)
#     return G

# def removeNodes(G, nodes):
#     for node in nodes:
#         G.pop(node)

#         for i in G:

#             for vv in G[i]:
#                 if vv[0] == node:

#                     G[i].remove(vv)

#     return G


# def displayGraph(G):
#     print(G)


# def printadjmatrix(G):
#     accu=[]
#     x=listOfNodes(G)
#     for alpha in range(len(x)):
#       index=[]

#       for b in range(len(x)):
#         index.append(0)
#       accu.append(index)
#     for alpha in G:

#       for b in G[alpha]:
#         accu[alpha-1][b[0]-1]=b[1]
#     return accu

# def getOutNeighbours(G, node): # Returns all out neighbours in the node from graph
#     index = []

#     for x in G[node]:

#         index.append(x[0])

#     return index

# #queue functions
# def enqueue(q, item):
#     q.append(item)
# def dequeue(q):
#     return q.pop(0)

# class Graph:
#     def __init__(self, adjac_lis):
#         self.adjac_lis = adjac_lis
 
#     def get_neighbors(self, v):
#         return self.adjac_lis[v]
 
#     # This is heuristic function which is having equal values for all nodes
#     def h(self, n):
#         H = {
#             'A': 1,
#             'B': 1,
#             'C': 1,
#             'D': 1
#         }
 
#         return H[n]
 
#     def a_star_algorithm(self, start, stop):
#         # In this open_lst is a lisy of nodes which have been visited, but who's 
#         # neighbours haven't all been always inspected, It starts off with the start 
#   #node
#         # And closed_lst is a list of nodes which have been visited
#         # and who's neighbors have been always inspected
#         open_lst = set([start])
#         closed_lst = set([])
 
#         # poo has present distances from start to all other nodes
#         # the default value is +infinity
#         poo = {}
#         poo[start] = 0
 
#         # par contains an adjac mapping of all nodes
#         par = {}
#         par[start] = start
 
#         while len(open_lst) > 0:
#             n = None
 
#             # it will find a node with the lowest value of f() -
#             for v in open_lst:
#                 if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
#                     n = v;
 
#             if n == None:
#                 print('Path does not exist!')
#                 return None
 
#             # if the current node is the stop
#             # then we start again from start
#             if n == stop:
#                 reconst_path = []
 
#                 while par[n] != n:
#                     reconst_path.append(n)
#                     n = par[n]
 
#                 reconst_path.append(start)
 
#                 reconst_path.reverse()
 
#                 print('Path found: {}'.format(reconst_path))
#                 return reconst_path
 
#             # for all the neighbors of the current node do
#             for (m, weight) in self.get_neighbors(n):
#               # if the current node is not presentin both open_lst and closed_lst
#                 # add it to open_lst and note n as it's par
#                 if m not in open_lst and m not in closed_lst:
#                     open_lst.add(m)
#                     par[m] = n
#                     poo[m] = poo[n] + weight
 
#                 # otherwise, check if it's quicker to first visit n, then m
#                 # and if it is, update par data and poo data
#                 # and if the node was in the closed_lst, move it to open_lst
#                 else:
#                     if poo[m] > poo[n] + weight:
#                         poo[m] = poo[n] + weight
#                         par[m] = n
 
#                         if m in closed_lst:
#                             closed_lst.remove(m)
#                             open_lst.add(m)
 
#             # remove n from the open_lst, and add it to closed_lst
#             # because all of his neighbors were inspected
#             open_lst.remove(n)
#             closed_lst.add(n)
 
#         print('Path does not exist!')
#         return None

# adjac_lis = {
#     'A': [('B', 1), ('C', 3), ('D', 7)],
#     'B': [('D', 5)],
#     'C': [('D', 12)]
# }
# graph1 = Graph(adjac_lis)
# graph1.a_star_algorithm('A', 'D')