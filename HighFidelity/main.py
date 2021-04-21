import pygame

#create lengths of window
width = 500
height = 800
frame_rater = 40

#pygame initializing
pygame.init()
pygame.mixer.init()
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Generator")
timing = pygame.time.Clock()


#set up coulours of maze window
white = (255, 255, 255)
green = (0, 255, 0)
purple =( 0, 0, 255)
red =( 255, 0, 0)


#maze variables
x_axis = 0
y_axis = 0
cell_width = 10
frame = []
stop_by = []
stack = []
results = {}

#build framework

def frame(x_axis, y_axis, cell_width):
   for i in range(1, 31):
         x_axis = 30 #point of start of the maze
         y_axis = y_axis + 30 #point of start of a new line

         for j in range( 1, 31):
             pygame.draw.line(display, white, [x_axis, y_axis], [x_axis + cell_width, y_axis]) #North of a cell
             pygame.draw.line(display, white, [x_axis + cell_width, y_axis], [x_axis + y_axis, y_axis + cell_width]) #East of a cell
             pygame.draw.line(display, white, [x_axis + y_axis, y_axis + cell_width], [x_axis, y_axis + cell_width]) #South of a cell
             pygame.draw.line(display, white, [x_axis, y_axis + cell_width], [x_axis, y_axis]) #west of a cell
             frame.append((x_axis, y_axis)) #put a cell in the list making the frame
             x_axis = x_axis + 30 #move cells to a new point


def move_north(x_axis, y_axis):
    pygame.draw.rect(display, green, (x_axis + 1, y_axis-cell_width + 1, 29, 59), 0) #draw the rectangle
    pygame.display.update()
def move_east(x_axis, y_axis):
    pygame.draw.rect(display, green, (x_axis + 1, y_axis + cell_width + 1, 29, 59), 0) #draw the rectangle
    pygame.display.update()
def move_south(x_axis, y_axis):
    pygame.draw.rect(display, green, (x_axis - cell_width + 1, y_axis + 1, 59, 29), 0) #draw the rectangle
    pygame.display.update()
def move_west(x_axis, y_axis):
    pygame.draw.rect(display, green, (x_axis + 1, y_axis + 1, 59, 39), 0) #draw the rectangle
    pygame.display.update()





















#set up window and its sizes

width = 700
height = 800
framerater = 40

#




