@echo off
docker build --tag=web_mars .
docker run -p 5701:5005 --name=web_mars --rm web_mars