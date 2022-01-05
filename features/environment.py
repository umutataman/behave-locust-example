import os
import shutil
import time

import allure
from selenium import webdriver
import undetected_chromedriver as uc


def before_all(context):
    if os.path.exists("capture_of_failed"):
        shutil.rmtree("capture_of_failed")

    # Global variables
    context.headless = context.config.userdata.get("headless")
    # Global Delays
    context.element_wait = 30
    context.ddos_attack_wait = 5
    context.search_wait = 4
    context.basket_after_load_wait = 2

    print("Initials are done and test starting")


def before_feature(context, feature):
    context.ft_name = feature.name


def before_scenario(context, scenario):
    if "web" in scenario.effective_tags:
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("ignore-certificate-errors")
        options.add_argument("--no-sandbox")

        if context.headless == "true":
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")

        context.browser = uc.Chrome(chrome_options=options)


def after_scenario(context, scenario):
    if "web" in scenario.effective_tags:
        if scenario.status == "failed":
            ss_name = scenario.name + " - " + time.strftime("%H:%M:%S")
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
