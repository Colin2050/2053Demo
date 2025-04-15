import car
list_of_cars = []
with open("cars.txt") as file:
    for line in file:
        info = line.strip().split()
        info[2] = int(info[2])
        info[3] = int(info[3])
        list_of_cars.append(car.Car(info[0],info[1],info[2],info[3]))
print(list_of_cars[0].get_gas_tank())
print(list_of_cars[0].get_odometer())
list_of_cars[0].drive()
print(list_of_cars[0].get_gas_tank())
print(list_of_cars[1].get_gas_tank())
print(list_of_cars[1].get_odometer())
list_of_cars[1].drive()
print(list_of_cars[1].get_gas_tank())