# set base image (host OS)
FROM python:3.10-alpine

# set the working directory in the container
WORKDIR /status_state_controller

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies

RUN python -m pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src_controller/ .

# command to run on container start
CMD ["python3","./main.py"] 

