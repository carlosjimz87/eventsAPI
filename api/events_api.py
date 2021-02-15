from providers.fake_provider import FakeProvider
from typing import Dict, Union, List
from requests.exceptions import MissingSchema
from utils.xml_parser import XMLParser


class EventsApi:
    @staticmethod
    def get_available_events(date: str) -> List[Dict[str, Union[str, int]]]:
        events = []
        try:
            tree, status = FakeProvider.events_on_date(date)
            if status == 200:
                for base_event in tree.find("output"):
                    events.append(XMLParser.parse_event(base_event.attrib))

        except MissingSchema:
            print(f"{date} is not provided in the External Provider API")

        return [event for event in events if event.get(
            "sell_mode") == "online"]
