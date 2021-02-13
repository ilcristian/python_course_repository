import csv
import json
import os

path = './output_data/'
os.mkdir(path)

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

with open('./output_data/slow_cars.json', 'w') as json_slow_cars, \
        open('./output_data/fast_cars.json', 'w') as json_fast_cars, \
        open('./output_data/sport_cars.json', 'w') as json_sport_cars:

    slow_cars_file = json.dumps(slow_cars)
    json_slow_cars.write(slow_cars_file)

    fast_cars_file = json.dumps(fast_cars)
    json_fast_cars.write(fast_cars_file)

    sport_cars_file = json.dumps(sport_cars)
    json_sport_cars.write(sport_cars_file)


cheap_cars = [cheap for cheap in cars if int(cheap['price']) < 1000]
medium_cars = [medium for medium in cars if 1000 <= int(medium['price']) < 5000]
expensive_cars = [expensive for expensive in cars if int(expensive['price']) >= 5000]

with open('./output_data/cheap_cars.json', 'w') as json_cheap_cars, \
        open('./output_data/medium_cars.json', 'w') as json_medium_cars, \
        open('./output_data/expensive_cars.json', 'w') as json_expensive_cars:

    cheap_cars_file = json.dumps(cheap_cars)
    json_cheap_cars.write(cheap_cars_file)

    medium_cars_file = json.dumps(medium_cars)
    json_medium_cars.write(medium_cars_file)

    expensive_cars_file = json.dumps(expensive_cars)
    json_expensive_cars.write(expensive_cars_file)

car_list_set = set(set_value['brand'] for set_value in cars)

for unique_value in car_list_set:
    unique_value_list = [each_car for each_car in cars if each_car['brand'] == unique_value]
    with open(f'./output_data/{unique_value}.json', 'a') as json_each:
        json_each.write(json.dumps(unique_value_list))