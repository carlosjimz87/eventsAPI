# **Events API Fever**

This is an API to gather events summary given a timeframe of dates. Is made with [FastAPI](https://fastapi.tiangolo.com/) and is use important features of the [Python](https://www.python.org/) language such as *annotations*, *asynchronous tasks*, *multithreading*, *pydantic classes*, *unit testing* and others.


## Description

We have an external provider that gives us some events from their company, and we want to integrate them on our stack, in order to do that, we are developing this microservice.

The provider will have one endpoint, where they will give us their list of events on `XML`. Every day we fetch the events, the endpoint will give us the current events available on their side. Here we provide some examples of three different calls to that endpoint on three different days.

Check the following links as **sample data**  to see responses on the following dates:

- [2021/02/09](https://gist.githubusercontent.com/miguelgf/fac9761c528befe700be6f94cdccdaa9/raw/80e552779c5c108bf0d076395bc5421784251bc0/response_2021-02-09.xml)

- [2021/02/10](https://gist.githubusercontent.com/miguelgf/38c5a6f6bc7630f9c8fd0a23f4c8327f/raw/203d2d556274369d5f035f079a49a0a45e77b872/response_2021-02-10.xml)

- [2021/02/11](https://gist.githubusercontent.com/miguelgf/37f1bea60e0fa262680e6e5031cfb038/raw/5df981e215949ba04a342acc7a36a18ea1c1310a/response_2021-02-11.xml)


As you can see, the events that aren't available anymore aren't shown on their API anymore.

**OUR MISSION** is to develop and expose just one endpoint, and should respect this [**Open API Spec**](https://app.swaggerhub.com/apis-docs/luis-pintado-feverup/backend-test/1.0.0) spec with the formatted and normalized data from the external provider.

Our endpoint should accept a `starts_at` and `ends_at` params, and return only the events within this time range.
- We should only receive the available events (the sell mode is online, the rest should be ignored)
- We should be able to request to this endpoint events from the past (since we have the app running) and the future. 
  
**Example**: If we deploy our application on *2021-02-01*, and we request the events from *2021-02-01* to *2022-02-02*, we should
see in our endpoint the events *291*, *322* and *1591* with their latest known values. 

## Project Structure

```bash
--main.py
--Makefile
--poetry.lock
--pyproject.toml
--requirements.txt
|--api
|   |--events_api.py
|   |--router.py
|
|--models
|   |--errors.py
|   |--events.py
|   |--queries.py
|   |--responses.py
|
|--providers
|   |--fake_provider.py
|   |__fake_responses.py
|
|--tests
|   |--test_api.py
|   |--test_fake_provider.py
|   |--test_validator.py
|   |--test_formatter.py
|   |--test_xml_parser.py
|
|--utils
    |--mock_response.py
    |--mock_response_10.py
    |--mock_response_11.py
```

## Tasks

- [X] Basic API with basic XML parsing.
- [X] Initial refactoring for better scalability.
- [X] Complete XML parsing.
- [X] Asynchronous request to external provider.
- [X] Adapt API to Open API spec.
- [X] Online events filtering.
- [X] Most recent events filtering.
- [ ] Cache middleware.
- [X] Complete routes endpoints and not-founds.
- [/] Error handling and output messages.
- [/] Testing and mocking.
- [/] Final refactoring for better scalability.
- [/] Code styling, comments, and other improvements.
- [ ] Github actions.
- [X] Deployment setup.
- [X] Performance recommendations.
- [ ] Security recommendations.
- [ ] Complete documentation.


## Performance Challenges

Because the external provider only gives the events for one specific date, is our responsibility to find all available events in a range of dates. According to the requirements, the endpoint of our API should receive the `starts_at` and `ends_at` params and then return the corresponding events within this timeframe.

One challenge arises from this situation, and it's that we need to request multiple times in case of a wide timeframe. For example, in one year we would have to request 365 times to the provider. That could be really time-consuming if we do it sequentially.

To solve this, we implement `asynchronous requests` for each date and put them into `separated threads`. This approach should improve considerably the performance of the data consumption side.

Now, this brings a new problem. By analyzing the sample data we realized that several events have the same ID in multiple days. And, events now are gathered simultaneously from multiple threads so this means that they arrive unordered to the storage container. This jeopardizes the requirement of having only the most recent event of one unique ID. Of course, we can sort all the events after that, but this will throw down all the good performance we could achieve with the asynchronous-multithreading requests.

To solve this new issue, we can use an efficient sorting method mixed with a **memoization** technique. If we keep track of the events we are retrieving and we only save the ones with identical ID and only if they have a more recent date, the number of saved events will be considerably less. 

There is another possible improvement to apply, and that is a *cache middleware* to avoid unnecessary requests.

## Acknowledgments

We want to thanks to the [FastAPI team](https://github.com/tiangolo/fastapi/graphs/contributors) for facilitating the development of this project.
