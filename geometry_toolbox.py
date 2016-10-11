import math

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
