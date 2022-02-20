# Flag: 
# -it: iteractive; tty layer
# -rm Automatically remove the container when it exits
docker run -it \
    -p 4000:4000 \
    --env-file .env \
    --rm \
    ap-backend