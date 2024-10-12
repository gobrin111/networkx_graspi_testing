<h1>Installing graspi_networkx via pip</h1>
<p>Below are instrictions regarding how to install graspi_networkx.</p>

## INSTALLATION
1. In a python script/IDE terminal, clone the repo:
```bash
   git clone https://github.com/gobrin111/networkx_graspi_testing.git
```

2. Install graspi-networkx
```bash
   pip install graspi-networkx==0.2.9
```
<br>
<h2>USING THE PACKAGE</h2>
<p>After installing all dependencies, you're able to follow this formula in the command line</p>
<h3>Importing graspi_networkx via Python script</h3>

In the cloned repo, graspi_networkx is already imported, but if you'd like, delete it and write:
```bash
import graspi_networkx as gn
```
### Command Line Formula
`python .\main.py <input txt file>`

Example
```bash
python .\main.py .\2x2.txt
```

### Importing graspi_networkx via Jupyter Notebook
1. Install notebook:
```bash
   pip install notebook
   ```
2. Open Jupyter Notebook:
```bash
   jupyter notebook
   ```
3. Once opened, open the **Graspi-Networkx.ipynb** file
4. Click on the **Run** tab on top and click on **Run All Cells**

**If you wish to use a different test file, you may change cell 4 and replace "10x10.txt" with any file from the testFiles directory**

<h3>OUTPUTS</h3>
<ul>
   <li>Graph Creation: All the Nodes and Edges for the created Graph</li>
   <li>Last 2 nodes of Graph represent the blue and red nodes respectfully</li>
   <li>Subgraph: Nodes and edges for the created subgraph</li>
   <li>BFS: With the source node being 1, returns a 2d array that resembles the paths from each node to the source node</li>
   <li>Visualization: Shows a picture of the nodes and respective edges connected to each other</li>
   <li>Runtimes and Memory: Outputs a csv file which contains the runtimes for graph creation, subgraphs, and BFS as well as the total runtime</li>
</ul>
