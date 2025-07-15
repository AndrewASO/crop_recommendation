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

cropData = pd.read_csv("crop_data.csv")
print(cropData.head() )
#print(cropData.head(0) )
#print(cropData.head(1) )
print(cropData.head(2) )