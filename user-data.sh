#!/bin/bash

# Install Docker and Git
sudo yum update -y
sudo amazon-linux-extras install docker -y
sudo yum install -y git
sudo yum install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo systemctl enable docker

sudo curl -SL https://github.com/docker/compose/releases/download/v2.4.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# Clone the latest version of the code from GitHub
git clone https://github.com/RaneenAK/PosterFinder.git

cd PosterFinder
sudo chmod 777 *.sh
sudo docker-compose build
sudo docker-compose up -d


