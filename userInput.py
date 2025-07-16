
#This takes in the userInput and gives out an output for the idx of the selected crop variables & weather variable

#Oopsies I forgot to add in the choice for user to select the location & unit selected for all of the data gathered
#by the WeatherAPI. Eh, I'll add it once I finish the crop recommendation file

from csvReader import csvReader
from weatherAPI import weatherAPI
from dfProcessor import DataFrameProcessor

class UserInput():
    
    def __init__(self):
        self.csvCrop = csvReader()
        self.weather = weatherAPI()

    def displayList(self, inputList):
        for idx, tables in enumerate(inputList):
            print(f"{idx}) {tables}")
    
    def getVariables(self):
        cropList = self.csvCrop.returnLabels()
        self.displayList(cropList)
        #This would be the numbered list
        crop_choices = list(map( int, input("Enter two numbers (e.g., 3,4) to select the variables to be compared: ").split(',')))
        #This would be a list of str that the numbers in crop_choice corresponded to in the inputted list
        crop_range = [cropList[c] for c in crop_choices] #Is this one even needed ? Maybe to make sure the user made a correct selection later

        #print(crop_choices)
        #print(crop_range)

        dfWeatherProc = DataFrameProcessor( self.weather.returnDF() )
        weatherLabel = dfWeatherProc.returnLabels()
        self.displayList( weatherLabel )
        weather_choice = int(input("Select a number for the corresponding variable to be compared to the range selected: ") )
        weather_label = weatherLabel[weather_choice]
        
        #print(weather_choice)
        #print(weather_label)

        #This returns as a list 
        #return crop_choices, weather_choice
        return crop_range, weather_label


#test = Input()
#cropData = csvReader()
#cropList = cropData.returnLabels()
#returnListTest = test.getVariables()
#print( returnListTest[0] )
#test.displayList( cropList )