# set base image 
FROM python:3.8-alpine

# set the working directory in the container
WORKDIR /status_state_controller

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src_controller/ .

# command to run on container start
CMD ["python3","./main.py"] 

