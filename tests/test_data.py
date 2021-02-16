from datetime import datetime, timezone


class TestData:
    STARTS_AT = datetime(day=1, month=2, year=2021, hour=5, minute=20, second=19, microsecond=0, tzinfo=timezone.utc)
    ENDS_AT = datetime(day=2, month=2, year=2022, hour=5, minute=20, second=19, microsecond=0, tzinfo=timezone.utc)
    EVENT_DATE = datetime(day=9, month=2, year=2021, hour=5, minute=20, second=19, microsecond=0, tzinfo=timezone.utc)

    Event = {
        "base_event_id": "291",
        "sell_mode": "online",
        "title": "Camela en concierto",
        "start_date": "2020-07-01",
        "start_time": "00:00:00",
        "end_date": "2021-06-30",
        "end_time": "20:00:00",
        "max_price": "30.00",
        "min_price": "15.00",
    }

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
