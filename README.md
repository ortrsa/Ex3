# Ex3

## Overview 
- This project is an implementation of data structures and algorithms on directional weighted graph in python.    
- It is conversion from Ex2 that was made in java, you can find more about Ex2 in [Here](https://github.com/ortrsa/ex2).
- This is a text base program however you can still draw the graph with `plot_graph()` method. 
- This project was built from 3 parts:    

**part1:** implement basic directional weighted graph class `DiGraph` that contains simple functions on graph.

**part2:** implement `GraphAlgo` class that contains more advanced functions on graph.      

*(you can read all about the functions in [here](https://github.com/ortrsa/Ex3/wiki/Functions-explanation).)*
  
**part3:** compare running time and correctness between this project, [Ex2](https://github.com/ortrsa/ex2)  and [networkx](https://github.com/networkx/networkx).  

  - To see time compareition on circle graphs click **[here](https://github.com/ortrsa/Ex3/wiki/Time-comparison_-new)**.
  - For correctness report outputs click **[here](https://github.com/ortrsa/Ex3/wiki/circle-graph-time-comparison-and-correctness-check)**
  - *(you can find the correctness file in the src folder feel free to verified this output)*

  
# How To Run
 
first clone the repo:
```sh
$ git clone https://github.com/ortrsa/Ex3.git

```
than you can load graph from JSON file with `load_from_json("your_file_name")`,  
or create your own graph like this:  
```sh
my_DiG = DiGraph()

my_DiG.add_node(1)
my_DiG.add_node(2)
         .
         .
         .
         .
         .       edge weight
         .           |
                     V
my_DiG.add_edge(1,2,14)
my_DiG.add_edge(2,1,16)
         .
         .
         .
my_G = GraphAlgo(my_DiG)

"
put your code here....
"
        
```
Then you can apply on the graph any function from GraphAlgo,   
You can read all about the functions in [here](https://github.com/ortrsa/Ex3/wiki/Functions-explanation).


# How it's work..
After initializing the graph, the fun part begins.  
In GraphAlgo we implement advanced functions with some familiar algorithms like BFS, and dijkstra's.  


`shorest_path()` - use [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) to find the shortest path In the most efficient way.  
**Dijkstra's**  

![Alt Text](https://github.com/ortrsa/Ex3/blob/master/img/dWtprX5.gif)  


`connected_component()` - make 2 lists, list 1 contain all the nodes that you can get *from* the first node, and list 2 contain all the nodes that can get *to* the first node, and take the intersection between list 1 and 2.  
We are able to make these lists using [BFS](https://en.wikipedia.org/wiki/Breadth-first_search).  
**BFS**  

![Alt Text](https://github.com/ortrsa/Ex3/blob/master/img/KcsN.gif)  
  
  


`plot_graph()` - use [matplotlib](https://matplotlib.org/gallery/index.html) library to draw the graph.  

**A5 graph from data folder**  

![Alt Text](https://github.com/ortrsa/Ex3/blob/master/img/A5_graph.png)

# Links:
- [Dijkstra's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [BFS - Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Directed_graph - Wikipedia](https://en.wikipedia.org/wiki/Directed_graph)
- [correctness file output - Wiki](https://github.com/ortrsa/Ex3/wiki/circle-graph-time-comparison-and-correctness-check)
- [Ex2](https://github.com/ortrsa/ex2)
- [Functions - Wiki](https://github.com/ortrsa/Ex3/wiki/Functions-explanation)
- *(you can see the structure of the project in this [WikiPage](https://github.com/ortrsa/Ex3/wiki/Inherent-diagram).)*

# About:
This project is part of oop course of Ariel university and made for study purposes.  
This project was made by Or Trabelsi and Nadav Epstein, for more information please contact me, email - ortrsa@gmail.com.



