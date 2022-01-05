import json
import os
from json import dumps

import requests as requests
from behave import *
from dotenv import load_dotenv, find_dotenv

use_step_matcher("re")

load_dotenv(find_dotenv())
api_data = json.load(open('data/api_data.json', 'r'))


@given("I start session")
def step_impl(context):
    context.base_url = os.getenv("API_URL") + "posts/"
    context.headers = api_data["headers"]
    context.payload = dumps(api_data["payload"])
    context.post_5 = api_data["post-five"]
    context.update_5 = dumps(api_data["update-five"])


@when("I create a new post")
def step_impl(context):
    context.response = requests.post(url=context.base_url, data=context.payload, headers=context.headers)


@then("I confirm post created")
def step_impl(context):
    assert context.response.status_code == requests.codes.created, \
        f"Actual: {context.response.status_code} - Expected: 201"


@when("I get details for post '5'")
def step_impl(context):
    request_url = f"{context.base_url}5/"
    context.response = requests.get(url=request_url, headers=context.headers)


@then("I confirm OK response")
def step_impl(context):
    assert context.response.status_code == requests.codes.ok, \
        f"Actual code: {context.response.status_code} - Expected code: 200"


@then("I confirm post '5' listed")
def step_impl(context):
    assert context.response.json() == context.post_5, \
        "Data do not match"


@then("I confirm post '5' updated")
def step_impl(context):
    assert json.dumps(context.response.json()) == context.update_5, \
        "Data do not match"


@when("I update post '5'")
def step_impl(context):
    request_url = f"{context.base_url}/5/"
    context.response = requests.put(url=request_url, data=context.update_5, headers=context.headers)


@when("I delete post '5'")
def step_impl(context):
    request_url = f"{context.base_url}/5/"
    context.response = requests.delete(url=request_url, headers=context.headers)
