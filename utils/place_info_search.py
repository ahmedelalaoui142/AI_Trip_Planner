import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper

class GooglePlaceSearchTool:
    def __init__(self,api_key: str):
        self.places_wrapper = GooglePlacesAPIWrapper(api_key=api_key)
        self.places_tool = GooglePlacesTool(places_wrapper=self.places_wrapper)
    
    def google_search_attractions(self,place:str) -> dict:
        """Search for attractions in a place"""
        return self.places_tool.run(f"top attractives places in and around {place}")
    
    def google_search_restaurants(self,place:str) -> dict:
        """Search for restaurants in a place"""
        return self.places_tool.run(f"what are the top 10 restaurants and eateries in and around {place}")
    def google_search_activities(self,place:str) -> dict:
        """Search for activities in a place"""
        return self.places_tool.run(f"Activities to do in and around {place}")
    def google_search_transportation(self,place:str) -> dict:
        """Search for transportation in a place"""
        return self.places_tool.run(f"what are different modes of transportation available in and around {place}")

class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result