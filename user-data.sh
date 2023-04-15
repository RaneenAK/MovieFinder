#!/bin/bash

# Install Docker and Git
yum update -y
amazon-linux-extras install docker -y
yum install -y git
service docker start
usermod -a -G docker ec2-user

# Clone the latest version of the code from GitHub
git clone https://github.com/RaneenAK/PosterFinder.git 


# Connect to the MongoDB container and run mongo shell
docker pull mongodb/mongodb-community-server
docker run --name mongo -d mongodb/mongodb-community-server:latest


# Build the Flask application image
cd /home/ec2-user/PosterFinder
docker build -t flask-img -f Dockerfile .


## Start the Flask application container
docker run -d --name flask-container -p 5000:5000 --link mongo:mongo -e FLASK_RUN_HOST=0.0.0.0 flask-img


