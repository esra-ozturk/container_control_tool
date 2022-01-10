container_control_tool

Clone the Repository - git clone https://github.com/esra-ozturk/container_control_tool.git

Move to the directory - cd status_state_api   

Build the docker image - docker image build -t status_api .

Create and run a container - docker container run -d -p 8080:8080 status_api

Navigate to http://localhost:8080/status_state_api to see json file

Move to the directory - cd status_state_controller

Build the docker image - docker image build -t controller .

Create and run a container - docker container run -d controller

Why Flask framework ?
Flask needs little dependency to update and it is lightweight and flexible
My reason for choosing the flask: Deploying a Flask application with Docker will allow US to replicate the application across different servers with minimal reconfiguration.



To improve our project : In the first step, it can be good idea to create a microservice.
In the second step, cron job should 



Bonus : Deploy the tool to a kubernetes cluster(using Minikube)
In addition to the steps already done above, the following prerequisites are also required :
Docker Desktop & Minikube & Kubernetes CLI installed on your computer.

Steps to deploy tool to Kubernetes cluster: 

Create a new file called deployment.yaml. 

kubectl apply -f deployment.yaml

minikube dashboard

To access the application :

minikube start service: flask-test-service
