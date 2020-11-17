# app.py
from flask import Flask, request, jsonify, render_template
import pickle
tetris = Flask(__name__)

@tetris.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@tetris.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

@tetris.route('/update_list', methods = ['POST'])
def update_list():
    name = request.form.get('name')
    score = request.form.get('score')
    print(name, score)
    return render_template("scores.html")

@tetris.route('/show_scores')
def show_scores():
    return render_template("scores.html")

@tetris.route('/get_high_scores', methods = ['GET'])
def get_list():
    data = {
    "data": [
      {
        "id": "1",
        "name": "John Q Public",
        "score": 100,
        
      },
      {
        "id": "1",
        "name": "Larry Bird",
        "score": 200,
        
      }]
      }
    return jsonify(data)



# A welcome message to test our server
@tetris.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    tetris.run(threaded=True, port=5000)