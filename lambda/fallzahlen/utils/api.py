import requests


def get_germany_data():
	response = requests.get(url='https://api.corona-zahlen.org/germany')
	return response.json()

def get_state_data(state_key):
	response = requests.get(url=f'https://api.corona-zahlen.org/states/{state_key}')
	return response.json()['data'][state_key]

def get_district_data(district_key):
	response = requests.get(url=f'https://api.corona-zahlen.org/districts/{district_key}')
	return response.json()['data'][district_key]
	