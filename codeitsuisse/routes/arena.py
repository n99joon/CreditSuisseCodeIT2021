import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)



@app.route('/tic-tac-toe', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("battleId")
    testing = requests.get('/tic-tac-toe/start/'+inputValue).content
    return json.dumps(testing)
    #logging.info("My result :{}".format(result))
    #return json.dumps(result)


