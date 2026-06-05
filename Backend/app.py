from flask import Flask, request, jsonify, redirect, url_for
from Services.Characters import character
from Services.Narrator import storytelling
import json
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMBER_PATH = os.path.join(BASE_DIR, "Services", "Member.txt")
JOURNEY_PATH = os.path.join(BASE_DIR, "Services", "player_journey.txt")

def has_character():
    if not os.path.exists("Services/Member.txt"):
        return False

    with open("Services/Member.txt", "r", encoding='utf-8', errors='ignore') as f:
        return f.read().strip() != ""



@app.route("/")
def startGame():
    if not has_character():
        return jsonify({
            "redirect": "/character"
        })

    return jsonify({
        "message": "Welcome back, Kindred"
    })

@app.route("/character", methods=[ "POST"])
def characterCreation():
    try:

        data = request.json

        kindred = character(data)

        with open(MEMBER_PATH, "w") as f:
            json.dump(kindred.getCharacter() , f, indent=4)

        return jsonify({
            "message": "Kindred registered successfully",
            "character": data
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500
    
    

@app.route("/gameplay", methods=["GET", "POST"])
def gameplay():

    # First visit
    if not os.path.exists(JOURNEY_PATH):
        output = storytelling()

        with open(JOURNEY_PATH, "w", encoding="utf-8") as f:
            json.dump(output, f)

        return jsonify({"message": output})

    # GET = load existing story
    if request.method == "GET":
        with open(JOURNEY_PATH, "r", encoding="utf-8") as f:
            output = json.load(f)

        return jsonify({"message": output})

    # POST = continue story
    data = request.get_json()

    output = storytelling(data)
    print(output)

    with open(JOURNEY_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f)

    return jsonify({"message": output})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)