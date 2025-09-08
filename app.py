from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict

from flask import Flask, request, jsonify, render_template_string

from age_of_sigmar.figurines import FIGURINES, Figurine

app = Flask(__name__)

DATA_FILE = Path("collection.json")


def load_collection() -> List[Dict[str, str]]:
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []


def save_collection(collection: List[Dict[str, str]]) -> None:
    DATA_FILE.write_text(json.dumps(collection, indent=2))


@app.get("/figurines")
def list_figurines() -> List[Dict[str, str]]:
    return jsonify([fig.__dict__ for fig in FIGURINES])


@app.get("/collection")
def get_collection() -> List[Dict[str, str]]:
    return jsonify(load_collection())


@app.post("/collection")
def add_to_collection():
    if request.is_json:
        data = request.get_json() or {}
        name = data.get("name")
        faction = data.get("faction")
    else:
        name = request.form.get("name")
        faction = request.form.get("faction")
    if not name or not faction:
        return {"error": "name and faction required"}, 400
    collection = load_collection()
    collection.append({"name": name, "faction": faction})
    save_collection(collection)
    if request.is_json:
        return {"status": "added"}, 201
    return index()


FORM_HTML = """
<!doctype html>
<title>Figurine Collection</title>
<h1>Ajouter une figurine</h1>
<form method="post" action="/collection">
  Nom: <input type="text" name="name"><br>
  Faction: <input type="text" name="faction"><br>
  <input type="submit" value="Ajouter">
</form>
<ul>
{% for fig in collection %}
<li>{{ fig.faction }} - {{ fig.name }}</li>
{% endfor %}
</ul>
"""


@app.get("/")
def index():
    return render_template_string(FORM_HTML, collection=load_collection())


if __name__ == "__main__":
    app.run(debug=True)
