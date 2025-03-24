# Data25WeatherGet200ResponseMain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**temp** | **float** |  | [optional] 
**feels_like** | **float** |  | [optional] 
**humidity** | **float** |  | [optional] 

## Example

```python
from openweather.models.data25_weather_get200_response_main import Data25WeatherGet200ResponseMain

# TODO update the JSON string below
json = "{}"
# create an instance of Data25WeatherGet200ResponseMain from a JSON string
data25_weather_get200_response_main_instance = Data25WeatherGet200ResponseMain.from_json(json)
# print the JSON string representation of the object
print(Data25WeatherGet200ResponseMain.to_json())

# convert the object into a dict
data25_weather_get200_response_main_dict = data25_weather_get200_response_main_instance.to_dict()
# create an instance of Data25WeatherGet200ResponseMain from a dict
data25_weather_get200_response_main_from_dict = Data25WeatherGet200ResponseMain.from_dict(data25_weather_get200_response_main_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


