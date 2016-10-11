from geometry_toolbox import *
from side import Side
import math

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

def middle_triangle(side):
	angle = math.pi / 3
	if side is Side.left:
		angle = -angle
	def fcn(line_segment):
		properties = vector_properties(line_segment)	
		new_length = properties[1] / 3
		first_point = offset_point(line_segment[0], properties[0], new_length)
		second_point = offset_point(first_point, properties[0] + angle, new_length)
		third_point = offset_point(line_segment[0], properties[0], new_length * 2)
		return [first_point, second_point, third_point]
	return fcn
