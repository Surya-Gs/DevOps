Docker commands



docker info - Display system information
docker version - Display docker installed version
docker login - login to docker registry
docker ps -list all the running containers
docker ps -a -list all the containers
docker stop [containerName] -stop containers
docker kill [containerName] -Kill the container
docker image inspect [image name] -
docker run -it -to create a container with interactive terminal
docker rm [container name] -to remove container 
docker rmi [image name] -to remove image from the registry
docker images - to list the images in docker
docker system prune -a -to remove unused container 
docker build -t [name:tag] - Builds an image using a dockerfile located in same folder
docker build -t [name:tag] -f [filename] -Builds an image using dockerfile located in different path
docker tag [imagename] [name:tag] -tag an existing image

-VOLUMES
docker create volume [volume name] -creates a new volume
docker inspect volume [volume name] -Inspect volume 
docker rm volume [volume name] -remove volume


-DOCKER COMPOSE
docker compose build -build the images
docker compose start -start the containers
docker comosse stop - stop the containers
docker compose up -d -Build and start the containers
docker compose rm -to remove the containers


