import requests

API_ENDPOINT = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

data = {
    "UCID": "sj728",
    "first_name": "Shubhransh",
    "last_name": "Joshi",
    "github_username": "ShubhranshJoshi",
    "discord_username": "@guesswho3196",
    "favorite_cartoon": "Scooby Doo",
    "favorite_language": "Python",
    "movie_or_game_or_book": "Pandora Hearts",
    "section": "101" 
}

try:
    response = requests.post(API_ENDPOINT, json=data)
    if response.status_code == 200:
        print("Information submitted successfully!")
        print("Response:", response.json())
    else:
        print(f"❌ Failed to submit information. Status code: {response.status_code}")
        print("Response:", response.text)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)