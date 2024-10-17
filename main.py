from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import httpx

app = FastAPI()

API_KEY = "a3d7df939b35376dcd7c8ae066769404"
URL = "http://api.openweathermap.org/data/2.5/weather"

templates = Jinja2Templates(directory="templates")

def format_time(timestamp, offset):
    """Convert a UTC timestamp to a formatted time string in local time."""
    local_time = datetime.utcfromtimestamp(timestamp + offset).strftime('%H:%M')
    return local_time

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, city: str = None):
    weather_data = None
    if city:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        async with httpx.AsyncClient() as client:
            response = await client.get(URL, params=params)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "weather": data["weather"][0]["description"],
                    "wind_speed": data["wind"]["speed"],
                    "humidity": data["main"]["humidity"],
                    "sunrise": format_time(data["sys"]["sunrise"], data["timezone"]),
                    "sunset": format_time(data["sys"]["sunset"], data["timezone"])
                }
            else:
                raise HTTPException(status_code=response.status_code, detail="City not found")
    return templates.TemplateResponse("home.html", {"request": request, "weather_data": weather_data})
