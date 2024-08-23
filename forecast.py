import os
from dotenv import load_dotenv
import requests

# Load API key from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')

def get_user_input():
    while True:
        city_name = input("Enter a city name (or 'quit' to exit): ")
        if city_name.lower() == "quit":
            return None
        return city_name

def get_weather_data(city_name, api_key):
    try:
        # Retrieve weather data from API
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(base_url)
        weather_data = response.json()
        return weather_data
    except Exception as e:
        print(f"Error retrieving weather data: {e}")
        return None

def get_forecast_data(city_name, api_key):
    try:
        # Retrieve forecast data from API
        base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
        response = requests.get(base_url)
        forecast_data = response.json()
        return forecast_data
    except Exception as e:
        print(f"Error retrieving forecast data: {e}")
        return None

def print_weather_data(weather_data):
    print("\nCurrent Weather:")
    print(f"  Temperature: {round(weather_data['main']['temp'] - 273.15)} C")
    print(f"  Humidity: {weather_data['main']['humidity']} %")

def print_forecast(forecast_data):
    forecast_list = forecast_data["list"]
    for i in range(0, len(forecast_list), 8): 
        weather_info = forecast_list[i]
        print("\nForecast:")
        print(f"  Date: {weather_info['dt_txt']}")
        print(f"  Description: {weather_info['weather'][0]['description']}")

def main():
    api_key = API_KEY
    while True:
        city_name = get_user_input()
        if city_name is None:
            break
        weather_data = get_weather_data(city_name, api_key)
        if weather_data is not None:
            print_weather_data(weather_data)
            forecast_data = get_forecast_data(city_name, api_key)
            if forecast_data is not None:
                print_forecast(forecast_data)

if __name__ == "__main__":
    main()

