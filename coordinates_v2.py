# Доработать граничные случаи
# !!! Координата совпадает с вершиной - как работаем?
# Разбор XML
# Разбор csv
# Перевод координат в десятичные
# Проверить точность на double
# 

def load_zone_coordinates():
	with open('zone1', 'r') as zone:
		zone1 = [] #green
		for string in zone:
			zone1.append([float(elem) for elem in string.split()])
	with open('zone2', 'r') as zone:
		zone2 = [] #yellow
		for string in zone:
			zone2.append([float(elem) for elem in string.split()])
	return zone1, zone2

def load_points_coordinates():
	with open('clients_coordinate', 'r') as clients_coordinates:
		coordinates = []
		for string in clients_coordinates:
#			coordinates.append([int(elem) for elem in string.split()])
			element = string.split()
			coordinates.append([element[0], float(element[2]), float(element[1])]) # Координаты в csv подаются в формате 55-37. Яндекс карты выдают в формате 37-55.
	return coordinates

def change_coordinates_to_cartesian(coordinates): #(wgs84)
	pass

def include_in_polygon(x, y, xp, yp):
   include = False
   for i in range(len(xp)):
       if (((yp[i] <= y < yp[i-1]) or (yp[i-1] <= y < yp[i])) and \
       	(x > (xp[i-1] - xp[i]) * (y - yp[i]) / (yp[i-1] - yp[i]) + xp[i])):
           include = not include    
   return include


if __name__ == '__main__':

	zone1, zone2 = load_zone_coordinates()
	#zone1, zone2 = load_zone_coordinates()
	points = load_points_coordinates()
	
	xp1 = []
	yp1 = []
	xp2 = []
	yp2 = []

	for pair in zone1:
		xp1.append(pair[0])
		yp1.append(pair[1])
	for pair in zone2:
		xp2.append(pair[0])
		yp2.append(pair[1])

	answer = []

	for point in points:
		answer_for_zone1 = include_in_polygon(point[1], point[2], xp1, yp1)
		answer_for_zone2 = include_in_polygon(point[1], point[2], xp2, yp2)
		if answer_for_zone1 is True:
			answer.append([point[0], 'Include in green zone'])
		elif answer_for_zone2 is True and answer_for_zone1 is False:
			answer.append([point[0], 'Include in yellow zone'])
		else:
			answer.append([point[0],'Not include'])

	for elem in answer: 
		print(elem)

