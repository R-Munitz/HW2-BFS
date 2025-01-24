#from matplotlib import pyplot as plt
import networkx as nx
from collections import deque

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """

    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")
    
    #returns the neighbors of a given node
    def get_neighbors(self, node):
        '''
        returns a list of all the neighbors of a given node
        '''
        return list(self.graph.neighbors(node))
    
    #checks if graph is unconnected
    def is_unnconnected(self, start):
        '''
        returns True if the graph is unconnected, False otherwise
        '''
        visited_nodes = self.run_bfs(start) 
        if len(visited_nodes) != len(self.graph):
            return True
        else:
            return False

    #handles edge cases   
    def validate_input(self, start, end=None):

        #empty graph
        if len(self.graph) == 0:
            raise ValueError("Empty graph")
        
        #start node not in graph
        elif start not in self.graph: #check this works as expected
            raise ValueError("Start node not in graph")
            
        #end node not in graph
        elif end not in self.graph and end != None:
            raise ValueError("End node not in graph")
    
        #start node = end node
        elif start == end:
            raise ValueError("Start node = End node!")
    
    #breath first traversal
    def run_bfs(self, start, end=None):

        '''
            #pseudocode for breadth first trasversal (from class)
            def BFS(G, source):
            Q = queue()
            visited = [ ]
            Q.push(source)
            visited.append(source)
            while Q is not empty:
                v = Q.pop()
                N = neighbors(v)
                for all w in N:
                    if w not in visited:
                        visited.append(w)
                        Q.push(w)
        #missing method to keep track of parent nodes to track shortest path
        '''

        #initialize a queue
        #use deque for more efficiency? or stick with list? 
        #queue = []
        queue = deque() 

        #initialize a list to store visited nodes
        visited_nodes =  []
       
        #dictionary to store parent nodes (used to reconstruct shortest path) 
        parent = {}

        #add the start node to the queue
        queue.append(start)
        #queue.push(start)

        #add the start node to the visited list
        visited_nodes.append(start)

        #set parent node of start = None
        parent[start] = None

        #while the queue is not empty
        while queue:
            #pop the first node in the queue
            #current_node = queue.pop(0)
            current_node = queue.popleft() #efficiency 0(1)

            # stop if reached end
            if current_node == end:
                break

            #get all neighboring nodes
            neighbors = self.get_neighbors(current_node) 
            
            # for each neighbor, check if it was visited, if not, add to visited list and queue
            for neighbor in neighbors:
                if neighbor not in visited_nodes: 
                    visited_nodes.append(neighbor)
                    #queue.push(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = current_node  #keeping track of path

                    
        #if no end node is given, return list of visited nodes in order of traversal
        if end == None:
            return list(visited_nodes)
        
        #if end node is reachable, return the shorest path
        if end in visited_nodes:
            path = []
            #backtrack from end node to start node
            while end != None:
                path.append(end)
                end = parent[end]
            #reverse path to get from start to end
            path[::1]
            return path
        else:
            print("No path found")
            return None
                

    def bfs(self, start, end=None):
        """
        This method performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, returns a list of nodes with the order of BFS traversal
        * If there is an end node input and a path exists, returns a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, returns None

        """
        
        #abstracted  edge cases to new method
        #ensure valid input
        self.validate_input(start, end)  

       
        #if graph is unconnected and end=None, raise error. cannot fully traverse unconnected graph
        if end == None:
            #ensure graph is connected
            if self.is_unnconnected(start):
                raise ValueError("Graph is unconnected, cannot traverse")
        
        #run bfs traversal
        path = self.run_bfs(start,end)
        return path  #path will be None if no path is found
        

        '''
        #abstracted to new method
        #edge cases
        #empty graph
        if len(self.graph) == 0:
            raise ValueError("Empty graph")
        

        #start node not in graph
        if start not in self.graph: #check this works as expected
            raise ValueError("Start node not in graph")
            
        
        #end node not in graph
        if end not in self.graph and end != None:
            raise ValueError("End node not in graph")
    
        
        #start node = end node
        if start == end:
            raise ValueError("Start node = End node!")
        

        '''

        '''
        #abstacted to new method
        #breadth first traversal
       
        #initialize a queue
        #use deque for more efficiency? or stick with list? 
        #queue = queue()
        queue = deque() 

        #initialize a list to store visited nodes
        visited_nodes =  []
       
        #dictionary to store parent nodes (used to reconstruct shortest path) 
        parent = {}

        #add the start node to the queue
        queue.append(start)
        #queue.push(start)

        #add the start node to the visited list
        visited_nodes.append(start)

        #parent node of start = None
        parent[start] = None

        #while the queue is not empty
        while queue:
            #pop the first node in the queue
            #current_node = queue.pop(0)
            current_node = queue.popleft() #efficiency 0(1)

            # stop if reached end
            if current_node == end:
                break

            #get all neighboring nodes
            neighbors = self.get_neighbors(current_node) 
            
            # for each neighbor, check if it was visited, if not, add to visited list and queue
            for neighbor in neighbors:
                if neighbor not in visited_nodes: 
                    visited_nodes.append(neighbor)
                    #queue.push(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = current_node #keeping track of path

                    
        #if no end node is given, return list of visited nodes in order of traversal
        if end == None:
            return list(visited_nodes)
        
        #if end node is reachable, return the shorest path
        if end in visited_nodes:
            path = []
            #backtrack from end node to start node
            while end != None:
                path.append(end)
                end = parent[end]
            #reverse path to get from start to end
            path.reverse()
            return path
        else:
            print("No path found")
            return None
    '''            


def main():
    """
    extra code to test Graph class
    """
   
    tiny_network_graph = Graph('data/tiny_network.adjlist')
    print(tiny_network_graph.graph)
    #print(tiny_network_graph.get_neighbors('Luke Gilbert'))
    #print(tiny_network_graph.bfs('Luke Gilbert','Martin Kampmann'))

    citation_network_graph = Graph('data/citation_network.adjlist')
    print((citation_network_graph.bfs('32024998','34095129')))
    #print(citation_network_graph.is_unnconnected('Tony Capra'))
    #print((citation_network_graph.bfs('Tony Capra')))

    '''
   #Extra code, plotting to help visualize graph 
    #plot graph
    plt.figure(figsize=(12, 8))
    nx.draw(
        citation_network_graph.graph, 
        with_labels=True, 
        node_size=500, 
        node_color="lightblue", 
        font_size=8, 
        font_weight="bold", 
        edge_color="gray"
    )
    plt.title("Graph Visualization")
    plt.show()
    '''

    pass

if __name__ == "__main__":
    main()


