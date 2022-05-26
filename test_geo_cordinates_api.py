import requests
import unittest
from Data.config_data import BETestData
import utilities.customlogger as cl
import logging
from utilities.teststatus import TestStatus


class TestHereAPI(unittest.TestCase):
    url = BETestData.FULL_URL
    log = cl.customLogger(logging.DEBUG)
    ts = TestStatus(driver=None)

    def getCoordinates(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.log.info("request is processed")
                self.ts.mark(True, "401 unauthorised exception")
                return response
            elif response.status_code == 401:
                self.log.info("Unauthorized api key")
                self.ts.mark(False, "401 unauthorised exception")
                raise Exception(response.status_code)
            else:
                self.log.info("error in processing request")
                self.ts.mark(False, "Other exceptions")
                raise Exception(response.status_code)
        except requests.ConnectionError:
            self.log.info("Connection Error")

    def test_geo_cordinates(self):
        response_body = self.getCoordinates()
        lat = response_body["items"][0]["position"]["lat"]
        lng = response_body["items"][0]["position"]["lng"]
        assert lat == BETestData.address_lat
        assert lng == BETestData.address_lng
        if lat == BETestData.address_lat and lng == TestData.address_lng:
            self.ts.markFinal("test_geo_coordinates", True, "validation is working fine")
            assert True
        else:
            self.ts.markFinal("test_geo_coordinates", False, "validation is working fine")
            assert False
