import requests

def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(url)
    data = response.json()
    return data

def get_temperature(data):
    temperature = data['hourly']['temperature_2m']
    return temperature

if __name__ == "__main__":
    weather_data = fetch_weather_data()
    temperature = get_temperature(weather_data)
    print("Hourly temperatures:", temperature)