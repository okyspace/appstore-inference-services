IMAGE=<repo/image/tag>

docker build -t $IMAGE .
docker push $IMAGE
