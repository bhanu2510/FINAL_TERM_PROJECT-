# FINAL_TERM_PROJECT-
This project discussed about solving the Rubik cubes using Breadth first search and Bidirectional BFS
# Rubics_cube
A 2-Dimensional representation of an actual 3 x 3 Rubics cube.

## Requirements
  - [x] As this program is running on Python3, so Python3 http://python.org should be installed onto the device.
  - [x] This application requires `tkinter` module ` $pip install tkinter` for running.
  
## Features
  1. Easy to operate.
  2. Simple to understand.
  3. Increases the understanding of 3D shapes on a plane.

  
Our code implements 2 algorithms for solving/finding the shortest path between 2 states in a 2x2x2 Rubik's Cube. We have used Breadth-First-Search (BFS) and Bidirectional BFS.So, Here's a walkthrough of the code.

Functions:
shortest_path(start, end)
In this function, we provide the start state and the end state for solving our Rubik's Cube. This function starts from the start state and uses BFS algorithm to traverse the newer states until it reaches the end state. At the end, the path/moves leading to the end state is returned as a list.

shortest_path_optimized(start, end)
Here also, we provide the start state and the end state for solving our Rubik's Cube. This function starts from both the start state and end state using BFS. At each iteration, current state from both direction is checked if it is equals to each other or already visited from other direction. If it is already visited then the path is found. The reverse of the path from the end state is taken till the coinciding state which is reversed and each move's inverse is taken. This is merged after the path from start state till the coinciding state. Then, the path/moves leading to the end state is returned as a list.


Bidirectional BFS Optimization:
The Rubik's Cube states are explored simultaneously from both the start and end states, which can significantly reduce the search space and improve efficiency.
The algorithm maintains separate queues, distances, and parent dictionaries for both the forward and backward searches.
Output:
The code measures and prints the time taken by each algorithm to find the shortest path.
Example Usage:
The shortest_path function is used to find the shortest path using a basic BFS algorithm.
The shortest_path_optimized function is used to find the shortest path using an optimized Bidirectional BFS algorithm.
BFS is a tree traversal algorithm, in which the nodes at current level are checked before proceeding to next level. Our shortest_path(start, end) function implements BFS. In this function, we provide the start state and the end state for solving our Rubik's Cube. This function starts from the start state and uses BFS algorithm to traverse the newer states until it reaches the end state. At the end, the path/moves leading to the end state is returned as a list.
A dictionary called 'visited' is used to store visited states and their parent states along with the move applied.
Bidirectional BFS is a graph search algorithm, which finds the smallest path by traversing from start and end state using BFS. Our shortest_path_optimized(start, end) function implemented bidirectional BFS. Here also, we provide the start state and the end state for solving our Rubik's Cube. This function starts from both the start state and end state using BFS. At each iteration, current state from both direction is checked if it is equals to each other or already visited from other direction. If it is already visited then the path is found. The reverse of the path from the end state is taken till the coinciding state which is reversed and each move's inverse is taken. This is merged after the path from start state till the coinciding state. Then, the path/moves leading to the end state is returned as a list. If a state is encountered that has been visited from both ends, a path is reconstructed from the start to the common state and from the end to the common state.
The Rubik's Cube is represented as a tuple of 24 integers, where each integer represents the color of a sticker on a specific face of the cube. The order of stickers corresponds to the solved state. The algorithm maintains separate queues, distances, and parent dictionaries for both the forward and backward searches.
Bidirectional BFS often reduces the time complexity by exploring fewer states compared to a unidirectional BFS.
By searching from both ends, the algorithm narrows down the search space more quickly.
Path Reconstruction:
The found path is reconstructed by tracing back from the end state to the start state using the visited or start_parent and end_parent dictionaries.
Highlight the bidirectional exploration of states from both the start and end, aiming for convergence in the middle.
The aim of our project is to find the shortest path and increase the efficiency of finding the shortest path. Hence, our project returns the shortest path found using BFS and also calculates the time taken to find the shortest path. Also, we use bidirectional BFS to find the shortest path which may or maynot be the same path found by BFS and the time taken to find the shortest path. 
Bidirectional BFS is expected to be more efficient in terms of time complexity, as it explores the search space from both ends simultaneously.
Potential Extensions:
By explaining these details, the presentation can provide a comprehensive understanding of how the code works, its efficiency improvements, and potential areas for further exploration.


