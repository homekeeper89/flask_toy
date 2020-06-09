docker_app='docker_my_docker_app'

docker rm $(docker ps -aqf "name=$docker_app")
docker rmi $(docker images -q "$docker_app" | uniq)
