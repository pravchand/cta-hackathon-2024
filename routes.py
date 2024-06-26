import matplotlib.pyplot as plt
import pandas as pd
from typing import List, Dict

from cta_analysis.bus import get_routes, get_vehicles, call_api, get_directions, get_all_directions, get_route_stops
from cta_analysis import cta_secrets    
direction = 'Northbound'

class Route:
    def __init__(self, route_id: str) -> None:
        self.route_id = route_id
        self.route_data = None
        self.directions = direction
        self.stops = {}

    def get_route_data(self):
        all_routes = get_routes()
        for route in all_routes:
            #print(route,'printing route within routes.py')
            if route['rt'] == self.route_id:
                self.route_data = route
                break

    # def get_directions(self):
    #     if self.route_data:
    #         self.directions = get_directions(self.route_id)
    #     else:
    #         print("Please call get_route_data.")

    def get_stops(self):
        # if not self.directions:
        #     print("Please call fetch_directions first.")
        #     return
        # for direction in self.directions:
        self.stops = get_route_stops(self.route_id, self.directions)


    #displays info based on data

    def display_route_details(self):
        if not self.route_data:
            print("Please fetch route data first.")
        else:
            print(f"Route ID: {self.route_data['rt']}, Route Name: {self.route_data['rtnm']}")

    def display_directions(self):
        if not self.directions:
            print("fetch directions first.")
        else:
            print(f"Directions for Route {self.route_id}: {self.directions}")

    def display_stops(self):
        if not self.stops:
            print("fetch stops first")
        else:
            for direction, stops in self.stops.items():
                print(f"Stops for {direction}:")
                for stop in stops:
                    print(f"  Stop ID: {stop['stpid']}, Stop Name: {stop['stpnm']}")
