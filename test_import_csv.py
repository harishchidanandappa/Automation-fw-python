from pages.home.import_page import ImportPage
import unittest
import pytest
from utilities.util import Util
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class OrderImportCsv(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = ImportPage(self.driver)
        self.ut = Util()
        self.ts = TestStatus(self.driver)

    def test_add_order_import(self):
        data = self.lp.page_import_tour_details_from_csv()
        result = self.ut.verifyTextContains(data, "Tour details")
        self.ts.markFinal("test_add_order_import", result, "Text Tour details exist")
