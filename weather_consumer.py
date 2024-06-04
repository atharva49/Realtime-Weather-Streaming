from kafka import KafkaConsumer
import json
from db_operations import DatabaseOperations

KAFKA_SERVER = "localhost:9092"

db_ops = DatabaseOperations(
    host="localhost",
    user="root",
    password="",
    database="weather_db"
)

def process_weather_messages():
    weather_consumer = KafkaConsumer("weather_data", bootstrap_servers=KAFKA_SERVER, value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in weather_consumer:
        weather_data = message.value
        print(f"Received weather data: {weather_data}")
        db_ops.store_weather_data(weather_data)

def process_humidity_messages():
    humidity_consumer = KafkaConsumer("humidity_data", bootstrap_servers=KAFKA_SERVER, value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in humidity_consumer:
        humidity_data = message.value
        print(f"Received humidity data: {humidity_data}")
        db_ops.store_humidity_data(humidity_data)

def process_temperature_messages():
    temperature_consumer = KafkaConsumer("temperature_data", bootstrap_servers=KAFKA_SERVER, value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in temperature_consumer:
        temperature_data = message.value
        print(f"Received temperature data: {temperature_data}")
        db_ops.store_temperature_data(temperature_data)

def process_wind_speed_messages():
    wind_speed_consumer = KafkaConsumer("wind_speed_data", bootstrap_servers=KAFKA_SERVER, value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in wind_speed_consumer:
        wind_speed_data = message.value
        print(f"Received wind speed data: {wind_speed_data}")
        db_ops.store_wind_speed_data(wind_speed_data)

def process_pressure_messages():
    pressure_consumer = KafkaConsumer("pressure_data", bootstrap_servers=KAFKA_SERVER, value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in pressure_consumer:
        pressure_data = message.value
        print(f"Received pressure data: {pressure_data}")
        db_ops.store_pressure_data(pressure_data)

if __name__ == "__main__":
    process_weather_messages()
    process_humidity_messages()
    process_temperature_messages()
    process_wind_speed_messages()
    process_pressure_messages()
    
    db_ops.close()
