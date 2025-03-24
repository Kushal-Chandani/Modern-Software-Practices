# Data25ForecastGet200ResponseListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt_txt** | **str** |  | [optional] 
**main** | [**Data25WeatherGet200ResponseMain**](Data25WeatherGet200ResponseMain.md) |  | [optional] 
**weather** | [**List[Data25WeatherGet200ResponseWeatherInner]**](Data25WeatherGet200ResponseWeatherInner.md) |  | [optional] 

## Example

```python
from openweather.models.data25_forecast_get200_response_list_inner import Data25ForecastGet200ResponseListInner

# TODO update the JSON string below
json = "{}"
# create an instance of Data25ForecastGet200ResponseListInner from a JSON string
data25_forecast_get200_response_list_inner_instance = Data25ForecastGet200ResponseListInner.from_json(json)
# print the JSON string representation of the object
print(Data25ForecastGet200ResponseListInner.to_json())

# convert the object into a dict
data25_forecast_get200_response_list_inner_dict = data25_forecast_get200_response_list_inner_instance.to_dict()
# create an instance of Data25ForecastGet200ResponseListInner from a dict
data25_forecast_get200_response_list_inner_from_dict = Data25ForecastGet200ResponseListInner.from_dict(data25_forecast_get200_response_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


