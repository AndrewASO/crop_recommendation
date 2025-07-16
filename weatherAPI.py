#This'll retrieve the weather conditions in a certain location according to the user's specifications 
#Should retrieve atleast temperature, humidity, and rainfall
#Aiming to retrieve rainfall per wk, or having a configurable option for the user to retrieve it by day, week, or month if the option is available for the weatherAPI

#Going to be experimenting with weatherapi.com for now but will look into 
#openweather, weatherbit, visualcrossing, meteomatics, and weatherusa in the future for comparison to the one currently being used 
#Might even add an option later for the user to choose which one they would want to choose based on speed and data retrieved by said API's

#For later when this could potentially become a website or for other users to use, this would need to be a partial backend that's hosted through potentially google 
#cloud for the api to be separated and private.
#Hmm, possibly could look into some libraries that would allow website to be built from this because if not, then this would need to be separated
#into a frontend & backend for the website to actually work and it wasn't planned out that far.
#Could just host a random backend for just the .env variables in 1 python file as well allowing this whole folder to become the frontend

from dfProcessor import DataFrameProcessor
import requests
import json
import pandas as pd
import os 
import dotenv
from dotenv import load_dotenv
load_dotenv()


class weatherAPI:

    def __init__(self, location = "new york", unit = "metric"):
        self.location = location
        self.unit = unit
        self.weatherAPIKey = os.getenv("weatherAPI_Key")

    def buildURL(self):
        #return "https://api.tomorrow.io/v4/weather/realtime?location={self.location}&units={self.unit}&apikey={self.weatherAPIKey}" //Figure out why this didn't work
        return "https://api.tomorrow.io/v4/weather/realtime?location=" + self.location + "&units=" + self.unit + "&apikey=" + self.weatherAPIKey

    def getWeather(self):
        url = self.buildURL()

        headers = {
            "accept": "application/json",
            "accept-encoding": "deflate, gzip, br"
        }

        response = requests.get(url, headers = headers)

        return response.text

    def returnDF(self):
        #Parse JSON string
        data_dict = json.loads( self.getWeather() )

        #Flatten the structure
        flat_dict = data_dict["data"].copy()
        flat_dict.update(flat_dict.pop("values") )
        flat_dict.update(data_dict["location"] )

        #Create DF
        df = pd.DataFrame( [flat_dict] )

        return df

    
#test = weatherAPI()
#dfTest = DataFrameProcessor( test.returnDF() )
#print( dfTest.returnColumn('temperature') )
#print(dfTest.returnLabels() )
#print( test.getWeather().text )
#weatherText = test.getWeather()
#print( test.convertToDF(weatherText) )
#print( test.returnLabels() )


