import os
import shutil
import time

import allure
import undetected_chromedriver as uc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from helpers import Web


def before_all(context):
    if os.path.exists("capture_of_failed"):
        shutil.rmtree("capture_of_failed")

    # Global variables
    context.environment = Web(context).get_environment()
    context.app_url = context.config.userdata.get("app_url")
    context.headless = context.config.userdata.get("headless")
    # Global Delays
    context.ddos_attack_wait = 5
    context.search_wait = 4
    context.basket_after_load_wait = 2

    print("Initials are done and test starting for " + context.environment)


def before_feature(context, feature):
    context.ft_name = feature.name


def before_scenario(context, scenario):
    if context.environment == "prod":
        if "automated" not in scenario.effective_tags:
            scenario.skip("Scenario is not automated")
            return
    options = webdriver.ChromeOptions()
    options.add_argument("enable-automation")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--dns-prefetch-disable")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("start-maximized")
    options.page_load_strategy = 'normal'
    if context.headless == "true":
        context.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    else:
        context.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())


def after_scenario(context, scenario):
    if scenario.status == "failed":
        ss_name = scenario.name + time.strftime("%H:%M:%S")
        fail_path = "capture_of_failed" + "/" + time.strftime("%d%b") + "/" + context.ft_name
        file_name = fail_path + "/" + ss_name + ".png"

        # Capture for allure
        allure.attach(context.browser.get_screenshot_as_png(),
                      name=file_name,
                      attachment_type=allure.attachment_type.PNG)

        # Capture for local
        if not os.path.exists(fail_path):
            os.makedirs(fail_path)
        context.browser.save_screenshot(file_name)

    context.browser.quit()


def after_all(context):
    print("Test run is successfully finished. You may check results.")
