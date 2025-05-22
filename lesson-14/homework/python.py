# === JSON Parsing ===
import json

def read_students():
    with open("students.json", "r") as file:
        data = json.load(file)
        for student in data.get("students", []):
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")


# === Weather API ===
import requests

def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("Failed to fetch weather data.")


# === JSON Modification ===
def load_books():
    with open("books.json", "r") as file:
        return json.load(file)

def save_books(data):
    with open("books.json", "w") as file:
        json.dump(data, file, indent=4)

def add_book(book):
    data = load_books()
    data['books'].append(book)
    save_books(data)

def update_book(title, new_info):
    data = load_books()
    for book in data['books']:
        if book['title'] == title:
            book.update(new_info)
    save_books(data)

def delete_book(title):
    data = load_books()
    data['books'] = [book for book in data['books'] if book['title'] != title]
    save_books(data)


# === Movie Recommendation System ===
import random

def recommend_movie_by_genre(genre):
    api_key = "your_api_key_here"  # Replace with your OMDb API key
    url = f"http://www.omdbapi.com/?apikey={api_key}&type=movie&s={genre}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'Search' in data:
            movie = random.choice(data['Search'])
            print(f"Title: {movie['Title']}")
            print(f"Year: {movie['Year']}")
            print(f"IMDb ID: {movie['imdbID']}")
        else:
            print("No movies found for this genre.")
    else:
        print("Failed to fetch movie data.")
