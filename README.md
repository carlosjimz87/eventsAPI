# **Events API Fever**

![CI](https://github.com/carlosjimz87/eventsAPI/workflows/CI/badge.svg)
![python](https://img.shields.io/badge/python-3.9.1-purple?logo=python)

This is an API to gather events summaries given a timeframe of dates. Is made with [FastAPI](https://fastapi.tiangolo.com/) and it use important features of the [Python](https://www.python.org/) language such as *annotations*, *asynchronous tasks*, *multithreading*, *pydantic classes*, *unit testing* and others.

## Installation

`make setup`

## Tests

`make test`

## Run

`make run`

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

```
--main.py
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
|   |--test_data.py
|   |--test_fake_provider.py
|   |--test_formatter.py
|   |--test_validator.py
|   |--test_xml_parser.py
|
|--utils
    |--formatter.py
    |--remove_errors.py
    |--validator.py
    |--xml_parser.py
```

## Tasks

- [X] Basic API with basic XML parsing.
- [X] Initial refactoring for better scalability.
- [X] Complete XML parsing.
- [X] Asynchronous request to external provider.
- [X] Adapt API to Open API spec. **
- [X] Online events filtering.
- [X] Most recent events filtering.
- [X] Complete routes endpoints and not-founds.
- [X] Final refactoring for better scalability.
- [X] Github actions.
- [X] Deployment setup.
- [X] Performance recommendations.
- [X] Security recommendations.
- [X] Code styling, comments, and other improvements.**
- [X] Error handling and output messages.**
- [X] Testing and mocking.**
- [ ] Cache middleware.
- [X] Complete documentation.

** partially finished tasks (see **Pending Issues** for more)
## Performance Challenges

Because the external provider only gives the events for one specific date, is our responsibility to find all available events in a range of dates. According to the requirements, the endpoint of our API should receive the `starts_at` and `ends_at` params and then return the corresponding events within this timeframe.

One challenge arises from this situation, and it's that we need to request multiple times in case of a wide timeframe. For example, in one year we would have to request 365 times to the provider. That could be really time-consuming if we do it sequentially.

To solve this, we implement `asynchronous requests` for each date and put them into `separated threads`. This approach should improve considerably the performance of the data consumption side.

Now, this brings a new problem. By analyzing the sample data we realized that several events have the same ID in multiple days. And, events now are gathered simultaneously from multiple threads so this means that they arrive unordered to the storage container. This jeopardizes the requirement of having only the most recent event of one unique ID. Of course, we can sort all the events after that, but this will throw down all the good performance we could achieve with the asynchronous-multithreading requests.

To solve this new issue, we can use an efficient sorting method mixed with a **memoization** technique. If we keep track of the events we are retrieving, and we only save the ones with identical ID and only if they have a more recent date, the number of saved events will be considerably less. 

There is another possible improvement to apply, and that is a **cache middleware** to avoid unnecessary requests.

## Security Recommendations

On the *implementation side* a real api like this, would need some way of authorization and tokenization of endpoints, an acceptable approach could be using **OAUTH2** and **JWT tokens**. Also, it needs protection against XSS & SQL Injections and ManInTheMiddle attacks, for this is important to extend validations, create secure SQL queries, secure string concatenation and encode data before send it via HTTP. Besides, these measures might help to mitigate the data leaks and contributes with data privacy and integrity. One of the most dangerous attacks to face are DDOS attacks, to help with that API should implement efficient pagination on large responses.

On other hand, in the *infrastructure side*, some of the most important protections are load balancing, proxies, black/white lists, id secularization, OAUTH servers and others.

## Pending Issues

Because of the time constraints, some tasks were partially finished in our consideration. Although we want to explain what should be done in the following lines.

In general, the code is good enough for this kind of project, but we think that some principles and good practices could be taken to a higher level. The asynchronous requests could be more efficient as the loop with nested requests is not the best solution. Comments and style can definately be improved and finally, the error handling needs a more concise and well-structured approach.

Testing and mock of objects can be and should be done thoroughly to really get good quality on our code. More test cases are needed in all modules and methods because only the basic tests were performed. By using better mocks and parameterized tests we can get better coverage.

Also, the adaption to OpenAPI specification is slightly incomplete. Some unnecessary models of the Schema could not be hidden.

Lastly, cache middleware was not implemented also because of a lack of time, but as we clarify earlier could be a solid performance catalyzer.
## Acknowledgments

We want to thanks to the [FastAPI team](https://github.com/tiangolo/fastapi/graphs/contributors) for facilitating the development of this project.
