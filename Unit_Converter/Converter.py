import math
import time
import datetime


def weight(num, unit):
	result = 0
	'''
	1. kilograms
	2. grams
	'''
	while True:
		try:
			if unit == "1":
				result = num/1000
				break
			elif unit == "2":
				result = num*1000
				break
		except: 
			print("wrong unit, choose again!!")
			break
	return result

def distance(num, unit):
	'''
	1. kilometers
	2. meter
	'''
	result = 0
	while True:
		try:
			if unit == "1":
				result = num/1000
				break
			elif unit == "2":
				result = num*1000
				break
		except:
			print("Wrong unit, Choose again !!!")
			break
	return result

def timeconvert():
	current_time = time.ctime()
	#isoformat = time.ctime().isoformat()
	print("current_time:" , current_time)
	#print("ISO Format: ", isoformat)

def datetimeconvert():
	current_time = datetime.datetime.now()
	isoformat = datetime.datetime.now().isoformat()
	utc = datetime.datetime.utcnow().isoformat()
	print("current_time:" , current_time)
	print("ISO Format: ", isoformat)
	print("UTC Time:", utc)

def main():
	print("What time is it ? ")
	timeconvert()
	datetimeconvert()

	while True:
		try:
			converttype = input("Please input the convert type : ")
			if converttype == 'weight':
				number = int(input("Please input the weight number : "))
				unit = input("Please input the unit(1. kilograms , 2. grams): ")
				convertresult = weight(number, unit)
				print(convertresult)
				break
			elif converttype == 'distance':
				number = int(input("Please input the weight number : "))
				unit = str(input("Please input the unit(1. kilometer , 2. meter): "))
				converetresult = distance(number, unit)
				print(convertresult)
				break
		except:
			print("Sorry please input convert type weight or distance!!!")


if __name__ == '__main__':
	main()