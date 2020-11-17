# app.py
from flask import Flask, request, jsonify, render_template
from sortedcontainers import SortedDict 
import pickle
import os
from datetime import datetime as dt
tetris = Flask(__name__)

if 'high_scores.pickle' in os.listdir():
    high_scores_file = open('high_scores.pickle','rb')
    high_scores = pickle.load(high_scores_file)
else:
    high_scores = SortedDict()

@tetris.route('/update_list', methods = ['POST'])
def update_list():
    name = request.form.get('name')
    score = request.form.get('score')
    if score in high_scores.keys():
        high_scores[score].append({'name':name,'score':score,'id':str(dt.now().timestamp())})
    else:
        high_scores[score] = [{'name':name,'score':score,'id':str(dt.now().timestamp())}]
    high_scores_file = open('high_scores.pickle','wb')
    pickle.dump(high_scores,high_scores_file)
    return render_template("scores.html")

@tetris.route('/show_scores')
def show_scores():
    return render_template("scores.html")

@tetris.route('/get_high_scores', methods = ['GET'])
def get_list():
    high_scores_top = list(high_scores.keys())
    high_scores_top.reverse()
    high_scores_list = [value for k in high_scores_top for value in high_scores[k] ]
    data = {
    "data": high_scores_list
      }
    return jsonify(data)



# A welcome message to test our server
@tetris.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    tetris.run(threaded=True, port=5000)