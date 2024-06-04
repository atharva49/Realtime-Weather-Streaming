import requests
from kafka import KafkaProducer
import json
import time

API_KEY = "bd5e378503939ddaee76f12ad7a97608"
CITIES = ["London", "New York", "Tokyo", "Sydney", "Paris"]
KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER,
                         value_serializer = lambda v: json.dumps(v).encode('utf-8')
                         )

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def send_weather_data():
    for city in CITIES:
        weather_data = fetch_weather_data(city)
        producer.send("weather_data", weather_data)
        producer.send("humidity_data", {'city': city, 'humidity': weather_data['main']['humidity'], 'timestamp': weather_data['dt']})
        producer.send("temperature_data", {'city': city, 'temperature': weather_data['main']['temp'], 'timestamp': weather_data['dt']})
        producer.send("wind_speed_data", {'city': city, 'wind_speed': weather_data['wind']['speed'], 'timestamp': weather_data['dt']})
        producer.send("pressure_data", {'city': city, 'pressure': weather_data['main']['pressure'], 'timestamp': weather_data['dt']})
        print(f"Weather data sent for {city}: {weather_data}")

if __name__ == "__main__":
    while True:
        send_weather_data()
        time.sleep(60)