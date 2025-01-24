# write tests for bfs
import pytest
from search import graph
import networkx as nx

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    #testing trasversal of all nodes in graph

    #create Graph object
    tiny_network_graph = graph.Graph('data/tiny_network.adjlist')

    #test bfs traversal valid start node
    start_node = 'Luke Gilbert'
    #assert correct number of nodes are traversed
    assert len(tiny_network_graph.bfs(start=start_node)) == 30
    #assert correct order of traversal
    assert tiny_network_graph.bfs(start=start_node) == ['Luke Gilbert', '33483487', '31806696', '31626775', '31540829', 'Martin Kampmann', 'Neil Risch', 
                                                        'Nevan Krogan', '32790644', '29700475', '34272374', '32353859', '30944313', 'Steven Altschuler',
                                                          'Lani Wu', 'Michael Keiser', 'Atul Butte', 'Marina Sirota', 'Hani Goodarzi', '32036252', '32042149', 
                                                          '30727954', '33232663', '33765435', '33242416', '31395880', '31486345', 'Michael McManus', 'Charles Chiu', '32025019']
    
    #test bfs traversal invalid start node
    start_node = 'Rochel Munitz'
    with pytest.raises(ValueError, match = "Start node not in graph"):
        tiny_network_graph.bfs(start=start_node)

    #test bfs traversal unconnected graph
    citation_network_graph = graph.Graph('data/citation_network.adjlist') #this is an unconnected graph
    start_node = 'Tony Capra'
    with pytest.raises(ValueError, match = "Graph is unconnected, cannot traverse"):
        citation_network_graph.bfs(start=start_node)

    pass

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """

    #testing bfs provides shortest path
    

    # valid start and end nodes
    citation_network_graph = graph.Graph('data/citation_network.adjlist')
    start_node = '32024998'
    end_node = 'Tony Capra'
    assert citation_network_graph.bfs(start=start_node, end=end_node) == ['32024998', 'Atul Butte', '32025013', 'Tony Capra'] 

    #test invalid end node
    end_node = 'Rochel Munitz'
    with pytest.raises(ValueError, match = "End node not in graph"):
        citation_network_graph.bfs(start=start_node, end=end_node)

    #test start node = end node
    with pytest.raises(ValueError, match = "Start node = End node!"):
        citation_network_graph.bfs(start=start_node, end=start_node)
    

    #test unreachable end node / unconnected graph returns None

    #create graph with unreachable node
    unconnected_graph = nx.DiGraph()

    #add nodes and edges
    unconnected_graph.add_nodes_from([1, 2, 3, 4, 5])
    unconnected_graph.add_edges_from([(1, 2), (2, 3), (3, 4)])

    #add unreachable node
    unconnected_graph.add_node(5)

    #test bfs search returns None for unreachable node
    start_node = '1'
    end_node = '5'
    assert unconnected_graph.bfs(start=start_node, end=end_node) == None


    pass

