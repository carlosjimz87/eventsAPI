from utils.xml_parser import XMLParser, Element
from providers.fake_responses import FakeResponses
import requests


class FakeProvider:
    @staticmethod
    def events_on_date(date: str) -> (Element, int):
        response = requests.get(FakeResponses.events_urls(date))
        return XMLParser.parse_str(response.content), response.status_code
