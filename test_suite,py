import unittest
from tests.home.test_import_csv import OrderImportCsv
from tests.home.test_manual_select import OrderManualSelect
from tests.home.test_geo_cordinates_api import TestHereAPI

tc1 = unittest.TestLoader().loadTestsFromTestCase(OrderImportCsv)
tc2 = unittest.TestLoader().loadTestsFromTestCase(OrderManualSelect)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestHereAPI)


smokeTest = unittest.TestSuite([tc1,tc2,tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
