import requests


def get_weather_desc_and_temp(url):
    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {
        "description": description,
        "temp_min": temp_min,
        "temp_max": temp_max,
    }


def print_weather(weather, city):
    print("The minimum temperature:", weather["temp_min"], "°C")
    print("Today's forecast for ", city, ": ", weather["description"], sep="")
    print("The maximum temperature:", weather["temp_max"], "°C")


def main():
    api_key = "97fae05da8217fb0a17edbfa0d250306"
    city = "Tbilisi"
    site = "https://api.openweathermap.org"
    url = f"{site}/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    weather = get_weather_desc_and_temp(url)
    print_weather(weather, city)


main()
