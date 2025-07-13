#This'll take in the csv. Should have some features where it'll update with new variables maybe ? 
#Unsure of the current plan but I want to make sure its scaleable and updates whenever new variables are added
#and the system isn't completely bricked
#Just going to use some simple data from Google search for the test run right now

import pandas as pd

cropData = pd.read_csv("test.csv")
print(cropData.head() )