# Weather Advisory gRPC Service

## Overview
My project is a gRPC-based Weather Advisory Service that interacts with the OpenWeatherMap API to provide weather updates, air quality data, and travel recommendations based on real-time weather conditions.

## Prerequisites For My Project

Before running the project, ensure you have the following installed:

- Python 3.8+
- gRPC and its tools
- Docker
- OpenWeatherMap API Key

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/project-2-Kushal-Chandani.git
cd project-2-Kushal-Chandani
```

### 2. Install Dependencies
Install the required dependencies, for installation commands I think you can use stackoverflow or even AI.

### 3. Set Environment Variables
Set the required environment variables for the server.

```sh
export OPENWEATHER_API_KEY="your personal api key (insert in this string)"
export SERVER_PORT=9999
```

## Running the Server

Start the gRPC server by executing:

```sh
python server.py
```

You should see:
```sh
Starting server on port 9999
Server started successfully
```

## Running the Client

Run the client to fetch air quality, weather, or travel recommendations:

### 1. Get Air Quality
```sh
tools\client\client-windows-amd64.exe air-quality -city "New York"
```

### 2. Get Weather
```sh
tools\client\client-windows-amd64.exe weather -city "Blacksburg"
```

### 3. Get Travel Recommendation
```sh
tools\client\client-windows-amd64.exe travel -city "Karachi"
```

## Notes
- Ensure your OpenWeatherMap API key is valid. Its free.
- The service listens on `localhost:9999` by default (but can be changed via `SERVER_PORT`.)

Now you can successfully run.

