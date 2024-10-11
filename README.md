<h1>Installing graspi_networkx via pip</h1>
<p>Below are instrictions regarding how to install graspi_networkx.</p>

## INSTALLATION
1. ```bash
   pip install graspi-networkx==0.2.5
   ```
2. That's it
<br>
<h2>USING THE PACKAGE</h2>
<p>After installing all dependencies, you're able to follow this formula in the command line</p>
<h3>Importing graspi_networkx via Python script</h3>
In a python script/IDE terminal, clone the repo:

```bash
git clone https://github.com/gobrin111/networkx_graspi_testing.git
```
<br>

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
1. Open Jupyter and create a new Notebook
2. In a cell put:
    ```bash
   !git clone https://github.com/gobrin111/networkx_graspi_testing.git
   ```
3. In the next cell, change directory into the cloned repo put:
   ```bash
   %cd networkx_graspi_testing
   ```
4. In the next cell, install the graspi_networkx package put:
   ```bash
   !pip install graspi-networkx==0.2.5
   ```
5. In the next cell, run the already made testing file (main.py) put:
   ```bash
   !python ./main.py ./2x2.txt
   ```
<h3>OUTPUTS</h3>
<ul>
   <li>Graph Creation: All the Nodes and Edges for the created Graph</li>
   <li>Last 2 nodes of Graph represent the blue and red nodes respectfully</li>
   <li>Subgraph: Nodes and edges for the created subgraph</li>
   <li>BFS: With the source node being 1, returns a 2d array that resembles the paths from each node to the source node</li>
   <li>Visualization: Shows a picture of the nodes and respective edges connected to each other</li>
</ul>
