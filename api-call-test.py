import requests

# Define the URL
url = "http://localhost:3000/api/getlines"

# Fetch data from the URL
response = requests.get(url)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Parse the JSON data
    json_data = response.json()

    # Print the values associated with the 'data' key
    if 'data' in json_data:
        for item in json_data['data']:
            print(item)
    else:
        print("The key 'data' is not present in the JSON data.")
else:
    print(f"Request failed! Status code: {response.status_code}")
