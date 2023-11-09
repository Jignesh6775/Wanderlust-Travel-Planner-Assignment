# Wanderlust-Travel-Planner-Assignment

The Wanderlust Travel Planner API is a Flask-based backend application that empowers users to plan their trips, manage destinations, create itineraries, track expenses, and fetch weather information for a specified location. This README provides an overview of the API and its features.

## Table of Contents
- [Features](#features)
- [API Routes](#api-routes)
  - [Welcome Route](#welcome-route)
  - [Weather Route](#weather-route)
  - [Destination Routes](#destination-routes)
  - [Itinerary Routes](#itinerary-routes)
  - [Expense Routes](#expense-routes)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Features
The Travel Planner API includes the following key features:
1. **Database Integration**: Utilizes a PostgreSQL database for storing destinations, itineraries, and expenses.
2. **Destination Management**: API endpoints for creating, retrieving, updating, and deleting destinations.
3. **Itinerary Planning**: API endpoints for creating and managing travel itineraries.
4. **Expense Tracking**: Allows users to record and categorize expenses related to their trips.
5. **Weather Data**: Fetches real-time weather information for a specified location using the OpenWeatherMap API.

## API Routes

### Welcome Route
- **Route**: `/`
- **Method**: GET
- **Description**: A welcome route to check if the API is running.

### Weather Route
- **Route**: `/weather`
- **Method**: GET
- **Description**: Fetches real-time weather information for a specified location.
- **Query Parameters**:
  - `location` (string, required): The name of the location for weather data retrieval.
- **Response**:
  - If successful, it returns JSON data with temperature, condition, humidity, and wind speed.
  - In case of an error, it provides an error message and an appropriate HTTP status code.

### Destination Routes
- **Route**: `/destinations`
- **Methods**: POST, GET
- **Description**: Allows users to create new destinations and retrieve a list of destinations.

- **Route**: `/destinations/<int:destination_id>`
- **Methods**: GET, PUT, DELETE
- **Description**: Retrieves, updates, or deletes a specific destination by its ID.

### Itinerary Routes
- **Route**: `/itineraries`
- **Methods**: POST, GET
- **Description**: Enables users to create itineraries and retrieve a list of itineraries.

- **Route**: `/itineraries/<int:itinerary_id>`
- **Methods**: PUT, DELETE
- **Description**: Updates or deletes a specific itinerary by its ID.

### Expense Routes
- **Route**: `/expenses`
- **Methods**: POST, GET
- **Description**: Allows users to create expenses and retrieve a list of expenses.

- **Route**: `/expenses/<int:expense_id>`
- **Methods**: PUT, DELETE
- **Description**: Updates or deletes a specific expense by its ID.

## Getting Started
1. Clone the repository.
2. Set up a PostgreSQL database and provide the connection details in your `.env` file.
3. Install the required packages using `pip install -r requirements.txt`.
4. Run the Flask application using `python app.py`.

## Usage
1. Access the API routes using tools like `curl` or create a client application to interact with the API.
2. Use the `/weather` route to fetch real-time weather data for a location by passing the `location` query parameter.
3. Create destinations, itineraries, and expenses using their respective routes.
