import requests
import json
from bs4 import BeautifulSoup
import json

getModelUrl = "https://www.carbase.my/ism/ajax-get-"

with open('carMakeModel.json', 'r') as f:
    carMakeModel = json.load(f)  # Returns a list

def parsePayload(payload):
    soup = BeautifulSoup(payload, 'html.parser')
    next_value = soup.find_all('option')[1]['value']
    return next_value
    
    
def getParam(paramType, dynamicPayload):
    getParamUrl = getModelUrl + paramType if paramType != "variant" else getModelUrl + "generation"
    # print(getParamUrl)
    # print(dynamicPayload)
    response = requests.post(getParamUrl, data=dynamicPayload)
    if response.status_code == 200:
        # print(f"get {paramType} was successful!")
        val = parsePayload(response.content)
        dynamicPayload[paramType] = val
        # print(dynamicPayload)
        return val
    else:
        print(f"Request failed with status code {response.status_code}")
        return "default"
    
    
    
def constructPayload(make, model):
    dynamicPayload = {
        "make": make,
        "family": model,
    }
    getParam("year",dynamicPayload)
    getParam("engine-capacity",dynamicPayload)
    getParam("transmission",dynamicPayload)
    getParam("variant",dynamicPayload)
    # print(dynamicPayload)
    return dynamicPayload           

def parseResponseIntoCarPrice(response):
    carLatestPrice = response['wm_new_pr']
    return carLatestPrice

def getCarPrice(make, model):
    payload = constructPayload(make, model)
    print(payload)
    url = "https://www.carbase.my/ism/ajax-get-valuation-result"  # Replace with your actual endpoint
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        # print("Request was successful!")
        return response.json()["wm_new_pr"]  # or response.text if it's not JSON
    else:
        # print(f"Request failed with status code {response.status_code}")
        return None


print(f"RM"+getCarPrice("PROTON", "SAGA"))
# # Define the URL of the endpoint
# url = "https://www.carbase.my/ism/ajax-get-valuation-result"  # Replace with your actual endpoint

# # Define the payload (form data)
# payload = {
#     "make": "TOYOTA",
#     "family": "HARRIER",
#     "year": "2002",
#     "cc": "2163",
#     "transmission": "4 SP AUTO SPORTS MODE",
#     "variant": "10637"
# }

# # Send the POST request with form data
# response = requests.post(url, data=payload)

# # Check the status of the response
# if response.status_code == 200:
#     print("Request was successful!")
#     print("Response Data:", response.json())  # or response.text if it's not JSON
# else:
#     print(f"Request failed with status code {response.status_code}")
#     print("Response:", response.text)