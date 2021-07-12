								Tasks.io

This is a simple app to store your daily tasks. 

It is developed using Flask and it is dockerized. 

You need to build a docker image using a Dockerfile present in the root directory of the application.

Command to build the docker image -> "$ docker build --tag Tasks.io:latest ."

Command to run the container -> "$ docker run -d -p 5000:5000 --name Taskapp Tasks.io:latest" 
