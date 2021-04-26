import random
import time

import pygame

#create lengths of window
width = 500
height = 600
frame_rater = 20

#pygame initializing
pygame.init()
pygame.mixer.init()
displays = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Generator")
timing = pygame.time.Clock()


#set up coulours of maze window
white = (255, 255, 255) #colour of the walls of cells
green = (0, 255, 0) #colour of the frame of maze
black =( 0, 0, 0) #colour of backtracker
red =( 255, 0, 0) #colour of the shortest path of the maze

#starter positions
x_axis = 0
y_axis = 0
cell_width = 20
frame = [] #hold list of cells in the maze grid
stop_by = [] #hold list of visited cells
stack = [] #help pop visited cells when the program reaches dead-end and it requires to backtrack
shortest_path = {} #hold coordinates of shortest path in a dictionary

#build framework
def create_frame(x_axis, y_axis, cell_width):
   for i in range(1, 21):
         x_axis = 20 #point of start of the maze
         y_axis = y_axis + 20 #point of start of a new line

         for j in range( 1, 21):
             pygame.draw.line(displays, white, [x_axis, y_axis], [x_axis + cell_width, y_axis]) #North of a cell
             pygame.draw.line(displays, white, [x_axis + cell_width, y_axis], [x_axis + cell_width, y_axis + cell_width]) #East of a cell
             pygame.draw.line(displays, white, [x_axis + cell_width, y_axis + cell_width], [x_axis, y_axis + cell_width]) #South of a cell
             pygame.draw.line(displays, white, [x_axis, y_axis + cell_width], [x_axis, y_axis]) #west of a cell
             frame.append((x_axis, y_axis)) #put a cell in the list making the frame
             x_axis = x_axis + 20 #move cells to a new point




def move_north(x_axis, y_axis):
    pygame.draw.rect(displays, green, (x_axis + 1, y_axis - cell_width + 1, 19, 39), 0)  # draw the rectangle
    pygame.display.update()

def move_south(x_axis, y_axis):
    pygame.draw.rect(displays, green, (x_axis  + 1, y_axis + 1, 19, 39), 0)  # draw the rectangle
    pygame.display.update()

def move_west(x_axis, y_axis):
    pygame.draw.rect(displays, green, (x_axis - cell_width + 1, y_axis + 1, 39, 19), 0)  # draw the rectangle
    pygame.display.update()

def move_east(x_axis, y_axis):
    pygame.draw.rect(displays, green, (x_axis + 1, y_axis + 1, 39, 19), 0) #draw the rectangle
    pygame.display.update()

def visiting_cell( x_axis, y_axis): #draw one cell
    pygame.draw.rect(displays, black, (x_axis +1 , y_axis + 1, 18, 18), 0)
    pygame.display.update()

def draw_backtracker(x_axis, y_axis):
    pygame.draw.rect(displays, green, (x_axis +1, y_axis +1, 18, 18), 0)
    pygame.display.update()                                        # colour visited cell


def shortestpath_cell(x_axis,y_axis):
    pygame.draw.rect(displays, red, (x_axis+8, y_axis+8, 5, 5), 0)
    pygame.display.update()                                        #colour of shortest path in maze


def create_maze(x_axis,y_axis):
    visiting_cell(x_axis, y_axis)   # starting positing of maze
    stack.append((x_axis,y_axis))      # put each visited cell in stack
    stop_by.append((x_axis,y_axis)) # add each visited cell to stop_by cells list

    while len(stack) > 0:            # loop through cells in the stack list if its not empty
        time.sleep(.06)          # reduce speed of program
        unvisited_cells = []      #hold list of unvisited cells
        if (x_axis + cell_width, y_axis) not in  stop_by and (x_axis + cell_width, y_axis) in frame: #check if the cell in the east is visited and if not then add it to unvisited cell list and name it east
            unvisited_cells.append("east")

        if (x_axis - cell_width, y_axis) not in stop_by and (x_axis - cell_width, y_axis) in frame:
            unvisited_cells.append("west")

        if (x_axis , y_axis + cell_width) not in stop_by and (x_axis , y_axis + cell_width) in frame:
            unvisited_cells.append("south")

        if (x_axis, y_axis - cell_width) not in stop_by and (x_axis , y_axis - cell_width) in frame:
            unvisited_cells.append("north")

        if len(unvisited_cells) > 0:                                          #if there are unvisited cells
            chosen_cell = (random.choice(unvisited_cells))                    # then randomly choose a cell from that list

            if chosen_cell == "east":                             # if cell in east is chosen then call move_east function
                move_east(x_axis, y_axis)
                shortest_path[(x_axis + cell_width, y_axis)] = x_axis, y_axis
                x_axis = x_axis + cell_width                                         # make this cell the current cell
                stop_by.append((x_axis, y_axis))                              # then add it to visited cells list
                stack.append((x_axis, y_axis))                                # and place it in the stack list

            elif chosen_cell == "west":
                move_west(x_axis, y_axis)
                shortest_path[(x_axis - cell_width, y_axis)] = x_axis, y_axis
                x_axis = x_axis - cell_width
                stop_by.append((x_axis, y_axis))
                stack.append((x_axis, y_axis))

            elif chosen_cell == "south":
                move_south(x_axis, y_axis)
                shortest_path[(x_axis , y_axis + cell_width)] = x_axis, y_axis
                y_axis = y_axis + cell_width
                stop_by.append((x_axis, y_axis))
                stack.append((x_axis, y_axis))

            elif chosen_cell == "north":
                move_north(x_axis, y_axis)
                shortest_path[(x_axis , y_axis - cell_width)] = x_axis, y_axis
                y_axis = y_axis - cell_width
                stop_by.append((x_axis, y_axis))
                stack.append((x_axis, y_axis))
        else:
            x_axis, y_axis = stack.pop()                                    # pop one cell from the stack when the program reaches a dead end
            shortestpath_cell(x_axis, y_axis)                                     # use single_cell function to show backtracking image
            time.sleep(.05)                                       # reduce speed of program
            draw_backtracker(x_axis, y_axis)                               # use colour black to show backtracking


def shortestpath_backtostart(x_axis, y_axis):
    shortestpath_cell(x_axis, y_axis)
    while (x_axis, y_axis) != (20,20):    #loop until the starting position
        x_axis, y_axis = shortest_path [x_axis, y_axis]
        shortestpath_cell(x_axis, y_axis)
        time.sleep(.1)


create_frame(40, 0, 20)
create_maze(20, 20)
shortestpath_backtostart(400, 400)


play = True
#loop through the game
while play:
    # keep running at the at the right speed
    timing.tick(frame_rater)
    # process input (events)
    for e in pygame.event.get():
        # check for closing the window
        if e.type == pygame.QUIT:
            play = False

























