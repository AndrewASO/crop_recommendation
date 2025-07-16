#This'll contain the algorithm for recommending crops based on the variable information it gets from weatherAPI and the 
#recommended crop variables from csvReader

import pandas as pd
from csvReader import csvReader
from weatherAPI import weatherAPI
from dfProcessor import DataFrameProcessor
from userInput import UserInput

class CropRecommendation:

    def __init__(self):
        self.userInput = UserInput()
        self.crop_data = csvReader()
        self.crop_data_df = self.crop_data.returnDataframe()
        self.weather = weatherAPI()
        self.weather_var = ""
        self.weather_val = ""

    def compareWeatherToCrops(self):
        userSelected = self.userInput.getVariables()

        dfWeatherProc = DataFrameProcessor( self.weather.returnDF() )
        #Had to make this a float because the way it was valued before was giving truth value  of a series is ambigious
        weather_value = float( dfWeatherProc.returnColumn( userSelected[1] ) ) 
        #print(weather_value)
        self.weather_var = userSelected[1]
        self.weather_val = weather_value

        crop_min_col, crop_max_col = userSelected[0]

        rotation_groups = {}

        for idx, row in self.crop_data_df.iterrows():
            min_val = row[crop_min_col]
            max_val = row[crop_max_col]

            #print(min_val)
            #print(max_val)

            if min_val <= weather_value <= max_val:
                rotation = row['rotation_type']
                crop_name = row['name']

                if rotation not in rotation_groups:
                    rotation_groups[rotation] = []
                    
                rotation_groups[rotation].append(crop_name)
        
        return rotation_groups

    def displayResults(self, results):
        print(f"\nCurrent {self.weather_var}: {self.weather_val}")
        print("Suitable crops by rotation group:")

        #Defining expected rotation types
        rotation_types = ['root', 'leaf', 'fruit', 'legume']

        for rot in rotation_types:
            crops = results.get(rot, [] )
            if crops:
                print(f"{rot.capitalize()}: {', '.join(crops) }")
            else:
                print(f"{rot.capitalize()}: No Matches Found")

