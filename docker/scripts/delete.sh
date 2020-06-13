docker_app='docker_flask_web'

docker rm $(docker ps -aqf "name=$docker_app")
docker rmi $(docker images -q "$docker_app" | uniq)
