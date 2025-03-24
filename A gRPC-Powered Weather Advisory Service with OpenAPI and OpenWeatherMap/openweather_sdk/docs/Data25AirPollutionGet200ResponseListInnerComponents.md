# Data25AirPollutionGet200ResponseListInnerComponents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pm2_5** | **float** |  | [optional] 
**pm10** | **float** |  | [optional] 
**co** | **float** |  | [optional] 

## Example

```python
from openweather.models.data25_air_pollution_get200_response_list_inner_components import Data25AirPollutionGet200ResponseListInnerComponents

# TODO update the JSON string below
json = "{}"
# create an instance of Data25AirPollutionGet200ResponseListInnerComponents from a JSON string
data25_air_pollution_get200_response_list_inner_components_instance = Data25AirPollutionGet200ResponseListInnerComponents.from_json(json)
# print the JSON string representation of the object
print(Data25AirPollutionGet200ResponseListInnerComponents.to_json())

# convert the object into a dict
data25_air_pollution_get200_response_list_inner_components_dict = data25_air_pollution_get200_response_list_inner_components_instance.to_dict()
# create an instance of Data25AirPollutionGet200ResponseListInnerComponents from a dict
data25_air_pollution_get200_response_list_inner_components_from_dict = Data25AirPollutionGet200ResponseListInnerComponents.from_dict(data25_air_pollution_get200_response_list_inner_components_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


