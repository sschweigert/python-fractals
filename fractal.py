from Tkinter import *
import math
from enum import Enum

class Side(Enum):
	left = 1
	right = 2

iteration_setting = 0
master = Tk()
canvas = Canvas(master, width=1500, height=900)
canvas.pack()

def triangle_iteration(side):
	angle = 0
	if side is Side.left:
		angle = math.pi / 4
	else:
		angle = -math.pi / 4
	def fcn(line_segment):
		properties = vector_properties(line_segment)

		new_angle = properties[0] + angle		
		new_length = properties[1] / math.sqrt(2)

		new_point = offset_point(line_segment[0], new_angle, new_length)
		return new_point
	return fcn

def next_button(event):
	global iteration_setting
	iteration_setting += 1
	create_drawing()

canvas.bind("<ButtonPress-1>", next_button)

def draw(line):
	global canvas
	canvas.delete(ALL)
	
	canvas.create_text(200, 80, text="Click the screen")
	
	previous = None
	for point in line:	
		if previous is not None:
			canvas.create_line(previous[0], previous[1], point[0], point[1])
		previous = point
	mainloop()

def create_drawing():
	global iteration_setting
	seed = [(500, 300), (800, 300)]
	points = dragon_fractal(seed, iteration_setting)
	draw(points)

def main():
	create_drawing()

def dragon_fractal(seed, iterations):
	for i in range(iterations):
		seed = dragon_iteration(seed)
	return seed

def dragon_iteration(seed):
	to_return = []
	
	functions = [ triangle_iteration(Side.left), triangle_iteration(Side.right)]	
	function_index = 0

	previous = None
	for point in seed:
		if previous is not None:
			line_segment = (previous, point)
			
			function = functions[function_index]
			new_point = function(line_segment)
			to_return.append(previous)
			to_return.append(new_point)
			
			function_index += 1
			if function_index == len(functions):
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
