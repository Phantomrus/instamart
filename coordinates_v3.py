# Доработать граничные случаи
# !!! Координата совпадает с вершиной - как работаем?
# Разбор XML
# Разбор csv
# Сохранение в csv


#import pandas as pd


def load_zone_coordinates():
	with open('green_zone', 'r') as zone:
		green_zone = []
		for string in zone:
			green_zone.append([float(elem) for elem in string.split()])

	with open('yellow_zone', 'r') as zone:
		yellow_zone = []
		for string in zone:
			yellow_zone.append([float(elem) for elem in string.split()])

	return green_zone, yellow_zone


def load_orders_information():
	with open('clients_coordinate', 'r') as clients_coordinates:
		information = []
		for string in clients_coordinates:
			element = string.split()
			information.append([element[0], float(element[1]), float(element[3]), float(element[2])]) # Координаты в csv подаются в формате 55-37. Яндекс карты выдают в формате 37-55.
	
	return information


def include_in_polygon(x, y, xp, yp):
   include = False
   for i in range(len(xp)):
       if (((yp[i] <= y < yp[i-1]) or (yp[i-1] <= y < yp[i])) and \
       	(x > (xp[i-1] - xp[i]) * (y - yp[i]) / (yp[i-1] - yp[i]) + xp[i])):
           include = not include
   return include


def make_decision(orders_information,x_coordinates_green_zone, y_coordinates_green_zone, x_coordinates_yellow_zone, y_coordinates_yellow_zone):

	answer = []

	for point in orders_information:
		answer_for_green_zone = include_in_polygon(point[2], point[3], x_coordinates_green_zone, y_coordinates_green_zone)
		answer_for_yellow_zone = include_in_polygon(point[2], point[3], x_coordinates_yellow_zone, y_coordinates_yellow_zone)
		
		number_of_order = point[0]
		order_price = point[1]

		if answer_for_green_zone is True:
			decision = 'Yes'
			reason = 'Coordinates are included in green zone'
		elif (answer_for_yellow_zone is True) and (answer_for_green_zone is False) and (order_price >= 5000):
			decision = 'Yes'
			reason = 'Coordinates are included in yellow zone and price more than 5k'
		else:
			decision = 'No'
			reason = 'Coordinates are not included in zones or price less than 5k'
		
		answer.append([number_of_order, decision, reason])

	return answer


def load_from_csv():
	pass


#def save_to_csv(data_for_saving):
#	my_df = pd.DataFrame(data_for_saving)
#	my_df.to_csv('address_checked.csv', index = False, header = False)


if __name__ == '__main__':

	green_zone, yellow_zone = load_zone_coordinates()
	
	# Можно создать массив из этих четырех массивов

	x_coordinates_green_zone = []
	y_coordinates_green_zone = []
	x_coordinates_yellow_zone = []
	y_coordinates_yellow_zone = []

	for pair in green_zone:
		x_coordinates_green_zone.append(pair[0])
		y_coordinates_green_zone.append(pair[1])
	for pair in yellow_zone:
		x_coordinates_yellow_zone.append(pair[0])
		y_coordinates_yellow_zone.append(pair[1])


	orders_information = load_orders_information()
	answer = make_decision(orders_information,x_coordinates_green_zone, y_coordinates_green_zone, x_coordinates_yellow_zone, y_coordinates_yellow_zone)


#	save_to_csv(answer)

	for elem in answer: 
		print(elem)
