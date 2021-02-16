from typing import Dict
from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError

from requests import Response

from models.events import EventList, EventSummary
from utils.formatter import Formatter
from utils.validator import Validator


class XMLParser:

    @staticmethod
    def parse_response(response: Response, date: str):
        tree = XMLParser.parse_str(response.content)
        return XMLParser.parse_base_event(tree, date)

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

    sample_dates_09, sample_dates_10, sample_dates_11 = "2021-02-09", "2021-02-10", "2021-02-11"

    event_xml = "<base_event base_event_id=\"291\" sell_mode=\"online\" title=\"Camela en concierto\"><event event_date=\"2021-06-30T21:00:00\" event_id=\"291\" sell_from=\"2020-07-01T00:00:00\" sell_to=\"2021-06-30T20:00:00\" sold_out=\"false\"><zone zone_id=\"40\" capacity=\"200\" price=\"20.00\" name=\"Platea\" numbered=\"true\" /><zone zone_id=\"38\" capacity=\"0\" price=\"15.00\" name=\"Grada 2\" numbered=\"false\" /><zone zone_id=\"30\" capacity=\"80\" price=\"30.00\" name=\"A28\" numbered=\"true\" /></event></base_event> "

    sample_xml_09 = "<?xml version='1.0' encoding='UTF-8'?><eventList version='1.0' " \
                    "xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' " \
                    "xsi:noNamespaceSchemaLocation='eventList.xsd'><output><base_event base_event_id='291'" \
                    " sell_mode='online' title='Camela en concierto'><event event_date='2021-06-30T21:00:00'" \
                    " event_id='291' sell_from='2020-07-01T00:00:00' sell_to='2021-06-30T20:00:00' " \
                    "sold_out='false'><zone zone_id='40' capacity='243' price='20.00' name='Platea' " \
                    "numbered='true' /><zone zone_id='38' capacity='100' price='15.00' name='Grada 2' " \
                    "numbered='false' /><zone zone_id='30' capacity='90' price='30.00' name='A28' " \
                    "numbered='true' /></event></base_event><base_event base_event_id='322' sell_mode='online' " \
                    "organizer_company_id='2' title='Pantomima Full'><event event_date='2021-02-10T20:00:00' " \
                    "event_id='1642' sell_from='2021-01-01T00:00:00' sell_to='2021-02-09T19:50:00' " \
                    "sold_out='false'><zone zone_id='311' capacity='2' price='55.00' name='A42' numbered='true'" \
                    " /></event></base_event><base_event base_event_id='1591' sell_mode='online'  " \
                    "organizer_company_id='1' title='Los Morancos'><event event_date='2021-07-31T20:00:00'" \
                    " event_id='1642' sell_from='2021-06-26T00:00:00' sell_to='2021-07-31T19:50:00' " \
                    "sold_out='false'><zone zone_id='186' capacity='2' price='75.00' name='Amfiteatre' " \
                    "numbered='true' /><zone zone_id='186' capacity='16' price='65.00' name='Amfiteatre'" \
                    " numbered='false' /></event></base_event></output></eventList>"

    sample_xml_10 = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><eventList version=\"1.0\" " \
                    "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" " \
                    "xsi:noNamespaceSchemaLocation=\"eventList.xsd\"><output><base_event base_event_id=\"291\" " \
                    "sell_mode=\"online\" title=\"Camela en concierto\"><event event_date=\"2021-06-30T21:00:00\"" \
                    " event_id=\"291\" sell_from=\"2020-07-01T00:00:00\" sell_to=\"2021-06-30T20:00:00\" " \
                    "sold_out=\"false\"><zone zone_id=\"40\" capacity=\"240\" price=\"20.00\" name=\"Platea\" " \
                    "numbered=\"true\" /><zone zone_id=\"38\" capacity=\"50\" price=\"15.00\" name=\"Grada 2\" " \
                    "numbered=\"false\" /><zone zone_id=\"30\" capacity=\"90\" price=\"30.00\" name=\"A28\" " \
                    "numbered=\"true\" /></event></base_event><base_event base_event_id=\"1591\" sell_mode=\"online\" " \
                    "organizer_company_id=\"1\" title=\"Los Morancos\"><event event_date=\"2021-07-31T20:00:00\" " \
                    "event_id=\"1642\" sell_from=\"2021-06-26T00:00:00\" sell_to=\"2021-07-31T19:50:00\" " \
                    "sold_out=\"false\"><zone zone_id=\"186\" capacity=\"0\" price=\"75.00\" name=\"Amfiteatre\" " \
                    "numbered=\"true\" /><zone zone_id=\"186\" capacity=\"14\" price=\"65.00\" name=\"Amfiteatre\" " \
                    "numbered=\"false\" /></event></base_event><base_event base_event_id=\"444\" sell_mode=\"offline\" " \
                    "organizer_company_id=\"1\" title=\"Tributo a Juanito Valderrama\"><event event_date=\"2021-09-31T20:00:00\" " \
                    "event_id=\"1642\" sell_from=\"2021-02-10T00:00:00\" sell_to=\"2021-09-31T19:50:00\" " \
                    "sold_out=\"false\"><zone zone_id=\"7\" capacity=\"22\" price=\"65.00\" name=\"Amfiteatre\" " \
                    "numbered=\"false\" /></event></base_event></output></eventList>"

    sample_xml_11 = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><eventList version=\"1.0\" " \
                    "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" " \
                    "xsi:noNamespaceSchemaLocation=\"eventList.xsd\"><output><base_event base_event_id=\"291\" " \
                    "sell_mode=\"online\" title=\"Camela en concierto\"><event event_date=\"2021-06-30T21:00:00\" " \
                    "event_id=\"291\" sell_from=\"2020-07-01T00:00:00\" sell_to=\"2021-06-30T20:00:00\" " \
                    "sold_out=\"false\"><zone zone_id=\"40\" capacity=\"200\" price=\"20.00\" name=\"Platea\" " \
                    "numbered=\"true\" /><zone zone_id=\"38\" capacity=\"0\" price=\"15.00\" name=\"Grada 2\" " \
                    "numbered=\"false\" /><zone zone_id=\"30\" capacity=\"80\" price=\"30.00\" name=\"A28\" " \
                    "numbered=\"true\" /></event></base_event><base_event base_event_id=\"1591\" sell_mode=\"online\" " \
                    "organizer_company_id=\"1\" title=\"Los Morancos\"><event event_date=\"2021-07-31T20:00:00\" " \
                    "event_id=\"1642\" sell_from=\"2021-06-26T00:00:00\" sell_to=\"2021-07-31T19:50:00\" " \
                    "sold_out=\"false\"><zone zone_id=\"186\" capacity=\"0\" price=\"75.00\" name=\"Amfiteatre\" " \
                    "numbered=\"true\" /><zone zone_id=\"186\" capacity=\"12\" price=\"65.00\" name=\"Amfiteatre\" " \
                    "numbered=\"false\" /></event></base_event><base_event base_event_id=\"444\" sell_mode=\"offline\" " \
                    "organizer_company_id=\"1\" title=\"Tributo a Juanito Valderrama\"><event event_date=\"2021-09-31T20:00:00\"" \
                    " event_id=\"1642\" sell_from=\"2021-02-10T00:00:00\" sell_to=\"2021-09-31T19:50:00\" " \
                    "sold_out=\"false\"><zone zone_id=\"7\" capacity=\"22\" price=\"65.00\" name=\"Amfiteatre\" " \
                    "numbered=\"false\" /></event></base_event></output></eventList>"
