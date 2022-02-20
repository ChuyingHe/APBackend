# https://hub.docker.com/_/postgres
POSTGRES_CONTAINER="ap-backend-postgres"

docker pull postgres

if [[ -z $(docker ps -a --filter="name=$POSTGRES_CONTAINER") ]]
then
  echo "Creating container $POSTGRES_CONTAINER ..."
  docker run --name $POSTGRES_CONTAINER -e POSTGRES_PASSWORD=topsecret -d postgres
else
  if [[ -z $(docker ps --filter="name=$POSTGRES_CONTAINER") ]]
  then
    echo "Container $POSTGRES_CONTAINER is already running"
  else
    echo "Restarting existing $POSTGRES_CONTAINER"
    docker restart $POSTGRES_CONTAINER
  fi
fi

