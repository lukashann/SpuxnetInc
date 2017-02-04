from Colour import Colour

def closestColour(readColour):
	file = open('RGBcolours.csv', 'r')
	num_lines = sum(1 for line in file)
	file.seek(0)

	smallestDistance = float('Inf')

	for i in range(0, num_lines):
		elements = file.readline().split(',')
		temp = Colour(elements[3], int(elements[0]), int(elements[1]), int(elements[2]))
		distance = temp.calc_distance(readColour)
		if distance < smallestDistance:
			smallestDistance = distance
			closest = temp

	return closest.get_name()
