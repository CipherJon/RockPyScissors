from flask import Flask, request, jsonify, redirect, url_for
from game.game_logic import determine_winner
import random

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data['choice']
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    result = determine_winner(user_choice, computer_choice)
    
    return jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result
    })

@app.route('/shutdown', methods=['GET'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(debug=True)