from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ai-move", methods=["POST"])
def ai_move():
    board = request.json["board"]
    empty_cells = [i for i, cell in enumerate(board) if cell == ""]
    
    if empty_cells:
        move = random.choice(empty_cells)
        return jsonify({"move": move})
    
    return jsonify({"move": None})

if __name__ == "__main__":
    app.run(debug=True)
