from flask import Flask, request, jsonify
import psycopg2
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from the .env file
load_dotenv()

# Database connection setup
DATABASE_URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)

# Create tables
def create_tables():
    with conn.cursor() as cursor:
        tables = [
            '''
            CREATE TABLE IF NOT EXISTS destinations (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT,
                location VARCHAR(100)
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS itineraries (
                id SERIAL PRIMARY KEY,
                destination_id INTEGER,
                activity TEXT,
                FOREIGN KEY (destination_id) REFERENCES destinations (id)
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS expenses (
                id SERIAL PRIMARY KEY,
                destination_id INTEGER,
                description TEXT,
                amount DECIMAL,
                FOREIGN KEY (destination_id) REFERENCES destinations (id)
            )
            '''
        ]
        for table in tables:
            cursor.execute(table)
        conn.commit()


# Routes
@app.route('/')
def welcome():
    return jsonify(message='Welcome to the Wanderlust Travel Planner API!')

# Define the route to get weather data
@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    weather_data = fetch_weather_data(location, api_key)
    return jsonify(weather_data)

def fetch_weather_data(location, api_key):
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    try:
        response = requests.get(weather_url)
        data = response.json()
        if response.status_code == 200:
            return {
                'location': location,
                'temperature': data['main']['temp'],
                'condition': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }, 200
        else:
            return {'error': 'Weather data not found'}, 404
    except Exception as e:
        return {'error': 'An error occurred while fetching weather data'}, 500

# Destination Routes 
@app.route('/destinations', methods=['POST'])
def create_destination():
    data = request.get_json()
    name, description, location = data['name'], data['description'], data['location']
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO destinations (name, description, location) VALUES (%s, %s, %s)", (name, description, location))
        conn.commit()
    return jsonify(message='Destination created successfully'), 201

@app.route('/destinations', methods=['GET'])
def get_destinations():
    destinations = fetch_records('destinations')
    return jsonify(destinations), 200

@app.route('/destinations/<int:destination_id>', methods=['GET'])
def get_destination(destination_id):
    destination = fetch_record_by_id('destinations', destination_id)
    return jsonify(destination), 200 if destination else 404

@app.route('/destinations/<int:destination_id>', methods=['PUT'])
def update_destination(destination_id):
    data = request.get_json()
    update_record('destinations', destination_id, data)
    return jsonify(message='Destination updated successfully'), 200

@app.route('/destinations/<int:destination_id>', methods=['DELETE'])
def delete_destination(destination_id):
    delete_record('destinations', destination_id)
    return jsonify(message='Destination deleted successfully'), 200

# Itinerary Routes
@app.route('/itineraries', methods=['POST'])
def create_itinerary():
    data = request.get_json()
    insert_record('itineraries', data)
    return jsonify(message='Activity added to itinerary'), 201

@app.route('/itineraries', methods=['GET'])
def get_itineraries():
    itineraries = fetch_records('itineraries')
    return jsonify(itineraries), 200

@app.route('/itineraries/<int:itinerary_id>', methods=['PUT'])
def update_itinerary(itinerary_id):
    data = request.get_json()
    update_record('itineraries', itinerary_id, data)
    return jsonify(message='Activity updated in itinerary'), 200

@app.route('/itineraries/<int:itinerary_id>', methods=['DELETE'])
def delete_itinerary(itinerary_id):
    delete_record('itineraries', itinerary_id)
    return jsonify(message='Activity removed from itinerary'), 200

# Expense Routes
@app.route('/expenses', methods=['POST'])
def create_expense():
    data = request.get_json()
    insert_record('expenses', data)
    return jsonify(message='Expense added successfully'), 201

@app.route('/expenses/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    data = request.get_json()
    update_record('expenses', expense_id, data)
    return jsonify(message='Expense updated successfully'), 200

@app.route('/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    delete_record('expenses', expense_id)
    return jsonify(message='Expense deleted successfully'), 200

@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = fetch_records('expenses')
    return jsonify(expenses), 200



# Database operations
def fetch_records(table):
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table}")
        return cursor.fetchall()

def fetch_record_by_id(table, record_id):
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table} WHERE id = %s", (record_id,))
        return cursor.fetchone()

def insert_record(table, data):
    with conn.cursor() as cursor:
        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        cursor.execute(query, tuple(data.values()))
        conn.commit()

def update_record(table, record_id, data):
    with conn.cursor() as cursor:
        set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE id = %s"
        cursor.execute(query, tuple(data.values()) + (record_id,))
        conn.commit()

def delete_record(table, record_id):
    with conn.cursor() as cursor:
        cursor.execute(f"DELETE FROM {table} WHERE id = %s", (record_id,))
        conn.commit()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
