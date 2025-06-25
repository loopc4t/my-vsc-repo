import requests


url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Parse HTML result
    print("Here's a random joke for you:")
    print(f"{data['setup']}")
    print(f"{data['punchline']}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
