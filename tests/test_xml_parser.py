from unittest import TestCase

from tests.test_data import TestData
from utils.xml_parser import XMLParser


class TestXmlParser(TestCase):

    def test_parse_str(self):
        # act
        tree09 = XMLParser.parse_str(TestData.sample_xml_09)
        # verify
        self.assertEqual(tree09.tag, "eventList")

    def test_parse_base_event(self):
        # arrange
        tree09 = XMLParser.parse_str(TestData.sample_xml_09)
        # act
        events = XMLParser.parse_base_event(tree09, "2020-02-02")
        # verify
        self.assertEqual(len(events), 3)
        self.assertEqual(events[0].date_query, "2020-02-02")

    def test_parse_event(self):
        # arrange
        treeEvent = XMLParser.parse_str(TestData.event_xml)
        # act
        event = XMLParser.parse_event(treeEvent)
        # verify
        self.assertEqual(int(event["base_event_id"]), 291)
        self.assertEqual(event["sell_mode"], "online")
        self.assertEqual(event["title"], "Camela en concierto")
        self.assertEqual(event["start_date"], "2020-07-01")
        self.assertEqual(event["start_time"], "00:00:00")
        self.assertEqual(event["end_date"], "2021-06-30")
        self.assertEqual(event["end_time"], "20:00:00")
        self.assertEqual(float(event["max_price"]), 30.00)
        self.assertEqual(float(event["min_price"]), 15.00)
