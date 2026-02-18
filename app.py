from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "/data/notes.json"

if not os.path.exists("/data"):
    os.makedirs("/data")

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.route("/")
def home():
    return {"message": "API running on AWS EC2"}

@app.route("/notes", methods=["GET"])
def get_notes():
    with open(DATA_FILE, "r") as f:
        notes = json.load(f)
    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def add_note():
    note = request.json

    with open(DATA_FILE, "r") as f:
        notes = json.load(f)

    notes.append(note)

    with open(DATA_FILE, "w") as f:
        json.dump(notes, f)

    return {"message": "Note added"}, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
