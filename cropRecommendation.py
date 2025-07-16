#This'll contain the algorithm for recommending crops based on the variable information it gets from weatherAPI and the 
#recommended crop variables from csvReader

from csvReader import csvReader
from weatherAPI import weatherAPI
from dfProcessor import DataFrameProcessor
from userInput import UserInput

class CropRecommendation:

    def __init__(self):
        self.userInput = UserInput()



