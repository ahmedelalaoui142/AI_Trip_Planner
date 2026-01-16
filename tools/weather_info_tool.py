import os
from typing import Any,Dict,Optional,List
from dotenv import load_dotenv
from utils.weather_info import WeatherForecastTool
from langchain.tools import tool

class WeatherInfoTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
        self.weather_service = WeatherForecastTool(self.api_key)
        self.weather_tool_list = self._setup_tools()
    def _setup_tools(self) -> List:
        """Setup the weather tools"""
        @tool
        def get_current_weather(city: str) -> str:
            """ Get current weather for a city"""
            weather_data = self.weather_service.get_current_weather(city)
            if weather_data:
                temp = weather_data.get('main',{}).get('temp','N/A')
                desc = weather_data.get('weather',[{}])[0].get('description','N/A')
                return f"The current weather in {city} is {temp}°C and {desc}"
            else:
                return f"No weather data found for {city}"
        @tool
        def get_forecast_weather(city: str) -> str:
            """ Get forecast weather for a city"""
            forecast_data = self.weather_service.get_forecast_weather(city)
            if forecast_data and 'list' in forecast_data:
                forecast_summary = []
                for i in range(len(forecast_data['list'])):
                    item = forecast_data['list'][i]
                    date = item['dt_txt'].split(' ')[0]
                    temp = item['main']['temp']
                    desc = item['weather'][0]['description']
                    forecast_summary.append(f"On {date}, the weather will be {temp}°C and {desc}")
                return "The forecast weather for {} is: {}".format(city, "\n".join(forecast_summary))
            return f"No forecast data found for {city}"
        return [get_current_weather, get_forecast_weather]