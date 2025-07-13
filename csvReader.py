#This'll take in the csv. Should have some features where it'll update with new variables maybe ? 
#Unsure of the current plan but I want to make sure its scaleable and updates whenever new variables are added
#and the system isn't completely bricked
#Just going to use some simple data from Google search for the test run right now, data isn't meant to be totally accurate and just a rough
#approximation to test how the system & code works, along with rounding the average to the first decimal point, rainfall is measured by week and in mm
#All of the temperatures & measurements are going to be done in metric system

import pandas as pd

cropData = pd.read_csv("crop_data.csv")
print(cropData.head() )