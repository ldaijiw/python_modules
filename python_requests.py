import requests

live_response = requests.get("https://www.bbc.co.uk/")

print(live_response.status_code)

if live_response.status_code == 200:
    print("Successful")
else:
    print("Something went wrong")