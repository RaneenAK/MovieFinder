#!/bin/bash
sudo apt-get update
sudo apt-get install -y docker.io
git clone https://github.com/RaneenAK/MovieFinder.git
cd MovieFinder
docker build -t flask-mongo .
docker run -d -p 5000:5000 -p 27017:27017 --name flask-mongo-container flask-mongo
