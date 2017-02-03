#import csv
import Colour

colourList = []

with open('RGBcolours.csv', 'rb') as csvfile:
	colourReader = read(csvfile, delimiter=',', quotechar='\n')
	for row in colourReader:
#		print ', '.join(row)
		colourList.append(Colour.Colour(int(row[0]),int(row[1]),int(row[2]),row[3]))

readColour = Colour.Colour(219,19,61)

smallestDistance = float('Inf')

for colour in colourList:
	distance = colour.calc_distance(readColour)
	if distance < smallestDistance:
		smallestDistance = distance
		closestColour = colour

print(closestColour.get_name())

