# https://hub.docker.com/_/postgres
POSTGRES_CONTAINER="ap-postgres-container"

docker pull postgres

if [[ $(docker ps -a --filter="name=$POSTGRES_CONTAINER") == "" ]]
then
  echo "> Creating container $POSTGRES_CONTAINER ..."
  docker run --name $POSTGRES_CONTAINER \
    -e POSTGRES_USER=root \
    -e POSTGRES_PASSWORD=top_secret \
    -e POSTGRES_DB=asianpearl_db \
    -p 5432:5432 \
    -d postgres
else
  if [[ $(docker ps --filter="name=$POSTGRES_CONTAINER") == "" ]]
  then
    echo "> Restarting existing $POSTGRES_CONTAINER"
    docker restart $POSTGRES_CONTAINER
  else
    echo "> Container $POSTGRES_CONTAINER is already running"
  fi
fi

