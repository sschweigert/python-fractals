from side import Side
from line_functions import *
from Tkinter import *
import math
import time


master = Tk()
canvas = Canvas(master, width=1500, height=900)
canvas.pack(fill=BOTH, expand=YES)
current_fractal = [(750, 700), (1450, 700)]
canvas.configure(background='white')
cool_list = [ triangle_iteration(Side.right), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.left), triangle_iteration(Side.right)]
alien_spiral = [triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.left)]
fractal_mask = [trapazoid_iteration(Side.left), trapazoid_iteration(Side.right), trapazoid_iteration(Side.left)]
dragon_curve = [triangle_iteration(Side.left), triangle_iteration(Side.right)]
new_dragon_curve = [new_triangle_iteration(Side.left), new_triangle_iteration(Side.right)]
organic_tips = [triangle_iteration(Side.left), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.left), triangle_iteration(Side.right)]
pine_cones = [triangle_iteration(Side.left), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.left), triangle_iteration(Side.left)]
two_faced_spiral = [triangle_iteration(Side.right), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.left),  triangle_iteration(Side.right)]
alien_network = [triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.right), triangle_iteration(Side.left)]
rose_spiral = [triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.right), triangle_iteration(Side.right)]
parallel_spiral = [triangle_iteration(Side.left), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.right)]
complex_dragon = [triangle_iteration(Side.left), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.right)]
von_koch_snowflake = [middle_triangle(Side.left)]
stacked_bears = [ middle_triangle(Side.left), middle_triangle(Side.right), middle_triangle(Side.right), middle_triangle(Side.left) ]

function_list = new_dragon_curve

def next_button():
	iterate_fractal()
	draw_fractal()

#canvas.bind("<ButtonPress-1>", next_button)

def draw(line):
	global canvas
	canvas.delete(ALL)
	button1 = Button(master, text="test", command=next_button, anchor='w', width =10)
	window = canvas.create_window(10, 10, anchor='nw', window=button1)
	
	#canvas.create_text(200, 80, text="Click the screen")
	
	previous = None
	for point in line:	
		if previous is not None:
			canvas.create_line(previous[0], previous[1], point[0], point[1], width=1)
		previous = point

def time_wrapper(function, text):
	start = time.time()
	function()	
	print text + " elapsed in " + str(time.time() - start)

def iterate_fractal():
	global current_fractal
	global function_list
	current_fractal = line_fractal(current_fractal, function_list, 1)

def draw_fractal():
	draw(current_fractal)

def main():
	global current_fractal
	draw(current_fractal)
	mainloop()

def line_fractal(seed, function_list, num_iterations=1):
	for i in range(num_iterations):
		seed = line_fractal_iteration(seed, function_list)
	return seed

def line_fractal_iteration(seed, function_list):
	to_return = []
	
	function_index = 0

	previous = None
	for point in seed:
		if previous is not None:
			line_segment = (previous, point)
			
			function = function_list[function_index]
			new_points = function(line_segment)
			to_return.append(previous)
			to_return.extend(new_points)
			
			function_index += 1
			if function_index == len(function_list):
				function_index = 0

		previous = point

	to_return.append(seed[-1])
	return to_return

if __name__ == "__main__":
	main()
