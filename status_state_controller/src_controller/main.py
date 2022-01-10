import docker
import requests
from django.shortcuts import render
import logging 
import os
import json
import time

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


def get_containers() :

    try:
        api_url = "http://localhost:8080/status_state_api"
        response = requests.get(api_url)
        data = response.content
        json_data = json.loads(data)
    except requests.exceptions.RequestException as e:  
        logging.info(e)
        raise SystemExit(e)

    return json_data


def control_containers(status_state_list,current_list):
    client = docker.from_env(assert_hostname=False)
    first_ids =  [x['id'] for x in status_state_list]
    current_ids =  [x['id'] for x in current_list]
    
    #restart any stopped container found in the status_state_list
    try:
        for id in first_ids:
            if id not in current_ids :  
                current_container = client.containers.get(id)      #container[3] == "stopped" : 
                current_container.restart()
                logging.info('%s restarted',current_container)
    
    except Exception:
        logging.info('some stopped containers could not be started',current_container)
        pass          

    #delete any container that is not found in the status_state_list
    try :
        for id in current_ids:
            if id not in first_ids : 
                current_container = client.containers.get(id)
                current_container.stop()
                logging.info('%s stopped',current_container)
                
    except Exception:
        logging.info('Some containers could not be stopped',current_container)
        pass

    logging.info('Containers running at startup : %s',status_state_list)
    logging.info('currently working containers : %s',current_list)

def main():
    status_state_list = get_containers()
    time.sleep(30)
    current_list = get_containers()
    control_containers(status_state_list,current_list)
    while True :
        time.sleep(30)
        current_list = get_containers()
        control_containers(status_state_list,current_list)   


if __name__ == '__main__':
    main()
    