# -*- coding: utf-8 -*-
'''
Author : Leo
API Resource : https://data.gov.tw/dataset/31897
資料來源：
1. 中央銀行。
2. 勞動部OAS標準之API說明文件：https://apiservice.mol.gov.tw/OdService/doc/v3.json。 
3. 勞動部開放資料Open API 頁面：https://apiservice.mol.gov.tw/OdService/openapi/OAS.html。
Licenses: https://data.gov.tw/licenses
'''

import os,sys
import math
import requests
import datetime


def compare_datetime(month): 
	'''
	Compare Month，Find the closest month
	'''
	global current_month 
	current_month = datetime.date.today() # Display currently month
	temp_year = int(month.split('-')[0])
	temp_month = int(month.split('-')[1])
	data_month = datetime.date(temp_year, temp_month, 1)
	interval = (current_month - data_month).days
	#print(interval)
	return interval

def compare_interval(num1, num2):
	'''
	Compare the size of time gap between the current time and the time in the data
	Find the smallest one
	'''
	result = num1 = num2
	if result > 0 :
		return num2
	else:
		return num1


def parse_json(currency): 
	'''
	Parsing the OpenData which response from API
	'''
	currency_data_size = len(currency)
	temp__save_list = []
	global currency_rate_list
	for item in currency:
		item_size = len(item)
		month_interval = compare_datetime(item['月別']) # Find the rate which is closest month 
		temp__save_list.append(month_interval) # Temporarily save the month result of compare 

		if len(temp__save_list)>1: # Make Sure that won't more than 2 values in the temp list 
			result = compare_interval(temp__save_list[0],temp__save_list[1])
			if result == temp__save_list[0]:
				temp__save_list.remove(temp__save_list[1])
			else:
				temp__save_list.remove(temp__save_list[0])
		else:
			continue	

	Selected = (current_month - datetime.timedelta(days=temp__save_list[0])).strftime("%Y-%m")
	#print(Selected)

	# Create dictionary for the rate
	for item in currency:
		if item['月別'] == Selected:
			currency_rate_list = {'TWD': item['新台幣'], 'RMB': item['人民幣'], 'JP': item['日圓'],\
			 'KRW': item['韓元'], 'SGD': item['新加坡元'], 'EU': item['歐元'], 'GBP': item['英鎊'], 'AUD': item['澳幣']}
			print(currency_rate_list)
	
	#return currency_rate_list


