# coding: utf-8

"""
    OpenWeather Proxy API

    API for fetching weather, air quality, and geocoding data from OpenWeatherMap.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openweather.models.data25_air_pollution_get200_response_list_inner import Data25AirPollutionGet200ResponseListInner

class TestData25AirPollutionGet200ResponseListInner(unittest.TestCase):
    """Data25AirPollutionGet200ResponseListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Data25AirPollutionGet200ResponseListInner:
        """Test Data25AirPollutionGet200ResponseListInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Data25AirPollutionGet200ResponseListInner`
        """
        model = Data25AirPollutionGet200ResponseListInner()
        if include_optional:
            return Data25AirPollutionGet200ResponseListInner(
                main = openweather.models._data_2_5_air_pollution_get_200_response_list_inner_main._data_2_5_air_pollution_get_200_response_list_inner_main(
                    aqi = 56, ),
                components = openweather.models._data_2_5_air_pollution_get_200_response_list_inner_components._data_2_5_air_pollution_get_200_response_list_inner_components(
                    pm2_5 = 1.337, 
                    pm10 = 1.337, 
                    co = 1.337, )
            )
        else:
            return Data25AirPollutionGet200ResponseListInner(
        )
        """

    def testData25AirPollutionGet200ResponseListInner(self):
        """Test Data25AirPollutionGet200ResponseListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
