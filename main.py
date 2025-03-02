import requests
from datetime import datetime
import os
APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
SHEETS_URL = os.environ['SHEETS_URL']
TOKEN = os.environ['TOKEN']

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
query = input('Tell me which exercises you did: ')
exercise_params = {
    'query': query
}
response = requests.post(url=url, json=exercise_params, headers=headers)
data = response.json()
today = datetime.now()
exercise_data = data['exercises'][0]
date = today.strftime('%d/%m/%Y')
time = today.strftime('%X')
exercise = exercise_data['name'].title()
duration = exercise_data['duration_min']
calories = exercise_data['nf_calories']
sheety_headers = {
    'Authorization': TOKEN,
    'Content-Type': 'application/json'
}
workout = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': exercise,
        'duration': duration,
        'calories': calories
    }
}

response = requests.post(url=SHEETS_URL, json=workout, headers=sheety_headers)
result = response.json()
print(result)
