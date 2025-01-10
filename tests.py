import requests
from datetime import datetime
import json

google_sheet = "https://docs.google.com/spreadsheets/d/1oDDURgmGxgKfSXErXk2IWqnYTMziTYnhAWsqgcaB4bw/edit?gid=0#gid=0"

website = "https://developer.nutritionix.com/admin/applications/1409625317829"
print(f"HERE IS WEBSITE-> {website}\n\n")

GENDER = "male"
WEIGHT_KG = "110"
HEIGHT_CM = "170"
AGE = "34"

APPLICATION_ID = "29d2b6c3"
APPLICATION_KEY = "430667d2ca4195415ec6d6df517baaa4"
HOST_DOMAIN = "https://trackapi.nutritionix.com"
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(ENDPOINT, json=parameters, headers=headers)
result = response.json()
print(result)

# Date stuff-----
today = datetime.now()
today_date = today.strftime("%Y-%m-%d")
now_time = today.strftime("%H")

# exercise = result['exercises'][0]['user_input']
# duration = result['exercises'][0]['duration_min']
# calories = result['exercises'][0]['nf_calories']

sheet_endpoint = 'https://api.sheety.co/0e9f1405a7dc8e492b85cdab00bdefc2/copyOfMyWorkouts/workouts'
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
