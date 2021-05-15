# By CHIBUZO IYIOKE

#Here I'm writting a program to silulate live data gotten from a sensor. 
#The generated values are printed to the console and stored as a .csv file

import csv
import random
import time

time_value = 0
Sensor1_start_value = 72 
Sensor2_start_value = 70 
Sensor3_start_value = 75
Sensor4_start_value = 69

fieldnames = ['TIME','SENSOR 1','SENSOR 2','SENSOR 3','SENSOR 4']

with open('Simulated_Sensor_Data.csv', 'w') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	csv_writer.writeheader()

while True:
	with open('Simulated_Sensor_Data.csv', 'a') as csv_file:
		csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

		info={
		'TIME': time_value,
		'SENSOR 1':Sensor1_start_value,
		'SENSOR 2':Sensor2_start_value,
		'SENSOR 3':Sensor3_start_value,
		'SENSOR 4':Sensor4_start_value

		}

		csv_writer.writerow(info)
		print(time_value, Sensor1_start_value, Sensor2_start_value, Sensor3_start_value,  Sensor4_start_value)

		time_value += 1
		Sensor1_start_value = Sensor1_start_value + random.randint(-1, 2)
		Sensor2_start_value = Sensor2_start_value + random.randint(-2, 3)
		Sensor3_start_value = Sensor3_start_value + random.randint(-1, 3)
		Sensor4_start_value = Sensor4_start_value + random.randint(-3, 4)



	time.sleep(1)
