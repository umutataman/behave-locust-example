import json
import time

from behave import *
from helpers import *
from features.locators.locators_ordering import OrderingLocators

use_step_matcher("re")


@given("I open page of city '(.*)' and postcode '(.*)'")
def step_impl(context, city, postcode):
    url = f"https://www.thuisbezorgd.nl/en/delivery/food/{city}-{postcode}?showTestRestaurants=true"
    context.browser.get(url)
    time.sleep(context.ddos_attack_wait)


@when("I search and find restaurant '(.*)'")
def step_impl(context, restaurant):
    # Search the restaurant
    elm_search_field = Web(context).locate_by_data_qa(OrderingLocators.search_field)
    elm_search_field.send_keys(restaurant)
    time.sleep(context.search_wait)
    # Find the restaurant
    elm_restaurant = Web(context).locate_by_data_qa(OrderingLocators.restaurant, restaurant)
    Web(context).click_js(elm_restaurant)
    # Wait until basket is loaded
    elm_basket = Web(context).locate_by_data_qa(OrderingLocators.header, "Basket")
    time.sleep(context.basket_after_load_wait)


@step("I add couple of burgers to basket and checkout")
def step_impl(context):
    elm_chicken_burger = Web(context).locate_by_data_qa(OrderingLocators.food, "Chicken Burger")
    Web(context).click_js(elm_chicken_burger)
    elm_beef_burger_big = Web(context).locate_by_data_qa(OrderingLocators.food, "Beef Burger [Big]")
    Web(context).click_js(elm_beef_burger_big)
    # Checkout
    elm_side_checkout = Web(context).locate_by_data_qa(OrderingLocators.side_checkout)
    Web(context).click_js(elm_side_checkout)


@step("I enter address details for city '(.*)'")
def step_impl(context, city):
    elm_street_name = Web(context).locate_by_name(OrderingLocators.street_name)
    elm_street_name.send_keys(get_city_data(city)["address"])

    elm_house_number = Web(context).locate_by_name(OrderingLocators.house_number)
    elm_house_number.send_keys(get_city_data(city)["house-number"])

    elm_postcode = Web(context).locate_by_name(OrderingLocators.postcode)
    elm_postcode.clear()
    elm_postcode.send_keys(get_city_data(city)["postcode"])

    elm_city = Web(context).locate_by_name(OrderingLocators.city)
    elm_city.clear()
    elm_city.send_keys(get_city_data(city)["city"])

    elm_name = Web(context).locate_by_name(OrderingLocators.name)
    elm_name.send_keys(get_city_data(city)["name"])

    elm_phone = Web(context).locate_by_name(OrderingLocators.phone_number)
    elm_phone.send_keys(get_city_data(city)["phone"])

    elm_email = Web(context).locate_by_name(OrderingLocators.email)
    elm_email.send_keys(get_city_data(city)["email"])


@step("I select payment method '(.*)'")
def step_impl(context, payment_method):
    elm_payment_method = Web(context).locate_by_data_qa(OrderingLocators.pay_with)
    Web(context).click_js(elm_payment_method)

    elm_payment_method_option = Web(context).locate_by_data_qa(OrderingLocators.payment_method, payment_method)
    Web(context).click_js(elm_payment_method_option)

    elm_done = Web(context).locate_by_data_qa(OrderingLocators.payment_method_done)
    Web(context).click_js(elm_done)


@step("I place the order")
def step_impl(context):
    elm_checkout = Web(context).locate_by_data_qa(OrderingLocators.checkout)
    Web(context).click_js(elm_checkout)


@then("I should see error message that cannot order from different city")
def step_impl(context):
    exception_message = "BRT Cypress Test Restaurant does not deliver in the delivery area 8888AA. " \
                        "Please tap here to see restaurants that deliver in the area 8888AA."
    elm_error_message = Web(context).locate_by_data_qa(OrderingLocators.error_delivery)
    assert exception_message == elm_error_message.text, "Error message is not correct"


@when("I visit restaurants that delivery my city")
def step_impl(context):
    elm_city_restaurants = Web(context).locate_by_data_qa(OrderingLocators.error_delivery_link)
    Web(context).click_js(elm_city_restaurants)


@then("I should see 'BRT Cypress Test Restaurant'")
def step_impl(context):
    elm_restaurant = Web(context).locate_by_data_qa(OrderingLocators.restaurant, "BRT Cypress Test Restaurant")
    assert elm_restaurant is not None, "Restaurant is not found"


@step("I should see '(.*)' address in location")
def step_impl(context, city):
    location = get_city_data(city)["address"] + " " + get_city_data(city)["house-number"] + ", " + get_city_data(city)["postcode"] + " " + get_city_data(city)["city"]
    elm_location = Web(context).locate_by_data_qa(OrderingLocators.location)
    assert elm_location.text == location, "Location is not correct"
