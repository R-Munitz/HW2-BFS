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
        elif start not in self.graph: 
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
        #useing deque for more effieciency (looked up this kind of queue)
        queue = deque() 

        #initialize a list to store visited nodes
        visited_nodes =  []
       
        #dictionary to store parent nodes (used to reconstruct shortest path) 
        parent = {}

        #add the start node to the queue
        queue.append(start)

        #add the start node to the visited list
        visited_nodes.append(start)

        #set parent node of start = None
        parent[start] = None

        #while the queue is not empty
        while queue:
            #pop the first node in the queue
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
            path = path[::-1]
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
        #ensure valid input
        self.validate_input(start, end)  

        #if graph is unconnected and end=None, raise error. cannot fully traverse unconnected graph
        if end == None:
            if self.is_unnconnected(start):
                raise ValueError("Graph is unconnected, cannot traverse")
        
        #run bfs traversal
        path = self.run_bfs(start,end)

        return path  #path will be None if no path is found