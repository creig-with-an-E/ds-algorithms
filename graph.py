class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacentList = {}
    
    def add_vertex(self, value):
        # append to the object if it don't exist
        if value not in self.adjacentList:
            self.adjacentList[value] = []
            self.number_of_nodes += 1

    def add_edge(self, node_1, node_2):
        # is this directed or undirected???
        # if undirected we make the connection both sides
        if self.adjacentList.get(node_1) is not None:
            self.adjacentList[node_1].append(node_2)
            self.adjacentList[node_2].append(node_1)


    def showConnections(self):
        all_nodes = self.adjacentList.keys()
        for node in all_nodes:
            node_connections = self.adjacentList[node]
            connections = ''
            for vertex in node_connections:
                connections += vertex + " "
            print(node + ' ---> ' + connections, sep=' ')


myGraph = Graph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')

myGraph.add_edge('3', '1') 
myGraph.add_edge('3', '4') 
myGraph.add_edge('4', '2') 
myGraph.add_edge('4', '5') 
myGraph.add_edge('1', '2') 
myGraph.add_edge('1', '0') 
myGraph.add_edge('0', '2') 
myGraph.add_edge('6', '5')

myGraph.showConnections()