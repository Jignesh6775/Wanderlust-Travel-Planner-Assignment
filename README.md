# Wanderlust-Travel-Planner-Assignment

The Wanderlust Travel Planner API is a Flask-based backend application that empowers users to plan their trips, manage destinations, create itineraries, track expenses, and fetch weather information for a specified location. This README provides an overview of the API and its features.

## Table of Contents

- [Installation](#installation)
- [Database Setup](#database-setup)
- [Models](#models)
- [Routes](#routes)
  - [Destination Management](#destination-management)
  - [Itinerary Planning](#itinerary-planning)
  - [Expense Tracking](#expense-tracking)
  - [Weather Route](#weather-route)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/travel-planner-app.git
   ```

2. Change to the project directory:

   ```bash
   cd travel-planner-app
   ```

3. Create a virtual environment (recommended) and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

The application uses a PostgreSQL database to store destination, itinerary, and expense data. To set up the database, make sure you have PostgreSQL installed and follow these steps:

1. Create a new PostgreSQL database.

2. Set the database URL as an environment variable. You can add it to a `.env` file:

   ```
   DATABASE_URL=postgresql://username:password@localhost/dbname
   ```

   Replace `username`, `password`, `localhost`, and `dbname` with your database credentials.

3. Run the following command to create the required tables:

   ```bash
   python setup_database.py
   ```

## Models

The application defines the following data models:

- Destination
  - Fields: id, name, description, location

- Itinerary
  - Fields: id, destination_id, activity

- Expense
  - Fields: id, destination_id, description, amount

## Routes

### Destination Management

- **Create a Destination**: `POST /destinations`
- **Get All Destinations**: `GET /destinations`
- **Get a Destination by ID**: `GET /destinations/<int:destination_id>`
- **Update a Destination by ID**: `PUT /destinations/<int:destination_id>`
- **Delete a Destination by ID**: `DELETE /destinations/<int:destination_id>`

### Itinerary Planning

- **Create an Itinerary**: `POST /itineraries`
- **Get All Itineraries**: `GET /itineraries`
- **Update an Itinerary by ID**: `PUT /itineraries/<int:itinerary_id>`
- **Delete an Itinerary by ID**: `DELETE /itineraries/<int:itinerary_id>`

### Expense Tracking

- **Create an Expense**: `POST /expenses`
- **Get All Expenses**: `GET /expenses`
- **Update an Expense by ID**: `PUT /expenses/<int:expense_id>`
- **Delete an Expense by ID**: `DELETE /expenses/<int:expense_id>`

### Weather Route

- **Get Weather Data**: `GET /weather?location=CityName`

   Returns weather information for the specified location.

## Usage

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Access the API using a tool like `curl` or a web browser.

3. Use the provided routes to manage destinations, itineraries, expenses, and check weather conditions.

## Contributing

Contributions are welcome! Please submit issues or pull requests for any improvements or bug fixes.
