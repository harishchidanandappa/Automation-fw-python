from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import logging
import utilities.customlogger as cl
import time


class ManualSelectPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    _btn_skip_intro = "//div[4]/div/div"
    _text_user_name = "input-edit-order-name"
    _fleet_depot_next = "button-fleet-next"
    _manual_mode_option = "button-orders-mode-Manual"
    _user_address = "input-edit-order-add"
    _select_address = "input-edit-order-add-option-0"
    _select_auto_address = "//div[@id='input-edit-order-add-option-0']"
    _add_order = "#button-add-order-manual > div"
    _add_order_next = "button-orders-next"
    _page_text = "//*[contains(text(),'Tour details')]"

    def click_skip_intro(self):
        self.elementClick(self._btn_skip_intro, locatorType="xpath")

    def click_fleet_depot_Next(self):
        self.elementClick(self._fleet_depot_next)

    def select_manual_order_option(self):
        self.elementClick(self._manual_mode_option)

    def enter_name(self, name):
        self.sendKeys(name, self._text_user_name)

    def enter_address(self, data):
        self.sendKeys(data, self._user_address)

    def select_auto_suggestion(self):
        self.elementClick(self._select_auto_address, locatorType="xpath")

    def add_order_in_the_list(self):
        self.elementClick(self._add_order, locatorType="css")

    def plan_tour(self):
        self.elementClick(self._add_order_next)

    def page_text(self):
        data = self.getText(self._page_text, By.XPATH)
        return data

    def here_intro(self):
        self.click_skip_intro()
        self.click_fleet_depot_Next()
        self.select_manual_order_option()
        self.enter_name('test1')
        self.enter_address("Invalidenstraße 112, 10115 Berlin, Germany")
        time.sleep(5)
        self.select_auto_suggestion()
        self.add_order_in_the_list()
        self.enter_name('test2')
        self.enter_address("Invalidenstraße 29, 10115 Berlin, Germany")
        time.sleep(5)
        self.select_auto_suggestion()
        self.add_order_in_the_list()
        self.enter_name('test3')
        self.enter_address("Chausseestraße 22, 10115")
        time.sleep(5)
        self.select_auto_suggestion()
        self.add_order_in_the_list()
        self.plan_tour()
        return self.page_text()
