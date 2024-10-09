import graspi_networkx as gn
import argparse
import networkx as nx
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Run Python code with user input")
parser.add_argument("input_value", help="Input value to process")
args = parser.parse_args()
args = args.input_value

def main():
    #Node 0 is Blue and 1 is Red
    #Graph Creation
    G = gn.createGraph(args)
    print("Nodes:", G.nodes())
    print("Edges:", G.edges())

    #Graph Filtering
    filteredGraph = gn.filterGraph(G)
    print("Subgraph Nodes:", filteredGraph.nodes())
    print("Subgraph Edges:", filteredGraph.edges())

    #BFS
    bfs = gn.bfs(filteredGraph)
    print("BFS:", bfs)

    #Visualization
    nx.draw(G, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()