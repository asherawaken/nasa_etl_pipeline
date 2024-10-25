import requests
from config.settings import settings

API_KEY = settings.NASA_API_KEY

def fetch_apod_data(start_date, end_date):
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&start_date={start_date}&end_date={end_date}"
    response = requests.get(url)
    return response.json()

def fetch_neo_data(start_date, end_date):
    url = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={API_KEY}&start_date={start_date}&end_date={end_date}"
    response = requests.get(url)
    return response.json()

def fetch_mars_photos(earth_date):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?api_key={API_KEY}&earth_date={earth_date}"
    response = requests.get(url)
    return response.json()