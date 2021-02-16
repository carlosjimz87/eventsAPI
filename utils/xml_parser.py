from datetime import datetime
from typing import Dict
from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError

from models.events import EventList, EventSummary
from utils.formatter import Formatter
from utils.validator import Validator


class XMLParser:
    @staticmethod
    def parse_text_on_date(text: str, date: datetime):
        tree = XMLParser.parse_str(text)
        return XMLParser.parse_base_event(tree, str(date.date()))

    @staticmethod
    def parse_str(content: str) -> ElementTree.Element:
        try:
            return ElementTree.fromstring(content)
        except ParseError as e:
            print(e.text)

    @staticmethod
    def parse_base_event(tree: ElementTree.Element, date: str) -> EventList:
        events = []
        for base_event in tree.find("output"):
            event = {**XMLParser.parse_event(base_event), "date_query": date}

            if Validator.is_online(event):
                event.pop("sell_mode")
                events.append(EventSummary(**event))
        return events

    @staticmethod
    def parse_event(base_event: ElementTree.Element) -> Dict[str, str]:
        data = {}
        try:
            event = base_event.find("event")
            prices = [float(z.attrib.get("price")) for z in event.findall("zone")]
            data.update(
                {
                    "base_event_id": base_event.attrib.get("base_event_id"),
                    "sell_mode": base_event.attrib.get("sell_mode"),
                    "title": base_event.attrib.get("title"),
                    "start_date": str(
                        Formatter.str_to_date(event.attrib.get("sell_from")).date()
                    ),
                    "start_time": str(
                        Formatter.str_to_date(event.attrib.get("sell_from")).time()
                    ),
                    "end_date": str(
                        Formatter.str_to_date(event.attrib.get("sell_to")).date()
                    ),
                    "end_time": str(
                        Formatter.str_to_date(event.attrib.get("sell_to")).time()
                    ),
                    "min_price": min(prices),
                    "max_price": max(prices),
                }
            )
        except (ElementTree.ParseError, ValueError):
            print(f"Parsing error, external API is returning invalid data")
        return data
