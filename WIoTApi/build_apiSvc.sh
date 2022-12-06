docker build -t="wiot-api-svc:1.0.0" .
docker run --rm -d -p 5000:5000 --name wiot-api-svc wiot-api-svc:1.0.0
docker ps