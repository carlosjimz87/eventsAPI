import os
from typing import Any
from xml.etree import ElementTree
from typing import Dict, Union, List

Element = ElementTree.Element


class XMLParser:
    MOCK_RESPONSE_09 = "assets/xml/mock_response_09.xml"
    MOCK_RESPONSE_10 = "assets/xml/mock_response_10.xml"
    MOCK_RESPONSE_11 = "assets/xml/mock_response_11.xml"

    @staticmethod
    def parse_str(content: Any) -> ElementTree.Element:
        return ElementTree.fromstring(content)

    @staticmethod
    def parse_file(filename: str) -> ElementTree.Element:
        with open(filename, 'r') as file:
            return ElementTree.parse(file).getroot()

    @staticmethod
    def parse_event(
            base_event: Dict[str, Union[str, int]]
    ) -> Dict[str, str]:
        return {
            "base_event_id": base_event.get("base_event_id"),
            "sell_mode": base_event.get("sell_mode", "offline"),
            "title": base_event.get("title"),
        }
