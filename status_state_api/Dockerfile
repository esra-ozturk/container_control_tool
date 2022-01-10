# set base image 
FROM python:3.8-alpine

# set the working directory in the container
WORKDIR /status_state_api

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN  pip3 install --upgrade pip
RUN  pip3 install -r requirements.txt

# copy the content of the local files to the working directory
COPY src_status/ .

EXPOSE 8080
# command to run on container start
CMD ["python3","./app.py"] 

