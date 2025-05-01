import requests

# Define the URL of the endpoint
url = "https://www.carbase.my/ism/ajax-get-year"  # Replace with your actual endpoint
# Define the payload (form data)
payload = {
    "make": "TOYOTA",
    "family": "HARRIER",
    # "year": "2002",
    # "cc": "2163",
    # "transmission": "4 SP AUTO SPORTS MODE",
    # "variant": "10637"
}

# Send the POST request with form data
response = requests.post(url, data=payload)

# Check the status of the response
if response.status_code == 200:
    print("Request was successful!")
    print("Response Data:", response.text)  # or response.text if it's not JSON
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response:", response.text)
