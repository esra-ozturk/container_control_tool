# set base image (host OS)
FROM python:3.8-slim-buster

# set the working directory in the container
WORKDIR /status_state_container

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .
EXPOSE 8080:8080
# command to run on container start
CMD ["python3","app.py"] 

