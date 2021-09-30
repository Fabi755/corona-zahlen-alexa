from dataclasses import dataclass
import requests


@dataclass
class LocationInfo:
    state: str
    district: str


def get_location_info(post_code):
	# TODO: remove api key to prevent external usage after github publishing
	response = requests.get(url=f'https://maps.googleapis.com/maps/api/geocode/json?address={post_code}%20Deutschland&key=AIzaSyCtlw309ZImOVZFcbwhg0fXjrNnhtV_2Cg&language=de')
	json = response.json()
	print(json) # TODO: remove logs, if exception handling was added

	# TODO: check if json response have success schema
	states = list(filter(lambda c: 'administrative_area_level_1' in c['types'], json['results'][0]['address_components']))
	print(states) # TODO: remove log, if exception handling was added
	districts = list(filter(lambda c: 'administrative_area_level_3' in c['types'], json['results'][0]['address_components']))
	print(districts) # TODO: remove log, if exception handling was added
	countries = list(filter(lambda c: 'locality' in c['types'], json['results'][0]['address_components']))

	final_district = districts[0] if districts else countries[0]
	return LocationInfo(state=states[0]['long_name'], district=final_district['long_name'])
