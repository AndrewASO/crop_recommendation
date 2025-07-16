Crop Recommendation with WeatherAPI

This takes a csv file with crop information such as: name, rotation type, minimum temperature, average temperature, maximum temperature, etc.
The weather API will grab a list of weather variables from the location in the selected unit.
Then there will be a displayed list of the crop labels that the user most choose to select a range to see if the weather variable they selected
falls within said range.
Then there would be an algorithm to see if the weather value falls within the crop range and if it does then it recommends it, and the recommended
crops are separated into rotation types, and if there's no recommended crop within that rotation type, then an output of "No Match Was Found" will be given.






Future work Needed
- Implement a user friendly front-end (Potentially as a website or tkinter)
- Allow for more than 1 crop variable range to 1 weather variable comparison
- Code for the user to select weatherAPI location & unit selected
- Optimize the code
- Add more data to the csv
- Look for a more robust dataset online for the crops, or use webscraping to gather crop information
- Add unit tests for each of the different classes
