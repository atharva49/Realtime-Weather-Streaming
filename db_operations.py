import mysql.connector

class DatabaseOperations:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def store_weather_data(self, data):
        city = data['name']
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        timestamp = data['dt']

        try:
            self.cursor.execute("""
                INSERT INTO weather (city, description, temperature, humidity, wind_speed, pressure, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, FROM_UNIXTIME(%s))
            """, (city, description, temperature, humidity, wind_speed, pressure, timestamp))
            self.connection.commit()
            print(f"Weather data stored: {data}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    def store_humidity_data(self, data):
        city = data['city']
        humidity = data['humidity']
        timestamp = data['timestamp']

        try:
            self.cursor.execute("""
                INSERT INTO humidity (city, humidity, timestamp)
                VALUES (%s, %s, FROM_UNIXTIME(%s))
            """, (city, humidity, timestamp))
            self.connection.commit()
            print(f"Humidity data stored: {data}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    def store_temperature_data(self, data):
        city = data['city']
        temperature = data['temperature']
        timestamp = data['timestamp']

        try:
            self.cursor.execute("""
                INSERT INTO temperature (city, temperature, timestamp)
                VALUES (%s, %s, FROM_UNIXTIME(%s))
            """, (city, temperature, timestamp))
            self.connection.commit()
            print(f"Temperature data stored: {data}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    def store_wind_speed_data(self, data):
        city = data['city']
        wind_speed = data['wind_speed']
        timestamp = data['timestamp']

        try:
            self.cursor.execute("""
                INSERT INTO wind_speed (city, wind_speed, timestamp)
                VALUES (%s, %s, FROM_UNIXTIME(%s))
            """, (city, wind_speed, timestamp))
            self.connection.commit()
            print(f"Wind speed data stored: {data}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    def store_pressure_data(self, data):
        city = data['city']
        pressure = data['pressure']
        timestamp = data['timestamp']

        try:
            self.cursor.execute("""
                INSERT INTO pressure (city, pressure, timestamp)
                VALUES (%s, %s, FROM_UNIXTIME(%s))
            """, (city, pressure, timestamp))
            self.connection.commit()
            print(f"Pressure data stored: {data}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    def close(self):
        self.cursor.close()
        self.connection.close()
