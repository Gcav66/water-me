from credentials import API_KEY
import requests

def build_url(mylat, mylong):
	mylat = str(mylat)
	mylong = str(mylat)
	url ="https://api.weather.com/v1/geocode/"+mylat+"/"+mylong+"/forecast/daily/10day.json?language=en-US&units=e&apiKey="+API_KEY
	return url

test_url = build_url(5.6, -0.19)
print test_url

def get_forecast(url):
	myForecasts = []
	response = requests.get(url)
	results = response.json()
	for result in results['forecasts'][1:]:
		row = {}
		row['date'] = result['fcst_valid_local'].split("T")[0]
		row['day_precip'] = int(result['day']['pop'])
		row['night_precip'] = int(result['night']['pop'])
		if row['day_precip'] <=50 and row['night_precip'] <= 50:
			row['action'] = 'Irrigate'
		else:
			row['action'] = 'Do not irrigate'
		myForecasts.append(row)
	return myForecasts

def get_action(mylat, mylong):
	url = build_url(mylat, mylong)
	myForecast = get_forecast(url)
	return myForecast

test_action = get_action(5.6, -0.19)
print test_action







