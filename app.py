from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

options = ("rock", "paper", "scissors")

@app.route('/', methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        data = request.get_json()
        player = data['choice']
        computer = random.choice(options)

        if player == computer:
            result = "It's a tie!"
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            result = "You win!"
        else:
            result = "You lose!"

        return jsonify(player=player, computer=computer, result=result)
    else:
        return render_template('index.html', rock_id="rock", paper_id="paper", scissors_id="scissors")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
