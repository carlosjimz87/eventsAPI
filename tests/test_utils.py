from unittest import TestCase
from utils.xml_parser import XMLParser


class TestUtils(TestCase):

    xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><eventList version=\"1.0\" " \
          "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" " \
          "xsi:noNamespaceSchemaLocation=\"eventList.xsd\"><output><base_event base_event_id=\"291\" " \
          "sell_mode=\"online\" title=\"Camela en concierto\"><event event_date=\"2021-06-30T21:00:00\" " \
          "event_id=\"291\" sell_from=\"2020-07-01T00:00:00\" sell_to=\"2021-06-30T20:00:00\" " \
          "sold_out=\"false\"><zone zone_id=\"40\" capacity=\"243\" price=\"20.00\" name=\"Platea\" numbered=\"true\" " \
          "/><zone zone_id=\"38\" capacity=\"100\" price=\"15.00\" name=\"Grada 2\" numbered=\"false\" /><zone " \
          "zone_id=\"30\" capacity=\"90\" price=\"30.00\" name=\"A28\" numbered=\"true\" " \
          "/></event></base_event><base_event base_event_id=\"322\" sell_mode=\"online\" organizer_company_id=\"2\" " \
          "title=\"Pantomima Full\"><event event_date=\"2021-02-10T20:00:00\" event_id=\"1642\" " \
          "sell_from=\"2021-01-01T00:00:00\" sell_to=\"2021-02-09T19:50:00\" sold_out=\"false\"><zone zone_id=\"311\" " \
          "capacity=\"2\" price=\"55.00\" name=\"A42\" numbered=\"true\" /></event></base_event><base_event " \
          "base_event_id=\"1591\" sell_mode=\"online\"  organizer_company_id=\"1\" title=\"Los Morancos\"><event " \
          "event_date=\"2021-07-31T20:00:00\" event_id=\"1642\" sell_from=\"2021-06-26T00:00:00\" " \
          "sell_to=\"2021-07-31T19:50:00\" sold_out=\"false\"><zone zone_id=\"186\" capacity=\"2\" price=\"75.00\" " \
          "name=\"Amfiteatre\" numbered=\"true\" /><zone zone_id=\"186\" capacity=\"16\" price=\"65.00\" " \
          "name=\"Amfiteatre\" numbered=\"false\" /></event></base_event></output></eventList> "

    def test_xml_parser_from_file(self):
        element = XMLParser.parse_file(XMLParser.MOCK_RESPONSE_11)
        self.assertEqual(element.tag, "eventList")

    def test_xml_parser_from_str(self):
        element = XMLParser.parse_str(self.xml)
        self.assertEqual(element.tag, "eventList")
