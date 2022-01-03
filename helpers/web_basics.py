from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Web:
    def __init__(self, context):
        self.context = context

    def get_environment(self):
        env = self.context.config.userdata.get("environment")
        if env == "production" or env == "master":
            env = "stage"
        else:
            env = "test"
        return env

    def click_js(self, element):
        self.context.browser.execute_script("arguments[0].click();", element)

    def alert_accept(self):
        self.context.browser.switch_to.alert.js_alert.accept()

    def locate_by_data_qa(self, locator, text=""):
        return WebDriverWait(self.context.browser, self.context.element_wait).until(lambda driver: driver.find_element_by_xpath(
            f"//*[@data-qa='{locator}' and contains(.,'{text}')]"))

    def locate_by_name(self, locator):
        return WebDriverWait(self.context.browser, self.context.element_wait).until(lambda driver: driver.find_element_by_name(locator))
