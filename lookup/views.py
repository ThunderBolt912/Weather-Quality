from django.shortcuts import render

def home(request):
	import json
	import requests
	
	if request.method == 'POST':
		zipcode = request.POST['zipcode']
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=10&API_KEY=9A5B0BC1-DBDB-4EE1-B259-052D7A777E16")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error ..."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0 - 50) Air quality is considered satisfactory, and air " \
									"pollution poses little or no risk."
			category_color = "good"
			category_description2 = category_description
			category_color2 = category_color

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = """(51-100) Air quality is acceptable, however,
			for some pollutants there may be a moderate health concern for a very
			small number of people who are unusually sensitive to air pollution."""
			category_color = "moderate"
			category_description2 = category_description
			category_color2 = category_color

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = """(101 - 150) Although the general public is not likely to be affected at this AQI range,
			people with lung disease, older adults, and children are at a greater risk from exposure to ozone,
			whereas persons with heart and lung disease, 
			older adults, and children are at greater risk from the presence of particles in the air."""
			category_color = "usg"
			category_description2 = category_description
			category_color2 = category_color

		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = """(151 - 200) Everyone may begin to experience health effects,
			members of sensitive groups may experience more serious health effects."""
			category_color = "unhealthy"
			category_description2 = category_description
			category_color2 = category_color

		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
			category_color = "veryunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = """(301 - 500) Health warnings of emergency conditions. 
			The entire population is more likely to be affected."""
			category_color = "hazardous"
			
			
		if api[1]['Category']['Name'] == "Good":
			category_descr = "(0 - 50) Air quality is considered satisfactory, and air " \
									"pollution poses little or no risk."
			category_colr = "good"
		
		elif api[1]['Category']['Name'] == "Moderate":
			category_descr = """(51-100) Air quality is acceptable, however,
			for some pollutants there may be a moderate health concern for a very
			small number of people who are unusually sensitive to air pollution."""
			category_colr = "moderate"
		
		elif api[1]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_descr = """(101 - 150) Although the general public is not likely to be affected at this AQI range,
			people with lung disease, older adults, and children are at a greater risk from exposure to ozone,
			whereas persons with heart and lung disease, 
			older adults, and children are at greater risk from the presence of particles in the air."""
			category_colr = "usg"
			
		elif api[1]['Category']['Name'] == "Unhealthy":
			category_descr = """(151 - 200) Everyone may begin to experience health effects,
			members of sensitive groups may experience more serious health effects."""
			category_colr = "unhealthy"
			
		elif api[1]['Category']['Name'] == "Very Unhealthy":
			category_descr = "(201 - 300) Health alert: everyone may experience more serious health effects."
			category_colr = "veryunhealthy"
			
		elif api[1]['Category']['Name'] == "Hazardous":
			category_descr = """(301 - 500) Health warnings of emergency conditions. 
			The entire population is more likely to be affected."""
			category_colr = "hazardous"




		return render(request, 'home.html', {
			'api': api,
			'category_description': category_description,
			'category_color': category_color,
			'category_descr' : category_descr,
			'category_colr' : category_colr,
			
		})


	else:
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=08831&distance=10&API_KEY=9A5B0BC1-DBDB-4EE1-B259-052D7A777E16")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error ..."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0 - 50) Air quality is considered satisfactory, and air " \
									"pollution poses little or no risk."
			category_color = "good"
			category_description2 = category_description
			category_color2 = category_color

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = """(51-100) Air quality is acceptable, however,
			for some pollutants there may be a moderate health concern for a very
			small number of people who are unusually sensitive to air pollution."""
			category_color = "moderate"
			category_description2 = category_description
			category_color2 = category_color

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = """(101 - 150) Although the general public is not likely to be affected at this AQI range,
			people with lung disease, older adults, and children are at a greater risk from exposure to ozone,
			whereas persons with heart and lung disease, 
			older adults, and children are at greater risk from the presence of particles in the air."""
			category_color = "usg"
			category_description2 = category_description
			category_color2 = category_color

		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = """(151 - 200) Everyone may begin to experience health effects,
			members of sensitive groups may experience more serious health effects."""
			category_color = "unhealthy"
			category_description2 = category_description
			category_color2 = category_color

		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
			category_color = "veryunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = """(301 - 500) Health warnings of emergency conditions. 
			The entire population is more likely to be affected."""
			category_color = "hazardous"
			
			
		if api[1]['Category']['Name'] == "Good":
			category_descr = "(0 - 50) Air quality is considered satisfactory, and air " \
									"pollution poses little or no risk."
			category_colr = "good"
		
		elif api[1]['Category']['Name'] == "Moderate":
			category_descr = """(51-100) Air quality is acceptable, however,
			for some pollutants there may be a moderate health concern for a very
			small number of people who are unusually sensitive to air pollution."""
			category_colr = "moderate"
		
		elif api[1]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_descr = """(101 - 150) Although the general public is not likely to be affected at this AQI range,
			people with lung disease, older adults, and children are at a greater risk from exposure to ozone,
			whereas persons with heart and lung disease, 
			older adults, and children are at greater risk from the presence of particles in the air."""
			category_colr = "usg"
			
		elif api[1]['Category']['Name'] == "Unhealthy":
			category_descr = """(151 - 200) Everyone may begin to experience health effects,
			members of sensitive groups may experience more serious health effects."""
			category_colr = "unhealthy"
			
		elif api[1]['Category']['Name'] == "Very Unhealthy":
			category_descr = "(201 - 300) Health alert: everyone may experience more serious health effects."
			category_colr = "veryunhealthy"
			
		elif api[1]['Category']['Name'] == "Hazardous":
			category_descr = """(301 - 500) Health warnings of emergency conditions. 
			The entire population is more likely to be affected."""
			category_colr = "hazardous"




		return render(request, 'home.html', {
			'api': api,
			'category_description': category_description,
			'category_color': category_color,
			'category_descr' : category_descr,
			'category_colr' : category_colr,
			
		})

def about(request):
	return render(request, 'about.html', {})
