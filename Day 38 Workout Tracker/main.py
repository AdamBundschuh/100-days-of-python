import requests
from datetime import datetime

APP_ID = "b112ed52"
API_KEY = "0c31a8113473be568440beb6dd451ebf"
SHEETY_KEY = "Bearer 349kdfa38fjf72h7fha7shad73jahf79ahsdf"
GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 178
AGE = 40

workout_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/d072de6e229f2ef33682abecc9cbe9ce/workoutTracking/workouts"

exercise_text = input("Tell me what exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

sheety_headers = {
    "Authentication": SHEETY_KEY,
    "Content-Type": "application/json"
}

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=workout_endpoint, json=exercise_params, headers=headers)
result = response.json()
print(result)

workout_list = [workout for workout in result['exercises']]
date = datetime.today().strftime("%d/%m/%Y")
time = datetime.now().strftime("%I:%M:%S %p")
exercise_num = 1

for workout in workout_list:
    exercise = workout['name'].title()
    user_input = workout['user_input']
    duration = workout['duration_min']
    calories = workout['nf_calories']

    workout_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    #print(f"EXERCISE {exercise_num}\nDate: {date} \nTime: {time} \nExercise: {exercise} ({user_input}) \nDuration: {duration} \nCalories: {calories}\n")
    #exercise_num += 1
    response = requests.post(url=sheety_endpoint, json=workout_params, headers=sheety_headers)
    print(response.text)
