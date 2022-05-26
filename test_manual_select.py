from pages.home.manual_select_page import ManualSelectPage
import unittest
import pytest
from utilities.util import Util
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class OrderManualSelect(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.ms = ManualSelectPage(self.driver)
        self.ut = Util()
        self.ts = TestStatus(self.driver)

    def test_add_order_csv(self):
        data = self.ms.here_intro()
        result = self.ut.verifyTextContains(data, "Tour details")
        self.ts.markFinal("test_add_order_csv", result, "Text Tour details exist")
