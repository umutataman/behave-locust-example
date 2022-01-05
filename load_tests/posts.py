import json
import os

from locust import HttpUser, task
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
api_data = json.load(open('data/api_data.json', 'r'))


class Posts(HttpUser):
    host = os.getenv("API_URL")
    max_wait = 300
    min_wait = 300
    sleep_time = 10

    def __init__(self, parent):
        super().__init__(parent)
        self.base_url = None
        self.headers = None
        self.response = None

    @task
    def list_post(self):
        self.client.get("posts/5")
