# Realtime-Weather-Streaming

This project demonstrates a real-time data pipeline to collect, process, and store weather data using Kafka, MySQL, and Python. It fetches weather data from the OpenWeatherMap API for multiple cities, processes it using Kafka, and stores it in a MySQL database. Additionally, it uses Airflow to schedule the producer and consumer scripts.

## Table of Contents

- [Introduction](#introduction)
- [Components](#components)
  - [Kafka](#kafka)
  - [MySQL](#mysql)
  - [Airflow](#airflow)
  - [OpenWeatherMap API](#openweathermap-api)
- [Project Structure](#project-structure)
- [Scripts](#scripts)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is designed to show how real-time data pipelines work using Kafka, MySQL, and Airflow. The pipeline fetches weather data from the OpenWeatherMap API for multiple cities, processes the data through Kafka, and stores it in a MySQL database. Airflow is used to schedule and manage the execution of the producer and consumer scripts.

## Components

### Kafka

Kafka is used as a distributed streaming platform to handle real-time data. It allows the producer to send weather data to different topics and the consumer to read from these topics and process the data.

### MySQL

MySQL is used as the relational database to store the weather data. Different tables are created to store different aspects of the weather data, such as temperature, humidity, wind speed, etc.

### Airflow

Airflow is used to schedule and manage the execution of the producer and consumer scripts. It ensures that the data fetching and processing happens at regular intervals.

### OpenWeatherMap API

The OpenWeatherMap API is used to fetch real-time weather data for multiple cities. The API provides various weather parameters such as temperature, humidity, wind speed, and pressure.

## Project Structure

```plaintext
weather-data-pipeline/
│
├── airflow/
│   └── dags/
│       └── weather_dag.py      # Airflow DAG for scheduling
│
├── db_operations.py            # Database operations script
├── weather_producer.py         # Kafka producer script
├── weather_consumer.py         # Kafka consumer script
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```
#Kafka Zookeeper
![Zookeeper](https://github.com/atharva49/Realtime-Weather-Streaming/assets/56105570/b272905c-306f-4b8d-8bce-cdb7537a5eff)

#Kafka Server
![Server](https://github.com/atharva49/Realtime-Weather-Streaming/assets/56105570/9a4c5668-fea5-4db8-8631-05ce0c8b7196)

#Kafka Producer
![Producer](https://github.com/atharva49/Realtime-Weather-Streaming/assets/56105570/0995a3bc-87f9-4c60-b221-26ccdd25f8d9)

#Kafka consumer
![Consumer](https://github.com/atharva49/Realtime-Weather-Streaming/assets/56105570/65e8cbd0-6797-43df-8dfd-8b0d3f72fb1c)

#Data in MySQL
![Data](https://github.com/atharva49/Realtime-Weather-Streaming/assets/56105570/474cb7c5-f88e-4dfe-98b9-7ab27652e298)
