import os


class BETestData:
    API_KEY: str = '80y1lalqWniSYTGsCVOtegNB8asbSIVljFXVpQuT964'
    API_BASE_URL = 'https://geocode.search.hereapi.com/v1/geocode?q='
    address_location_name: str = 'Invalidenstr'
    address_location_number: str = '117'
    address_Location_city: str = 'Berlin'
    FULL_URL = API_BASE_URL + address_location_name + "+" + address_location_number + "+" + \
               address_Location_city + "&apiKey=" + API_KEY

    address_lat: str = '52.53041'
    address_lng: str = '13.38527'


class FE_TestData():
    fileName = "here-wego-deliver-template.csv"
    currentDirectory = os.path.dirname(__file__)
    destinationFile: str = os.path.join(currentDirectory, fileName)
    # geckodriver_path = "/Users/manjunatha.thimmaiah/Documents/Drivers/geckodriver"
    geckodriver_path = ""
