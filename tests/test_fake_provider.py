from providers.fake_provider import FakeProvider, FakeResponses
from unittest import TestCase
from unittest.mock import Mock


class TestFakeProvider(TestCase):
    DATE = "2021-02-09"
    CODE = 200

    def test_fake_provider_events(self):
        # arrange
        mock_response = FakeResponses.events_xml(self.DATE)
        # act
        content, status = FakeProvider.events_on_date(self.DATE)
        # assert
        self.assertEqual(status, self.CODE)
        self.assertEqual(content.tag, mock_response.tag)

    '''
    If we had a REAL Provider we should be mocking it to test it correctly.
    But as our Provider is a FakeProvider and we need it to deploy the API,
    we will test it as well to guarantee its correctness.

    Also, for educational purposes, we implement a mock for the FakeProvider, 
    -regardless that in this case is not necessary- to demonstrate how we
    would do it for a real one.
    '''

    # @pytest.mark.parametrize(
    #     "date,expectation",
    #     [
    #         ("string", does_not_raise()),
    #         ("", does_not_raise()),
    #         (0, pytest.raises(problems.helpers.InvalidArgs)),
    #         (None, pytest.raises(problems.helpers.InvalidArgs)),
    #     ],
    # )

    def test_mock_fake_provider_events(self):
        # arrange
        mock_response = FakeResponses.events_xml(self.DATE)
        mock_events_api = Mock(FakeProvider)
        mock_events_api.return_value.status = self.CODE
        mock_events_api.return_value.json.content = mock_response
        # act
        content, status = FakeProvider.events_on_date(self.DATE)
        # assert
        self.assertEqual(status, self.CODE)
        self.assertEqual(content.tag, mock_response.tag)
