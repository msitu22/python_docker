import requests

def call_url_with_zip_code(city_name):
    # URL for the server
    server_url = "http://127.0.0.1:5000/" + city_name
    
    # Making the API call to the server
    response = requests.get(server_url)

    d = response.json()
    
    print(d)


city_name = input("Enter a city name: ")
call_url_with_zip_code(city_name)
