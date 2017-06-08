import requests

from bs4 import BeautifulSoup


class SEOAnalyst:

    def __init__(self, url):
        self.url = url