# Use docker image python, version 3
FROM python:3

# Define & create working directory in Docker image instance
WORKDIR /usr/src/app

# USER 0
# RUN chown -R 1001:0 ./

# Copy requirements.txt to "root of WORKDIR" - for all the dependencies
COPY requirements.txt ./requirements.txt

# Run the requirements.txt in Docker
# USER 1001

RUN pip install -r requirements.txt

# Copy from "/app" directory TO "root of WORKDIR"
COPY ./app .

# The container listens on port 4000
EXPOSE 4000

# Switch back to /src folder
WORKDIR /usr/src

# Command to use for starting the application
CMD [   "gunicorn", "app.main:app", \
        "--bind", "0.0.0.0:4000", \
        "--workers", "1", \
        "--worker-class", "uvicorn.workers.UvicornWorker"]