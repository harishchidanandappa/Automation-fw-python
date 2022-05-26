from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import logging
import utilities.customlogger as cl
import time
from Data.config_data import FE_TestData


class ImportPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _button_skip_introduction = "//div[4]/div/div"
    _button_fleet_depot_next = "button-fleet-next"
    _import_dropdown_input = "input-file-upload"
    _button_save_template = '.css-1tf0t0h:nth-child(3)'
    _btn_confirm_csv_settings = '.css-1tf0t0h:nth-child(1)'
    _btn_confirm_plan_tour = "button-orders-next"
    _page_text = "//*[contains(text(),'Tour details')]"

    def click_skip_introduction(self):
        self.elementClick(self._button_skip_introduction, locatorType="xpath")

    def click_fleet_depot_next(self):
        self.elementClick(self._button_fleet_depot_next)

    def upload_csv_file(self):
        self.sendKeys(FE_TestData.destinationFile, self._import_dropdown_input)

    def save_info_file(self):
        self.elementClick(self._button_save_template, locatorType="css")

    def review_confirm_csvsettigns(self):
        self.elementClick(self._btn_confirm_csv_settings, locatorType="css")

    def confirm_plan_tour(self):
        self.elementClick(self._btn_confirm_plan_tour)

    def validate_tour_details_text(self):
        data = self.getText(self._page_text, By.XPATH)
        return data

    def page_import_tour_details_from_csv(self):
        self.click_skip_introduction()
        self.click_fleet_depot_next()
        self.upload_csv_file()
        self.save_info_file()
        self.review_confirm_csvsettigns()
        time.sleep(5)
        self.confirm_plan_tour()
        time.sleep(5)
        return self.validate_tour_details_text()
