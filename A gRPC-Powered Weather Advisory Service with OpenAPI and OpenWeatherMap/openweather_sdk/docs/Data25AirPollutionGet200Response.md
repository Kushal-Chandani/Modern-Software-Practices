# Data25AirPollutionGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[Data25AirPollutionGet200ResponseListInner]**](Data25AirPollutionGet200ResponseListInner.md) |  | [optional] 

## Example

```python
from openweather.models.data25_air_pollution_get200_response import Data25AirPollutionGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Data25AirPollutionGet200Response from a JSON string
data25_air_pollution_get200_response_instance = Data25AirPollutionGet200Response.from_json(json)
# print the JSON string representation of the object
print(Data25AirPollutionGet200Response.to_json())

# convert the object into a dict
data25_air_pollution_get200_response_dict = data25_air_pollution_get200_response_instance.to_dict()
# create an instance of Data25AirPollutionGet200Response from a dict
data25_air_pollution_get200_response_from_dict = Data25AirPollutionGet200Response.from_dict(data25_air_pollution_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


