import graspi_networkx as gn
import argparse
import networkx as nx
import matplotlib.pyplot as plt

import csv
import tracemalloc
import time
import os

parser = argparse.ArgumentParser(description="Run Python code with user input")
parser.add_argument("input_value", help="Input value to process")
args = parser.parse_args()
args = args.input_value

#obtains the average runtimes for each operation
#and gets the memory usage for overall
def writeRow(txt):
    row = []
    finalTotal = 0
    total = 0
    g = gn.createGraph(txt)
    for i in range(3):
        start = time.time()
        g = gn.createGraph(txt)
        total+=time.time()-start
    total = total/3
    finalTotal +=total
    row.append(total)
    total = 0

    for i in range(3):
        start = time.time()
        g_filtered = gn.filterGraph(g)
        total+=time.time()-start
    total = total / 3
    finalTotal+=total
    row.append(total)
    total = 0

    num_nodes = g.number_of_nodes()
    for i in range(3):
        start = time.time()
        bfs_paths=nx.single_source_shortest_path(g_filtered, source=num_nodes-1)
        total+=time.time()-start
    total = total / 3
    finalTotal += total
    row.append(total)
    row.append(finalTotal)
    tracemalloc.start()
    g=gn.createGraph(txt)
    g_filtered = gn.filterGraph(g)
    bfs_paths=nx.single_source_shortest_path(g_filtered, source=num_nodes-1)
    stats = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    stats = stats[1] - stats[0]
    row.append(stats)
    return row

def main():
    #Graph Creation
    G = gn.createGraph(args)
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
    gn.plotGraph(G)

    #writes to the csv file all the calculated times and memory usage
    # first column is the average runtime for graph creation
    # second column is the average runtime for graph filtering
    # third is the average runtime for BFS search
    # fourth is the overall average runtime
    # fifth is the overall memory usage for doing everything

    # runtime is measured in seconds
    # and memory is measured in bytes
    # results are sent to the out.csv file in the same directory
    file_exists = os.path.exists('out.csv')
    row = writeRow(args)
    with open('out.csv', mode='a' if file_exists else 'w', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['creation(s)','filtering(s)','bfs(s)','overall runtime(s)','whole memory usage(byte)'])
        writer.writerow(row)

if __name__ == "__main__":
    main()
