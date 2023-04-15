#!/bin/bash
#
#To stop all running containers, you can use the following command:
sudo docker stop $(sudo docker ps -aq)
#To remove all stopped containers, you can use the following command:
sudo docker rm $(sudo docker ps -aq)


#sudo docker rmi $(docker images -q)

#remove folder
sudo rm -rf ~/PosterFinder_New/

sudo docker system prune -a
sudo docker volume prune

