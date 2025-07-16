#This'll run the main program for everything and take in an input from user then output the recommended crop rotations


from cropRecommendation import CropRecommendation


if __name__ == '__main__':
    crop_rec = CropRecommendation()
    results = crop_rec.compareWeatherToCrops()
    crop_rec.displayResults(results)