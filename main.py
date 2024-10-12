import graspi_networkx as gn
import argparse
import networkx as nx
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Run Python code with user input")
parser.add_argument("input_value", help="Input value to process")
args = parser.parse_args()
args = args.input_value

def main():
    #Graph Creation
    G = gn.createGraph("./testFiles/10x10.txt")
    print("Nodes:", G.nodes())
    print("Edges:", G.edges())

    #Graph Filtering
    filteredGraph = gn.filterGraph(G)
    print("Subgraph Nodes:", filteredGraph.nodes())
    print("Subgraph Edges:", filteredGraph.edges())

    #BFS
    numNodes = G.number_of_nodes()
    bfs = gn.bfs(filteredGraph, numNodes-1)
    print("BFS:", bfs)

    #Visualization
    nx.draw(G, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()