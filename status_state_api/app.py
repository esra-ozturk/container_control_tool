from flask import  Flask,jsonify
import docker

app = Flask(__name__)

def create_container_list() :
    status_state_list = []
    client = docker.from_env()
    for container in client.containers.list():
        container_dict = {'container_name':container.name,'image':container.attrs['Config']['Image'],'id':container.id,'status':container.status}
        status_state_list.append(container_dict)
        
    return  status_state_list
    
@app.route("/status_state_api", methods=['GET'])
def main():
    result = create_container_list()
   
    return jsonify(result)
   
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug = True)



       
