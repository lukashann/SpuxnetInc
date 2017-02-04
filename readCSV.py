import csv
import Colour

colourList = []

with open('RGBcolours.csv', 'rb') as csvfile:
	colourReader = csv.reader(csvfile, delimiter=',', quotechar='\n')
	for row in colourReader:
#		print ', '.join(row)
		colourList.append(Colour.Colour(int(row[0]),int(row[1]),int(row[2]),row[3]))

for colour in colourList:
	print "name: %s, red: %d" % (colour.name, colour.get_red())


