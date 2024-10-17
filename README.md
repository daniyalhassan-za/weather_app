SkyForecast API is a FastAPI-based web application that allows users to retrieve and display current weather information using the OpenWeather API. Users can input a location and receive real-time weather data, including temperature and weather conditions.

Files
main.py: Handles the backend operations, setting up the FastAPI server, defining routes for home and weather requests, and fetching weather data from the OpenWeather API.

home.html: Provides the frontend interface where users can enter a location and view the retrieved weather data.

How to Run
Clone the repository.

Install the required dependencies: pip install fastapi uvicorn requests jinja2.

Set your OpenWeather API key in main.py.

Run the FastAPI server: uvicorn main:app --reload.

Open your browser and navigate to http://127.0.0.1:8000
