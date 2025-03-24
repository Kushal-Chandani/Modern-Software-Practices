# Data25AirPollutionGet200ResponseListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main** | [**Data25AirPollutionGet200ResponseListInnerMain**](Data25AirPollutionGet200ResponseListInnerMain.md) |  | [optional] 
**components** | [**Data25AirPollutionGet200ResponseListInnerComponents**](Data25AirPollutionGet200ResponseListInnerComponents.md) |  | [optional] 

## Example

```python
from openweather.models.data25_air_pollution_get200_response_list_inner import Data25AirPollutionGet200ResponseListInner

# TODO update the JSON string below
json = "{}"
# create an instance of Data25AirPollutionGet200ResponseListInner from a JSON string
data25_air_pollution_get200_response_list_inner_instance = Data25AirPollutionGet200ResponseListInner.from_json(json)
# print the JSON string representation of the object
print(Data25AirPollutionGet200ResponseListInner.to_json())

# convert the object into a dict
data25_air_pollution_get200_response_list_inner_dict = data25_air_pollution_get200_response_list_inner_instance.to_dict()
# create an instance of Data25AirPollutionGet200ResponseListInner from a dict
data25_air_pollution_get200_response_list_inner_from_dict = Data25AirPollutionGet200ResponseListInner.from_dict(data25_air_pollution_get200_response_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


