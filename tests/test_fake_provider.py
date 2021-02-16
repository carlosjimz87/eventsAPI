from unittest import TestCase
from unittest.mock import patch

from providers.fake_provider import FakeProvider, FakeResponses
from tests.test_data import TestData
from utils.validator import Validator
from utils.xml_parser import XMLParser


class TestFakeProvider(TestCase):

    def test_get_events_on_dates(self):
        # arrange
        start_at = TestData.STARTS_AT
        end_at = TestData.ENDS_AT
        date_list = Validator.range_of_dates(start_at, end_at)
        # act
        events = FakeProvider.get_events_on_dates(date_list)
        # assert
        self.assertNotEqual(events, None)
        self.assertEqual(3, len(events))

        self.assertEqual("291", events[0].base_event_id)
        self.assertEqual("1591", events[1].base_event_id)
        self.assertEqual("322", events[2].base_event_id)

    def test_get_events_on_date(self):
        # arrange
        date = TestData.EVENT_DATE
        # act
        events = FakeProvider().get_events_on_date(date)
        # assert
        self.assertNotEqual(events, None)
        self.assertEqual(len(events), 3)
        self.assertEqual(events[0].base_event_id, "291")
        self.assertEqual(events[1].base_event_id, "322")
        self.assertEqual(events[2].base_event_id, "1591")

    """
    If we had a REAL Provider we should be mocking it to test it correctly.
    But as our Provider is a FakeProvider and we need it to deploy the API,
    we will test it as well to guarantee its correctness.

    Also, for educational purposes, we implement a mock for the FakeProvider,
    -regardless that in this case is not necessary- to demonstrate how we
    would do it for a real one.
    """

    def test_request_events(self):
        # arrange
        date = TestData.EVENT_DATE
        mock_response = FakeResponses.events_xml(date)
        # act
        response = FakeProvider.request_events(date)
        tree = XMLParser.parse_str(response.content)
        # assert
        self.assertNotEqual(response, None)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(tree.tag, mock_response.tag)

    """
    Here the same test but using Mocks
    """

    @patch('providers.fake_provider.FakeProvider.request_events')
    def test_request_events_with_mock(self, request_events):
        # arrange
        date = TestData.EVENT_DATE
        mock_response = FakeResponses.events_xml(date)
        request_events.return_value.status_code = 200
        request_events.return_value.content = mock_response

        # act
        response = FakeProvider.request_events(date)

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, mock_response)
