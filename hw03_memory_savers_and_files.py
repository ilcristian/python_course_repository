import csv
import json

header = ()
car_details = []

while True:
    filename = input('Enter a filename (enter \'q\' to exit): ')
    if filename == 'q':
        break
    else:
        try:
            with open(filename) as file:
                csv_data = csv.reader(file)
                for index, data in enumerate(csv_data):
                    if index == 0:
                        header = data
                    else:
                        car_details.append(data)
            break
        except FileNotFoundError:
            print('The file doesn\'t exist!')
            continue

cars = [{key: value for key, value in zip((head.strip() for head in header), (c.strip() for c in car))}
        for car in car_details]

slow_cars = [slow for slow in cars if int(slow['hp']) < 120]
fast_cars = [fast for fast in cars if 120 <= int(fast['hp']) < 180]
sport_cars = [sport for sport in cars if int(sport['hp']) >= 180]

with open('slow_cars.json', 'w') as json_slow_cars, \
        open('fast_cars.json', 'w') as json_fast_cars, \
        open('sport_cars.json', 'w') as json_sport_cars:

    slow_cars_file = json.dumps(slow_cars)
    json_slow_cars.write(slow_cars_file)

    fast_cars_file = json.dumps(fast_cars)
    json_fast_cars.write(fast_cars_file)

    sport_cars_file = json.dumps(sport_cars)
    json_sport_cars.write(sport_cars_file)


cheap_cars = [cheap for cheap in cars if int(cheap['price']) < 1000]
medium_cars = [medium for medium in cars if 1000 <= int(medium['price']) < 5000]
expensive_cars = [expensive for expensive in cars if int(expensive['price']) >= 5000]

with open('cheap_cars.json', 'w') as json_cheap_cars, \
        open('medium_cars.json', 'w') as json_medium_cars, \
        open('expensive_cars.json', 'w') as json_expensive_cars:

    cheap_cars_file = json.dumps(cheap_cars)
    json_cheap_cars.write(cheap_cars_file)

    medium_cars_file = json.dumps(medium_cars)
    json_medium_cars.write(medium_cars_file)

    expensive_cars_file = json.dumps(expensive_cars)
    json_expensive_cars.write(expensive_cars_file)


car_list_set = set()
for unique in cars:
    car_list_set.add(unique['brand'])

for unique_value in car_list_set:
    unique_value_list = []
    for each_car in cars:
        if each_car['brand'] == unique_value:
            unique_value_list.append(each_car)
    json_file = '{}.json'.format(unique_value)
    with open(json_file, 'a') as json_each:
        json_each.write(json.dumps(unique_value_list))