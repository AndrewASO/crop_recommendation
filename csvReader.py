#This'll take in the csv. Should have some features where it'll update with new variables maybe ? 
#Unsure of the current plan but I want to make sure its scaleable and updates whenever new variables are added
#and the system isn't completely bricked
#Just going to use some simple data from Google search for the test run right now, data isn't meant to be totally accurate and just a rough
#approximation to test how the system & code works, along with rounding the average to the first decimal point, rainfall is measured by week and in mm
#All of the temperatures & measurements are going to be done in metric system
#Averages might not be needed ? Just using the temperature range to see if the temperature, humidity & rainfall grabbed from the input region
#fits within that range so average might not be needed.

#Column 0: name, 1: rotation type, 2: min temp, 3: avg temp, 4: max temp, 5: min humidity, 6: avg humidity, 7: max humidity, 8: min rainfall, 9: avg rainfall, 10: max rainfall
#Rotation: Legumes --> Greens --> Fruits --> Root --> Legumes

import pandas as pd
from dfProcessor import DataFrameProcessor

class csvReader:

    def __init__(self):
        self.cropData = pd.read_csv("crop_data.csv")
    
    def returnDataframe(self):
        return self.cropData



#test = csvReader()
#df = test.returnDataframe()
#dfTest = DataFrameProcessor(df)
#print( dfTest.returnLabels() )
#test.testPrint()
#print( test.returnLabels() )
#print( test.returnRow(1) )
#testRow = test.returnRow(0)
#print( testRow )
#print( testRow.iloc[0] )
#print( test.returnColumn("name") )

#print( len(test.returnDataframe() ) )
'''
if( "potato" == testRow.iloc[0] ):
    print("This test was successful at seeing testRow without tolist() can be used for comparisons")
else:
    print("Test may have failed and testRow without tolist() might not be comparable")
'''
