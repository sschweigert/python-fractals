from Tkinter import *
import math
from enum import Enum

class Side(Enum):
	left = 1
	right = 2

master = Tk()
canvas = Canvas(master, width=1500, height=900)
canvas.pack()
current_fractal = [(450, 600), (1050, 600)]
canvas.configure(background='white')
#cool_list = [ triangle_iteration(Side.right), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.left), triangle_iteration(Side.right)]
#alien_spiral = [triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.left)]
#fractal_mask = [trapazoid_iteration(Side.left), trapazoid_iteration(Side.right), trapazoid_iteration(Side.left)]
#dragon_curve = [triangle_iteration(Side.left), triangle_iteration(Side.right)]
#organic_tips = [triangle_iteration(Side.left), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.left), triangle_iteration(Side.right)]
#pine_cones = [triangle_iteration(Side.left), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.left), triangle_iteration(Side.left)]
#two_faced_spiral = [triangle_iteration(Side.right), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.left),  triangle_iteration(Side.right)]
#alien_network = [triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.right), triangle_iteration(Side.left)]
#rose_spiral = [triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.right), triangle_iteration(Side.right)]
#parallel_spiral = [triangle_iteration(Side.left), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.right)]
#complex_dragon = [triangle_iteration(Side.left), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.right)]

def trapazoid_iteration(side):
	first_angle = math.pi / 3
	second_angle = -2 * math.pi / 3
	if side is Side.left:
		first_angle = -first_angle
		second_angle = -second_angle
	def fcn(line_segment):
		properties = vector_properties(line_segment)	
		first_point_angle = properties[0] + first_angle
		first_point_length = properties[1] / 2
		first_new_point = offset_point(line_segment[0], first_point_angle, first_point_length)
		
		second_point_angle = properties[0]
		second_point_length = properties[1] / 2
		second_new_point = offset_point(first_new_point, second_point_angle, second_point_length)
		return [first_new_point, second_new_point]
	return fcn

def triangle_iteration(side):
	angle = math.pi / 4
	if side is Side.left:
		angle = -angle
	def fcn(line_segment):
		properties = vector_properties(line_segment)

		new_angle = properties[0] + angle		
		new_length = properties[1] / math.sqrt(2)

		new_point = offset_point(line_segment[0], new_angle, new_length)
		return [new_point]
	return fcn

def next_button(event):
	create_drawing()

canvas.bind("<ButtonPress-1>", next_button)

def draw(line):
	global canvas
	canvas.delete(ALL)
	
	#canvas.create_text(200, 80, text="Click the screen")
	
	previous = None
	for point in line:	
		if previous is not None:
			canvas.create_line(previous[0], previous[1], point[0], point[1], width=2)
		previous = point
	mainloop()

def create_drawing():
	global current_fractal 
	function_list = [triangle_iteration(Side.left), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.left), triangle_iteration(Side.right), triangle_iteration(Side.right)]
	current_fractal = line_fractal(current_fractal, function_list, 1)
	draw(current_fractal)

def main():
	global current_fractal
	draw(current_fractal)

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

def offset_point(base, angle, length):
	x = base[0] + length * math.cos(angle)			
	y = base[1] + length * math.sin(angle)			
	return (x, y)


def vector_properties(vector):
	(base, arrow_head) = vector
	x_diff = arrow_head[0] - base[0]
	y_diff = arrow_head[1] - base[1]	
	angle = math.atan2(y_diff, x_diff)
	length = math.hypot(x_diff, y_diff)
	return (angle, length)

if __name__ == "__main__":
	main()
