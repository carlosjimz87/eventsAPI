from xml.etree.ElementTree import Element
from utils.xml_parser import XMLParser


class FakeResponses:
    @staticmethod
    def events_urls(date):
        dates_urls = {
            "2021-02-09": (
                "https://gist.githubusercontent.com/miguelgf/"
                "fac9761c528befe700be6f94cdccdaa9/raw/"
                "80e552779c5c108bf0d076395bc5421784251bc0/response_2021-02-09.xml"
            ),
            "2021-09-10": (
                "https://gist.githubusercontent.com/miguelgf/"
                "38c5a6f6bc7630f9c8fd0a23f4c8327f/raw/"
                "203d2d556274369d5f035f079a49a0a45e77b872/response_2021-02-10.xml"
            ),
            "2021-09-11": (
                "https://gist.githubusercontent.com/miguelgf/"
                "37f1bea60e0fa262680e6e5031cfb038/raw/"
                "5df981e215949ba04a342acc7a36a18ea1c1310a/response_2021-02-11.xml"
            ),
        }
        return dates_urls[date]

    @staticmethod
    def events_xml(date: str) -> Element:
        dates_xmls = {
            "2021-02-09": XMLParser.parse_str(XMLParser.sample_xml_09),
            "2021-02-10": XMLParser.parse_str(XMLParser.sample_xml_10),
            "2021-02-11": XMLParser.parse_str(XMLParser.sample_xml_11),

        }

        return dates_xmls[date]
