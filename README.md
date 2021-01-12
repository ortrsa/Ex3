# Ex3

## Overview 
- This project is an implementation of data structures and algorithms on directional weighted graph in python.    
- It is converthion from Ex2 that was made at java, you can find more abut Ex2 in [Here](https://github.com/ortrsa/ex2).
- This is a text base program however you can still drow the graph with `plot_graph()` method. 
- This project was build from 3 parts:    

**part1:** imploment basic directional weighted graph class `DiGraph` that contains simpale functions on graph.

**part2:** imploment `GraphAlgo` class, that contains more advanced functions on graph.      

*(you can find all the relevant functions in this [WikiPage](https://github.com/ortrsa/Ex3/wiki/Inherent-diagram).)*  
**part3:** compare runing time and correctness between this project, [Ex2](https://github.com/ortrsa/ex2)  and [networkx](https://github.com/networkx/networkx).  

  - To see time compareition on circal graphs click **[here](https://github.com/ortrsa/ex2)**.
  - To see time compareition on random graphs click **[here](https://github.com/ortrsa/ex2)**.
  - For correctness report outputs click **[here](https://github.com/ortrsa/ex2)**
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
You can read about all the functions in detail [here](https://github.com/ortrsa/Ex3/wiki/Functions-explanation).


# How it's work..
This algorithm calculates the shortest path from each agent to the closest free pokemon.
I found that the easiest way to understand the implementation of this algorithm is with a flow chart:

![alt text](https://i.ibb.co/M5WHNcV/2020-12-20-17-07-53.png)

- **Run():** run the thread.
- **Init():** before each level load the relevant graph, open GUI class, first placed of Pokemon's and place  
 agents closest as possible to Pokemon's with high value.
- **Is running:** if the time ends stop the game and return the result, else keep moving agents.
- **Move agent():** this method responsible for the course of the game, updates Pokemon's and agent location continuously,  
and call to all the following function...
- **Deal With Eaten():** After getting updated information abput the Pokemons we have we check if the pokemons that the agents 
are chasing now are in the updated list of Pokemons and if not we know the agents ate them so we need to clear the agents
so they'll be free to chase other Pokemons and we need to remove the pokemons from the being chaased list as well so well know weren't chasing them any more.  
- **Set Poke Catch():** Gets an agent and checks whos the closest Pokemon to this agent (only from the pokemons that aren't being chased yet) .
Then sets the agent List of nodes to the shortestpath to the pokemon location and now the agent will move thowards that pokemon.  
- **NextNode():** Returns the next node the agent needs to go to get to his destination by going to the HashMap (PathMap) and look at the agent Path and every time removing the head of the list and sending him to the first node on the list (because we removing the head every time he'll always need to go to the first node on the list)
then we set his edge by his src (the node his on right now) and his dest that we choosed from the list. we also changing the dt to reduce unnessecery calls from the server.  
              


# Links:
- [Dijkstra's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Directed_graph - Wikipedia](https://en.wikipedia.org/wiki/Directed_graph)
- [correctnes file output - Wiki](https://github.com/ortrsa/Ex2/wiki/result)
- [Ex2](https://github.com/ortrsa/ex2)
- [Functions - Wiki](https://github.com/ortrsa/Ex3/wiki/Functions-explanation)

# About:
This project is part of oop course of Ariel university and made for study purposes.  
This project made by Or Trabelsi and Nadav Epstein, for more information please contact me, email - ortrsa@gmail.com.



