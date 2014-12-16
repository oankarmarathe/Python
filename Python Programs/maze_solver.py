import types
import random

ROWS = 3
COLS = 3
BLOCK_FILL_PERCENTAGE = float(0.20)

def generate_random_xy():
	return random.randint(0, ROWS-1), random.randint(0, COLS-1)

def is_valid_maze(maze):
	has_start = False
	has_end = False

	for row in maze:
		for cell in row:
			if cell == "1":
				has_start = True
				continue
			if cell == "2":
				has_end = True
	return has_start and has_end

def generate_maze():
	maze = []

	#Generate empty maze
	for i in range(ROWS):
		current_row = []
		for j in range(COLS):
			current_row.append("0")
		maze.append(current_row)	

	#Fill maze with blocks
	TOTAL_BLOCK_FILL = int(ROWS * COLS * BLOCK_FILL_PERCENTAGE)
	for i in range(TOTAL_BLOCK_FILL):
		x,y = generate_random_xy()
		maze[x][y] = "-1"

	#Put random start position
	start_x, start_y = generate_random_xy()
	maze[start_x][start_y] = "1"

	#Put random end position
	end_x, end_y = generate_random_xy()
	maze[end_x][end_y] = "2"

	if is_valid_maze(maze):
		return maze
	else:
		generate_maze()

def get_cords(maze, cell_value):
	for i in range(ROWS):
		for j in range(COLS):
			if maze[i][j] == cell_value:
				return i,j

def gen_child_state(maze):
	print "Calling gen child state"
	child_states = []
	current_x, current_y = get_cords(maze, "1")

	#Check if valid up action is possible
	new_x = current_x
	new_y = current_y - 1
	print current_x
	print current_y
	print new_x
	print new_y
	if new_y >=0 and maze[new_x][new_y] == "0":
		print "Generate new UP state"
		current_child_state = list(maze)
		current_child_state[new_x][new_y] = "1"
		current_child_state[current_x][current_y] = "0"
		child_states.append(current_child_state)
		print current_child_state

	#Check if valid right action is possible
	new_x = current_x + 1
	new_y = current_y
	if new_x <=ROWS-1 and maze[new_x][new_y] == "0":
		print "Generate new RIGHT state"
		current_child_state = list(maze)
		current_child_state[new_x][new_y] = "1"
		current_child_state[current_x][current_y] = "0"
		child_states.append(current_child_state)
		print current_child_state
	return child_states
def print_maze(maze):
	if isinstance(maze, types.NoneType):
		return
	for row in maze:
		print "\t".join(row)

if __name__ == "__main__":
	maze = generate_maze()
	print_maze(maze)
	child_states = gen_child_state(maze)
	print "\n\nChild States:\n\n"
	for child_state in child_states:
		print_maze(child_state)
		print "***\n\n"