def converter(currency_1, currency_2, num):
	'''
	Exchange rate convert
	'''
	# Declare 
	result = 0.0
	Taiwan = float(currency_rate_list['TWD'])
	China = float(currency_rate_list['RMB'])
	Japan = float(currency_rate_list['JP'])
	Korea = float(currency_rate_list['KRW'])
	Singapore = float(currency_rate_list['SGD'])
	Europ = float(currency_rate_list['EU'])
	England = float(currency_rate_list['GBP'])
	Australia = float(currency_rate_list['AUD'])

	try:
		'''
		USD to TWD/RMB/JP/KRW/SGD/EU/GBP/AUD
		'''
		if currency_1 == 'USD':
			if currency_2 == 'TWD': 
				result = float('{:.3f}'.format(num*Taiwan))
			elif currency_2 == 'RMB':
				result = float('{:.3f}'.format(num*China))
			elif currency_2 == 'JP':
				result = float('{:.3f}'.format(num*Japan))
			elif currency_2 == 'KRW':
				result = float('{:.3f}'.format(num*Korea))
			elif currency_2 == 'SGD':
				result = float('{:.3f}'.format(num*Singapore))
			elif currency_2 == 'EU':
				result = float('{:.3f}'.format(num*Europ))
			elif currency_2 == 'GBP':
				result = float('{:.3f}'.format(num*England))
			elif currency_2 == 'AUD':
				result = float('{:.3f}'.format(num*Australia))
			else:
				valued = input_value()
				converter(valued[0], valued[1], valued[2])
		else:
			"ERROR 0: USD Convert Error"
		'''
		TWD to USD/RMB/JP/KRW/SGD/EU/GBP/AUD
		'''
		if currency_1 == 'TWD':
			if currency_2 == 'USD': 
				result = float('{:.3f}'.format(num/Taiwan))
				print('Result : {} {} '.format(result , currency_2))
			elif currency_2 == 'RMB':
				result = float('{:.3f}'.format((num/Taiwan)*China))
			elif currency_2 == 'JP':
				result = float('{:.3f}'.format((num/Taiwan)*Japan))
			elif currency_2 == 'KRW':
				result = float('{:.3f}'.format((num/Taiwan)*Korea))
			elif currency_2 == 'SGD':
				result = float('{:.3f}'.format((num/Taiwan)*Singapore))
			elif currency_2 == 'EU':
				result = float('{:.3f}'.format((num/Taiwan)*Europ))
			elif currency_2 == 'GBP':
				result = float('{:.3f}'.format((num/Taiwan)*England))
			elif currency_2 == 'AUD':
				result = float('{:.3f}'.format((num/Taiwan)*Australia))
			else:
				valued = input_value()
				converter(valued[0], valued[1], valued[2])
		else:
			"ERROR 1: TWD Convert Error"
		'''
		RMB to USD/TWD/JP/KRW/SGD/EU/GBP/AUD
		'''
		if currency_1 == 'RMB':
			if currency_2 == 'USD': 
				result = float('{:.3f}'.format(num/China))
			elif currency_2 == 'TWD':
				result = float('{:.3f}'.format((num/China)*Taiwan))
			elif currency_2 == 'JP':
				result = float('{:.3f}'.format((num/China)*Japan))
			elif currency_2 == 'KRW':
				result = float('{:.3f}'.format((num/China)*Korea))
			elif currency_2 == 'SGD':
				result = float('{:.3f}'.format((num/China)*Singapore))
			elif currency_2 == 'EU':
				result = float('{:.3f}'.format((num/China)*Europ))
			elif currency_2 == 'GBP':
				result = float('{:.3f}'.format((num/China)*England))
			elif currency_2 == 'AUD':
				result = float('{:.3f}'.format((num/China)*Australia))
			else:
				valued = input_value()
				converter(valued[0], valued[1], valued[2])
		else:
			"ERROR 1: TWD Convert Error"
		'''
		JP to USD/TWD/RMB/KRW/SGD/EU/GBP/AUD
		'''
		if currency_1 == 'JP':
			
			if currency_2 == 'USD': 
				result = float('{:.4f}'.format(num/Japan))
			elif currency_2 == 'RMB':
				result = float('{:.3f}'.format((num/Japan)*China))
			elif currency_2 == 'TWD':
				result = float('{:.3f}'.format((num/Japan)*Taiwan))
			elif currency_2 == 'KRW':
				result = float('{:.3f}'.format((num/Japan)*Korea))
			elif currency_2 == 'SGD':
				result = float('{:.5f}'.format((num/Japan)*Singapore))
			elif currency_2 == 'EU':
				result = float('{:.5f}'.format((num/Japan)*Europ))
			elif currency_2 == 'GBP':
				result = float('{:.5f}'.format((num/Japan)*England))
			elif currency_2 == 'AUD':
				result = float('{:.5f}'.format((num/Japan)*Australia))
			else:
				valued = input_value()
				converter(valued[0], valued[1], valued[2])
		else:
			"ERROR 1: TWD Convert Error"
		
		'''
		KRW to USD/TWD/JP/RMB/SGD/EU/GBP/AUD
		'''
		if currency_1 == 'KRW':
			if currency_2 == 'USD': 
				result = float('{:.5f}'.format(num/Korea))
			elif currency_2 == 'RMB':
				result = float('{:.3f}'.format((num/Korea)*China))
			elif currency_2 == 'JP':
				result = float('{:.3f}'.format((num/Korea)*Japan))
			elif currency_2 == 'TWD':
				result = float('{:.3f}'.format((num/Korea)*Taiwan))
			elif currency_2 == 'SGD':
				result = float('{:.5f}'.format((num/Korea)*Singapore))
			elif currency_2 == 'EU':
				result = float('{:.5f}'.format((num/Korea)*Europ))
			elif currency_2 == 'GBP':
				result = float('{:.5f}'.format((num/Korea)*England))
			elif currency_2 == 'AUD':
				result = float('{:.8f}'.format((num/Korea)*Australia))
			else:
				valued = input_value()
				converter(valued[0], valued[1], valued[2])
		else:
			"ERROR 1: TWD Convert Error"

		'''
		SGD to USD/TWD/JP/RMB/KRW/EU/GBP/AUD
		'''
		if currency_1 == 'SGD':
			if currency_2 == 'USD': 
				result = float('{:.3f}'.format(num/Singapore))
			elif currency_2 == 'RMB':
				result = float('{:.3f}'.format((num/Singapore)*China))
			elif currency_2 == 'JP':
				result = float('{:.3f}'.format((num/Singapore)*Japan))
			elif currency_2 == 'TWD':
				result = float('{:.3f}'.format((num/Singapore)*Taiwan))
			elif currency_2 == 'KRW':
				result = float('{:.3f}'.format((num/Singapore)*Korea))
			elif currency_2 == 'EU':
				result = float('{:.3f}'.format((num/Singapore)*Europ))
			elif currency_2 == 'GBP':
				result = float('{:.3f}'.format((num/Singapore)*England))
			elif currency_2 == 'AUD':
				result = float('{:.3f}'.format((num/Singapore)*Australia))
			else:
				valued = input_value()
				converter(valued[0], valued[1], valued[2])
		else:
			"ERROR 1: TWD Convert Error"
		'''
		EU to USD/TWD/JP/RMB/KRW/SGD/GBP/AUD
		'''
		if currency_1 == 'EU':
			if currency_2 == 'USD': 
				result = float('{:.3f}'.format(num/Europ))
			elif currency_2 == 'RMB':
				result = float('{:.3f}'.format((num/Europ)*China))
			elif currency_2 == 'JP':
				result = float('{:.3f}'.format((num/Europ)*Japan))
			elif currency_2 == 'TWD':
				result = float('{:.3f}'.format((num/Europ)*Taiwan))
			elif currency_2 == 'KRW':
				result = float('{:.3f}'.format((num/Europ)*Korea))
			elif currency_2 == 'SGD':
				result = float('{:.3f}'.format((num/Europ)*Singapore))
			elif currency_2 == 'GBP':
				result = float('{:.3f}'.format((num/Europ)*England))
			elif currency_2 == 'AUD':
				result = float('{:.3f}'.format((num/Europ)*Australia))
			else:
				valued = input_value()
				converter(valued[0], valued[1], valued[2])
		else:
			"ERROR 1: TWD Convert Error"
		'''
		GBP to USD/TWD/JP/RMB/KRW/EU/SGD/AUD
		'''
		if currency_1 == 'GBP':
			if currency_2 == 'USD': 
				result = float('{:.3f}'.format(num/England))
			elif currency_2 == 'RMB':
				result = float('{:.3f}'.format((num/England)*China))
			elif currency_2 == 'JP':
				result = float('{:.3f}'.format((num/England)*Japan))
			elif currency_2 == 'TWD':
				result = float('{:.3f}'.format((num/England)*Taiwan))
			elif currency_2 == 'KRW':
				result = float('{:.3f}'.format((num/England)*Korea))
			elif currency_2 == 'EU':
				result = float('{:.3f}'.format((num/England)*Europ))
			elif currency_2 == 'SGD':
				result = float('{:.3f}'.format((num/England)*Singapore))
			elif currency_2 == 'AUD':
				result = float('{:.3f}'.format((num/England)*Australia))
			else:
				valued = input_value()
				converter(valued[0], valued[1], valued[2])
		else:
			"ERROR 1: TWD Convert Error"
		'''
		AUD to USD/TWD/JP/RMB/KRW/EU/GBP/SGD
		'''
		if currency_1 == 'AUD':
			if currency_2 == 'USD': 
				result = float('{:.3f}'.format(num/Australia))
			elif currency_2 == 'RMB':
				result = float('{:.3f}'.format((num/Australia)*China))
			elif currency_2 == 'JP':
				result = float('{:.3f}'.format((num/Australia)*Japan))
			elif currency_2 == 'TWD':
				result = float('{:.3f}'.format((num/Australia)*Taiwan))
			elif currency_2 == 'KRW':
				result = float('{:.3f}'.format((num/Australia)*Korea))
			elif currency_2 == 'EU':
				result = float('{:.3f}'.format((num/Australia)*Europ))
			elif currency_2 == 'GBP':
				result = float('{:.3f}'.format((num/Australia)*England))
			elif currency_2 == 'SGD':
				result = float('{:.3f}'.format((num/Australia)*Singapore))
			else:
				valued = input_value()
				converter(valued[0], valued[1], valued[2])
		else:
			"ERROR 1: TWD Convert Error"

	except Exception as e:
		print('ERROR: ' , e)

	return result
	
	
def input_value():
	convert = input('請輸入要被轉換到的幣別是:')
	number = float(input('請輸入要轉換的金額:'))
	be_convert = input('請輸入要轉換成的幣別是:')
	valued =[convert, be_convert, number]
	return valued


def main():
	global valued
	r=requests.get('https://apiservice.mol.gov.tw/OdService/download/A17030000J-000049-KRC', verify=False)
	currency_data=r.json() # API Response(JSON Data) 
	parse_json(currency_data)
	#print(currency_list)
	print("Can be convert currency : 1. USD, 2. TWD, 3. RMB, 4. JP, 5. KRW, 6. SGD, 7. EU, 8. GBP, 9. AUD !!")
	valued = input_value()
	result = converter(valued[0], valued[1], valued[2])
	print('Result : {} {} '.format(result , valued[1]))
	


if __name__ == '__main__':
	main()