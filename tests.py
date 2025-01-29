import requests
from datetime import datetime
import json

# Google Sheet URL (for my personal reference)
google_sheet = "https://docs.google.com/spreadsheets/d/1oDDURgmGxgKfSXErXk2IWqnYTMziTYnhAWsqgcaB4bw/edit?gid=0#gid=0"

# Nutritionix API website URL (for my personal reference)
website = "https://developer.nutritionix.com/admin/applications/1409625317829"
print(f"HERE IS WEBSITE-> {website}\n\n")

# User's personal details
GENDER = "male"
WEIGHT_KG = "110"
HEIGHT_CM = "170"
AGE = "34"

# Nutritionix API credentials
APPLICATION_ID = "29d2b6c3"
APPLICATION_KEY = "430667d2ca4195415ec6d6df517baaa4"
HOST_DOMAIN = "https://trackapi.nutritionix.com"
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Bearer token for Sheety API authentication
BEARER = "test123"

# Ask user for exercise details
exercise_text = input("Tell me which exercises you did: ")

# Set headers for Nutritionix API request
headers = {
    "Authorization": "Basic cnlkZXI6cGFzcw=="
}

# Set parameters for Nutritionix API request
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Send POST request to Nutritionix API
response = requests.post(ENDPOINT, json=parameters, headers=headers)
result = response.json()
print(f"\n\n{result}")

# Get current date and time
today = datetime.now()
today_date = today.strftime("%Y-%m-%d")
now_time = today.strftime("%H:%M")

# Extract exercise details from Nutritionix API response
exercises = result['exercises']
for i in exercises:
    exercise = i['user_input']
    duration = int(i['duration_min'])
    calories = i['nf_calories']

    # Set URL for Sheety API
    sheet_endpoint = 'https://api.sheety.co/0e9f1405a7dc8e492b85cdab00bdefc2/copyOfMyWorkouts/workouts'

    # Set body for Sheety API request
    sheet_inputs = {
        'workout': {
            "date": today_date,
            "time": now_time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    # Set headers for Sheety API request
    sheet_headers = {
        "Authorization": "Basic cnlkZXI6cGFzcw=="
    }

    # Send POST request to Sheety API
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=sheet_headers
    )

    # Check if response was successful
    if sheet_response.status_code == 200:
        json_data = sheet_response.json()
        print(json_data['workout'])
    else:
        print(f"Error: {sheet_response.status_code} - {sheet_response.text}")