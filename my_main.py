# Import necessary libraries
import requests
from datetime import datetime
import json
import os
from dotenv import find_dotenv, load_dotenv

# Find.env automatically
dotenv_path = find_dotenv()

# Load the entries as environment variables
load_dotenv(dotenv_path)
APPLICATION_ID = os.getenv("APPLICATION_ID")
APPLICATION_KEY = os.getenv("APPLICATION_KEY")
BEARER = os.getenv("BEARER")
ENDPOINT = os.getenv("ENDPOINT")

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
APPLICATION_ID = APPLICATION_ID
APPLICATION_KEY = APPLICATION_KEY
HOST_DOMAIN = "https://trackapi.nutritionix.com"
ENDPOINT = ENDPOINT

# Bearer token for Sheety API authentication
BEARER = BEARER

# Ask user for exercise details
exercise_text = input("Tell me which exercises you did: ")

# Set headers for Nutritionix API request
headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_KEY,
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

# exercise = result['exercises'][0]['user_input']
# duration = result['exercises'][0]['duration_min']
# calories = result['exercises'][0]['nf_calories']

# Extract exercise details from Nutritionix API response
exercises = result['exercises']
for i in exercises:
    exercise = i['user_input']
    duration = int(i['duration_min'])
    calories = i['nf_calories']

    # Set URL for Sheety API
    url = 'https://api.sheety.co/0e9f1405a7dc8e492b85cdab00bdefc2/copyOfMyWorkouts/workouts'

    # Set body for Sheety API request
    body = {
        'workout': {
            "date": today_date,
            "time": now_time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    # Bearer Token Authentication
    bearer_headers = {
        "Authorization": f"Bearer {BEARER}"
    }


    # Send POST request to Sheety API
    response = requests.post(url, json=body, headers=bearer_headers)

    # Check if response was successful
    if response.status_code == 200:
        json_data = response.json()
        print(json_data['workout'])
    else:
        print(f"Error: {response.status_code}")
