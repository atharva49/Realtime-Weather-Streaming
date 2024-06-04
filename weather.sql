CREATE DATABASE weather_db;

USE weather_db;

CREATE TABLE weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    description VARCHAR(100),
    temperature FLOAT,
    humidity INT,
    wind_speed FLOAT,
    pressure INT,
    timestamp DATETIME
);

CREATE TABLE humidity (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    humidity INT,
    timestamp DATETIME
);

CREATE TABLE temperature (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    timestamp DATETIME
);

CREATE TABLE wind_speed (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    wind_speed FLOAT,
    timestamp DATETIME
);

CREATE TABLE pressure (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    pressure INT,
    timestamp DATETIME
);
