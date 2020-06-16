docker_app='application_my_app'

docker rm $(docker ps -aqf "name=$docker_app")
docker rmi $(docker images -q "$docker_app" | uniq)
