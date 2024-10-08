import networkx as nx
import math
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Run Python code with user input")
parser.add_argument("input_value", help="Input value to process")
args = parser.parse_args()
args = args.input_value


def createGraph(txt):
    g = nx.Graph()
    g = nx.Graph(g) #makes sure that it is an undirect graph
    nodeIndex=0
    with open(txt,'r') as file:
        lines = file.readlines()
        metadata = lines[0].strip().split()
        x = int(metadata[0])
        y = int(metadata[1])
        row = lines[1].strip().split()
        for i in range(x): #creates bottom row of structure
            currentColor = 'white'
            if(row[i]=='0'):
                currentColor = 'black'
            g.add_node(nodeIndex,color=currentColor)
            if(i!=0):
                g.add_edge(nodeIndex,nodeIndex-1, weight=1)
            nodeIndex+=1
        for a in range(y+1):
            if(a==0 or a==1): #skips over the metadata and the first row of the graph, since those two lines have already been processed
                continue
            row = lines[a].strip().split()
            for i in range(x):
                currentColor = 'white'
                if(row[i]=='0'):
                    currentColor = 'black'
                g.add_node(nodeIndex,color=currentColor)
                g.add_edge(nodeIndex,nodeIndex-x,weight=1) #node below current node
                if(i!=0):
                    g.add_edge(nodeIndex,nodeIndex-1, weight=1) #node to the left of the current node
                    g.add_edge(nodeIndex,nodeIndex-(x+1), weight=math.sqrt(2)) #node to the bottom left of the current node
                if(i!=x-1):
                    g.add_edge(nodeIndex,nodeIndex-(x-1),weight=math.sqrt(2)) #node to the bottom right of the current node
                nodeIndex+=1
    print(nodeIndex)
    g.add_node(nodeIndex, color='blue')
    nodeIndex+=1
    g.add_node(nodeIndex,color='red')
    for i in range(x):
        g.add_edge(nodeIndex-1,i,weight=1) #bottom connection to the blue element  
        g.add_edge(nodeIndex,i+(x*(y-1))) #top connection to the red element
    nodeIndex+=1
    return g


def filterGraph(inputG):
    filter_edges = []
    filtered_edges = [(u, v) for u, v, d in inputG.edges(data=True) if ((inputG.nodes[v]['color'] == 'black') and (inputG.nodes[u]['color'] == 'black')) or ((inputG.nodes[v]['color'] == 'red') and (inputG.nodes[u]['color'] == 'black')) or ((inputG.nodes[v]['color'] == 'black') and (inputG.nodes[u]['color'] == 'red')) or ((inputG.nodes[v]['color'] == 'white') and (inputG.nodes[u]['color'] == 'white')) or ((inputG.nodes[v]['color'] == 'white') and (inputG.nodes[u]['color'] == 'blue')) or ((inputG.nodes[v]['color'] == 'blue') and (inputG.nodes[u]['color'] == 'white'))]
    H = nx.Graph()
    H.add_nodes_from(inputG.nodes(data=True))
    H = inputG.edge_subgraph(filtered_edges)
    

    return H


g = createGraph(args)
print(g.nodes())
f_g=filterGraph(g)
print(f_g.nodes())

bfs_paths = nx.single_source_shortest_path(f_g, source=1)

nx.draw(g, with_labels=True)
plt.show()



