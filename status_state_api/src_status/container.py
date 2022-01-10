import docker
def create_container_list() :
    status_state_list = []
    client = docker.from_env()
    for container in client.containers.list():
        container_dict = {'container_name':container.name,'image':container.attrs['Config']['Image'],'id':container.id,'status':container.status}
        status_state_list.append(container_dict)
        
    return  status_state_list

