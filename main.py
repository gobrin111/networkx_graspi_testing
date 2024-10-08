import graspi_networkx as gn

def main():
    #Node 0 is Blue and 1 is Red
    G = gn.createGraph("./2x2.txt")
    print("Nodes:", G.nodes())
    print("Edges:", G.edges())

    subgraph = gn.filterGraph(G)
    print("Subgraph Nodes:", subgraph.nodes())
    print("Subgraph Edges:", subgraph.edges())

if __name__ == "__main__":
    main()