# Maze Generator
### Group Members:
1. Josephine Uwizeye
2. Samwel Maisiba
3. Modester Mwangi
### Project Description

This project is about a game called the Maze Generator which we have created. The maze is created by a prearrangement of cell that will be 
inform of rectangular grids with wall sites in between them.
The predetermined arrangement will be considered as a connected graph with edges representing the pathways and nodes representing the cells.
The purpose of the maze generator algorithm is to make a subgraph that is challenging for users
to find the route between particular nodes. 

We are planning to use recursive back-tracker as a randomized version of the depth-first implemented with the 
Stacks. This approach will be done by a computer starting from a random generated cell and randomly selecting a neighbour from other cells
that have not been visited. The computer marks each cell visited . If the visited cell has no neighbours, this will be considered as a dead-end. This is where stacks play a role in facilitating back-tracking. 
From the dead-end the computer backtracks to the previous cells until it reaches a cell that has a neighbour that has not been visited.

This process continues until all unvisited cell are visited, this causes the computer to backtrack until the beginning cell. This maze will be completed as a large grid of cells 
inform of a board.

### Purpose of Data Structures and Algorithm Used
Depth First Search  traversal algorithm implemented using backtracking. This will help to traverse and visit
all cells in the grid by backtracking through the visited to unvisited cells using stacks.
Stacks will be used where the last cell visited is the first cell to be popped in backtracking.

### Purpose of Project
* Creating a game for Entertainment and Leisure during this pandemic.
* Show application of Graphs and applying learnt skills in this topic.
* Help people keep mind active and involved in away of challenging them solve hard puzzles in the game.

### Motivation Behind The Maze Generator
* The motivation behind creating a Maze is the curiosity of how graphs are applied in game development. From research, we saw that graphs are used in games that involve finding routes and mappings. Since Mazes include
 finding the shortest paths, we decided to use them.
* The other reason is to help people be entertained while assisting them to become problem 
solvers as users are required to use logic in finding paths. During this pandemic, many countries are in lockdown. Most schools have been closed, and many students are at home idle. By them playing this game, it will enable them to 
be active, entertained and as well learning.

### Technology Used
* Python Programming Language
* Pycharm IDE

### Project File Structure
* Create a Graphical User Interface and animation we used pygame.
* Create a grid for cell space connecting all neighbour cells resulting to connectivity graph.
* Assign random weights to every edge of the graph.
* Remove grid wall resulting to a perfect maze.
* Include Test Cases


### How to Run Application
* To run Application. Download and Install package pygame.


### Correctness of Algorithm
* Given a function to create full maze:
with looping variant containing number of visited cells in 
a stack list.
* (0 < length(stack) given function (x + w, y) to indicate a cell in east direction.
* If the cell is not visited and is in the frame, then it cannot be added in the stack list rather it will be 
added in list of unvisited cell.
* This is correct because a stack only cells that are visited, this will make program run through the unvisited cells in the grid
creating a full maze.

  
### Analysis of Algorithm
![Space Complexity](http://www.sciweavers.org/upload/Tex2Img_1619387817/render.png)
![Time Complexity](http://www.sciweavers.org/upload/Tex2Img_1619387599/render.png)

### Solution Description
During this Pandemic, a lot of children are not in school but rather at home. This also counts for those who are in school and are able to go home each day. During this time, parents are busy working to fend for their families and due to this, they have no time to play with their children. At this time, kids are bored while others are getting depressed because they are not active. In order to curb this problem, we created a Maze Generator for children at home to play during their leisure in order to keep their minds active and free for idleness.
This game will keep them entertained and also boost their knowledge because the game entails solving patterns while looking for the shortest path in the maze.
The game will also help students in colleges to be aware of the application of Data Structures Graphs in real-life scenarios.

### Recording of The Presentation
![img.png](img.png)


### Bibliography
Harder, D., 2012. Maze Generation | Algorithms and Data Structures | University of Waterloo. [online] Ece.uwaterloo.ca. <https://ece.uwaterloo.ca/~dwharder/aads/Algorithms/Maze_generation/> 
[Accessed 7 April 2021].

Internet, C., 2020. Random Maze Generator < JavaScript | The Art of Web. [online] The-art-of-web.com. Available at: 
<https://www.the-art-of-web.com/javascript/maze-generator/> [Accessed 7 April 2021].

Blades, A., 2020. Solving mazes with Depth-First Search. [online] Medium. Available at:
 <https://medium.com/swlh/solving-mazes-with-depth-first-search-e315771317ae> [Accessed 7 April 2021].

Makeschool.com. 2021. Generating a Maze with DFS | Trees and Mazes. [online] Available at: 
<https://www.makeschool.com/mediabook/oa/tutorials/trees-and-mazes/generating-a-maze-with-dfs/> 
[Accessed 25 April 2021].

Mathsisfun.com. 2021. Hexadecimal / Decimal Colors. [online] Available at: <https://www.mathsisfun.com/hexadecimal-decimal-colors.html> 
[Accessed 25 April 2021].








