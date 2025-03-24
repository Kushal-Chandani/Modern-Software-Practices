FROM python:3.8

ENV REDIS_HOST redis
ENV DB_HOST postgres
ENV DB_NAME shortener
ENV DB_USER user
ENV DB_PASS password
ENV HOSTNAME unknown

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY service.py .
COPY static/ ./static

EXPOSE 5000

CMD ["python", "service.py"]