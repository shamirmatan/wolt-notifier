import json
import geocoder
import requests
from dataclasses import dataclass
from enum import Enum
from typing import Dict

class Geo(Enum):
    LAT = 0
    LON = 1

@dataclass
class Restaurant:
    name: str
    online: bool = False
    api = 'https://restaurant-api.wolt.com/v1/'

    @staticmethod
    def _get_my_location():
        my_location = geocoder.ip("me")
        return my_location.latlng

    def _search_restaurant(self, restaurant: str, lat: float, lon: float) -> Dict:
        x = requests.get(f'{self.api}search?sort=relevancy&q={restaurant}&lat={lat}&lon={lon}&limit=20')
        x_dict = json.loads(x.text)
        return x_dict["results"]
    
    def _is_target_restaurant(self, restaurant: str) -> bool:
        return restaurant["value"].get("name")[0]["value"] == self.name

    def _get_restaurant(self, restaurant: str) -> Dict:
        location = Restaurant._get_my_location()
        optional_rests = self._search_restaurant(restaurant, *location)
        for rest in optional_rests:
            if self._is_target_restaurant(rest):
                return rest["value"]

    def is_online(self) -> bool:
        return self._get_restaurant(self.name)["online"]
