import grpc
import os
from concurrent import futures
from openweather.api.default_api import DefaultApi
from openweather.configuration import Configuration
from openweather.api_client import ApiClient
import spec_pb2
import spec_pb2_grpc

#OpenWeather API key ko environment variable se le raha hun, agar available nahi hai to default value hei set kar raha hun
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "95556c56122c84ef73cbff95c28792bd")
SERVER_PORT = os.getenv("SERVER_PORT", "9999")

openweather_config = Configuration()
openweather_config.api_key['appid'] = OPENWEATHER_API_KEY
openweather_client = ApiClient(openweather_config)
openweather_api = DefaultApi(openweather_client)

AQI_MAPPING = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}

#Yahan mein Weather Advisory Service ka class define kar raha hun
class WeatherAdvisoryService(spec_pb2_grpc.WeatherAdvisoryServicer):

    #Air Quality fetch karne ka function
    def GetAirQuality(self, request, context):
        geo_data = openweather_api.geo10_direct_get(q=request.city, appid=OPENWEATHER_API_KEY, limit=1)
        lat, lon = geo_data[0].lat, geo_data[0].lon
        air_quality_data = openweather_api.data25_air_pollution_get(lat=lat, lon=lon, appid=OPENWEATHER_API_KEY)
        aqi_score = air_quality_data.list[0].main.aqi
        aqi_description = AQI_MAPPING[aqi_score]

        return spec_pb2.AirQualityResponse(
            city=request.city,
            air_quality=aqi_description,
            message=f"Air quality in {request.city} is {aqi_description} (AQI {aqi_score})"
        )
    
    #Mausam ka data fetch karne ka function
    def GetWeather(self, request, context):
        weather_data = openweather_api.data25_weather_get(q=request.city, appid=OPENWEATHER_API_KEY)
        temp_celsius = weather_data.main.temp - 273.15
        temp_celsius = round(temp_celsius, 2)

        return spec_pb2.WeatherResponse(
            city=request.city,
            temperature=temp_celsius,
            description=weather_data.weather[0].description
        )

    #Safar ke liye recommendation dene ka function
    def GetTravelRecommendation(self, request, context):
        forecast_data = openweather_api.data25_forecast_get(q=request.city, appid=OPENWEATHER_API_KEY)
        temp_kelvin = forecast_data.list[0].main.feels_like
        temp_celsius = round(temp_kelvin - 273.15, 2)
        if temp_celsius < 15:
            recommendation = "It's chilly, consider wearing a jacket"
        elif temp_celsius > 30:
            recommendation = "It's hot, consider wearing sunscreen"
        else:
            recommendation = "It's perfect, no need to bring an umbrella"

        return spec_pb2.TravelRecommendationResponse(
            city=request.city,
            recommendation=recommendation
        )

#server start karne ka function
def start_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    spec_pb2_grpc.add_WeatherAdvisoryServicer_to_server(WeatherAdvisoryService(), server)
    print(f"Starting server on port {SERVER_PORT}")
    server.add_insecure_port(f"[::]:{SERVER_PORT}")
    server.start()
    print("Server started successfully")
    server.wait_for_termination()

start_server()