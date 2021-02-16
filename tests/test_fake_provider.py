from providers.fake_provider import FakeProvider, FakeResponses
from unittest import TestCase
from unittest.mock import Mock

from utils.xml_parser import XMLParser


class TestFakeProvider(TestCase):
    DATE = "2021-02-09"
    CODE = 200

    def test_fake_provider_events(self):
        # arrange
        mock_response = FakeResponses.events_xml(self.DATE)
        # act
        response = FakeProvider.events_on_date(self.DATE)
        element = XMLParser.parse_str(response.content)
        # assert
        self.assertEqual(response.status_code, self.CODE)
        self.assertEqual(element.tag, mock_response.tag)

    '''
    If we had a REAL Provider we should be mocking it to test it correctly.
    But as our Provider is a FakeProvider and we need it to deploy the API,
    we will test it as well to guarantee its correctness.

    Also, for educational purposes, we implement a mock for the FakeProvider, 
    -regardless that in this case is not necessary- to demonstrate how we
    would do it for a real one.
    '''
    def test_mock_fake_provider_events(self):
        # arrange
        mock_response = FakeResponses.events_xml(self.DATE)
        mock_events_api = Mock(FakeProvider)
        mock_events_api.return_value.status = self.CODE
        mock_events_api.return_value.json.content = mock_response
        # act
        response = FakeProvider.events_on_date(self.DATE)

        element = XMLParser.parse_str(response.content)
        # assert
        self.assertEqual(response.status_code, self.CODE)
        self.assertEqual(element.tag, mock_response.tag)
