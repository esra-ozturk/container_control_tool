from flask import  Flask,jsonify
import container

app = Flask(__name__)
    
@app.route("/status_state_api", methods=['GET'])
def main():
    result = container.create_container_list()
   
    return jsonify(result)
   
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug = True)



       
