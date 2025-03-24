# openweather.DefaultApi

All URIs are relative to *https://api.openweathermap.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data25_air_pollution_get**](DefaultApi.md#data25_air_pollution_get) | **GET** /data/2.5/air_pollution | Get air quality data
[**data25_forecast_get**](DefaultApi.md#data25_forecast_get) | **GET** /data/2.5/forecast | Get 5-day/3-hour weather forecast
[**data25_weather_get**](DefaultApi.md#data25_weather_get) | **GET** /data/2.5/weather | Get current weather data for a city
[**geo10_direct_get**](DefaultApi.md#geo10_direct_get) | **GET** /geo/1.0/direct | Geocode a location


# **data25_air_pollution_get**
> Data25AirPollutionGet200Response data25_air_pollution_get(lat, lon, appid)

Get air quality data

Fetch air quality data for specific coordinates.

### Example


```python
import openweather
from openweather.models.data25_air_pollution_get200_response import Data25AirPollutionGet200Response
from openweather.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.openweathermap.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openweather.Configuration(
    host = "https://api.openweathermap.org"
)


# Enter a context with an instance of the API client
with openweather.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openweather.DefaultApi(api_client)
    lat = 3.4 # float | Latitude of the location (e.g., \"51.5074\").
    lon = 3.4 # float | Longitude of the location (e.g., \"-0.1278\").
    appid = 'appid_example' # str | API key for authentication.

    try:
        # Get air quality data
        api_response = api_instance.data25_air_pollution_get(lat, lon, appid)
        print("The response of DefaultApi->data25_air_pollution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->data25_air_pollution_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude of the location (e.g., \&quot;51.5074\&quot;). | 
 **lon** | **float**| Longitude of the location (e.g., \&quot;-0.1278\&quot;). | 
 **appid** | **str**| API key for authentication. | 

### Return type

[**Data25AirPollutionGet200Response**](Data25AirPollutionGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for air quality data |  -  |
**401** | Unauthorized - Invalid API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data25_forecast_get**
> Data25ForecastGet200Response data25_forecast_get(q, appid)

Get 5-day/3-hour weather forecast

Retrieve weather forecasts at 3-hour intervals for the next 5 days.

### Example


```python
import openweather
from openweather.models.data25_forecast_get200_response import Data25ForecastGet200Response
from openweather.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.openweathermap.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openweather.Configuration(
    host = "https://api.openweathermap.org"
)


# Enter a context with an instance of the API client
with openweather.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openweather.DefaultApi(api_client)
    q = 'q_example' # str | Name of the city (or city, state, and country).
    appid = 'appid_example' # str | API key for authentication.

    try:
        # Get 5-day/3-hour weather forecast
        api_response = api_instance.data25_forecast_get(q, appid)
        print("The response of DefaultApi->data25_forecast_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->data25_forecast_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Name of the city (or city, state, and country). | 
 **appid** | **str**| API key for authentication. | 

### Return type

[**Data25ForecastGet200Response**](Data25ForecastGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for weather forecast data |  -  |
**401** | Unauthorized - Invalid API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data25_weather_get**
> Data25WeatherGet200Response data25_weather_get(q, appid)

Get current weather data for a city

Fetch current weather details such as temperature, humidity, and weather description.

### Example


```python
import openweather
from openweather.models.data25_weather_get200_response import Data25WeatherGet200Response
from openweather.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.openweathermap.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openweather.Configuration(
    host = "https://api.openweathermap.org"
)


# Enter a context with an instance of the API client
with openweather.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openweather.DefaultApi(api_client)
    q = 'q_example' # str | Name of the city (or city, state, and country).
    appid = 'appid_example' # str | API key for authentication.

    try:
        # Get current weather data for a city
        api_response = api_instance.data25_weather_get(q, appid)
        print("The response of DefaultApi->data25_weather_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->data25_weather_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Name of the city (or city, state, and country). | 
 **appid** | **str**| API key for authentication. | 

### Return type

[**Data25WeatherGet200Response**](Data25WeatherGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for current weather data |  -  |
**401** | Unauthorized - Invalid API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo10_direct_get**
> List[Geo10DirectGet200ResponseInner] geo10_direct_get(q, appid, limit=limit)

Geocode a location

Fetch geographic coordinates for a given city, state, and country.

### Example


```python
import openweather
from openweather.models.geo10_direct_get200_response_inner import Geo10DirectGet200ResponseInner
from openweather.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.openweathermap.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openweather.Configuration(
    host = "https://api.openweathermap.org"
)


# Enter a context with an instance of the API client
with openweather.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openweather.DefaultApi(api_client)
    q = 'q_example' # str | Name of the city (or city, state, and country).
    appid = 'appid_example' # str | API key for authentication.
    limit = 5 # int | Maximum number of results to return. (optional) (default to 5)

    try:
        # Geocode a location
        api_response = api_instance.geo10_direct_get(q, appid, limit=limit)
        print("The response of DefaultApi->geo10_direct_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->geo10_direct_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Name of the city (or city, state, and country). | 
 **appid** | **str**| API key for authentication. | 
 **limit** | **int**| Maximum number of results to return. | [optional] [default to 5]

### Return type

[**List[Geo10DirectGet200ResponseInner]**](Geo10DirectGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for geocoding data |  -  |
**401** | Unauthorized - Invalid API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

