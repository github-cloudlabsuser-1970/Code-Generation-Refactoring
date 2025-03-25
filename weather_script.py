import requests

def fetch_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }
        return weather
    else:
        return {"error": f"Failed to fetch weather data. HTTP Status Code: {response.status_code}"}

if __name__ == "__main__":
    API_KEY = "5117148899815e2e491ceb01b56ab2f6"  # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")
    weather_data = fetch_weather(city, API_KEY)
    
    if "error" in weather_data:
        print(weather_data["error"])
    else:
        print(f"Weather in {weather_data['city']}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Description: {weather_data['description']}")
        print(f"Humidity: {weather_data['humidity']}%")