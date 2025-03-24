FROM python:3.12-slim
# The Dockerfile should copy the portfolio directory and install all the requirements.
# Then it should run the app.py when the container starts.
# Define the directory where the application will reside
RUN mkdir /app
WORKDIR /app

# Transfer the portfolio folder contents to the container's working directory
COPY ./portfolio/ /app/

# Set up the required packages listed in requirements.txt
RUN pip install --no-cache-dir --requirement requirements.txt

# Make port 5000 available for the application
EXPOSE 5000

# Launch the application when container starts
ENTRYPOINT ["python", "app.py"]