from functools import reduce
import csv

with open("titanic.csv","r") as file:
	keys = file.readline()
	reader = csv.reader(file, delimiter=",")
	dataset = [x for x in reader]
keys = list(keys.split(","))

def to_dictionary(keys, values):
	dictionary = {}
	for i in range(len(keys)):
		dictionary[keys[i]] = values[i]
	return dictionary

dataset = list(map(lambda x: to_dictionary(keys, x), dataset))

age = list(map(lambda x: int(x['Amount']), dataset))
sum_of_age = reduce(lambda x, y: x + y, age)
average_age = round(sum_of_age / len(age), 2)

print("Sum of age:", sum_of_age,"\nCount of Assistance:",len(age),"\nAverage Assistance:", average_age)