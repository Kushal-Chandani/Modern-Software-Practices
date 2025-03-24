# Geo10DirectGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**local_names** | **Dict[str, str]** |  | [optional] 
**lat** | **float** |  | [optional] 
**lon** | **float** |  | [optional] 
**country** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from openweather.models.geo10_direct_get200_response_inner import Geo10DirectGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of Geo10DirectGet200ResponseInner from a JSON string
geo10_direct_get200_response_inner_instance = Geo10DirectGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(Geo10DirectGet200ResponseInner.to_json())

# convert the object into a dict
geo10_direct_get200_response_inner_dict = geo10_direct_get200_response_inner_instance.to_dict()
# create an instance of Geo10DirectGet200ResponseInner from a dict
geo10_direct_get200_response_inner_from_dict = Geo10DirectGet200ResponseInner.from_dict(geo10_direct_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


