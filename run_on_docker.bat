@echo off

REM Terminate previous Docker processes
echo Stopping previous Docker containers
docker-compose down

REM Build and initiate Docker containers
echo Building and starting Docker containers
docker-compose up --build -d --scale iris-app=3