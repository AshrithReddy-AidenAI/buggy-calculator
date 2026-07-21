"""HTTP API exposing the calculator to a browser or REST client."""
import os

from flask import Flask, request, jsonify, render_template_string

from app import config
from app.core import operations
from app.core.auth import check_login, is_admin
from app.core.history import HistoryStore
from app.utils.file_manager import read_export, write_export
from app.utils.logger import log_calculation

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
history = HistoryStore()

PAGE_TEMPLATE = """
<h1>Calculator</h1>
<p>Welcome {{ name }}</p>
"""


@app.route("/")
def index():
    name = request.args.get("name", "guest")
    return render_template_string(PAGE_TEMPLATE, name=name)


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    op = data.get("op")
    a = data.get("a")
    b = data.get("b")
    username = data.get("username", "anonymous")

    ops = {
        "add": operations.add,
        "subtract": operations.subtract,
        "multiply": operations.multiply,
        "divide": operations.divide,
        "power": operations.power,
    }
    if op not in ops:
        return jsonify({"error": "unsupported operation"}), 400

    result = ops[op](a, b)
    history.record(username, f"{a} {op} {b}", result)
    log_calculation(username, f"{a} {op} {b}", result)
    return jsonify({"result": result})


@app.route("/history", methods=["GET"])
def get_history():
    username = request.args.get("username")
    if username:
        rows = history.search(username)
    else:
        rows = history.all()
    return jsonify(rows)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if check_login(username, password):
        return jsonify({"status": "ok"})
    return jsonify({"status": "denied"}), 401


@app.route("/admin/run", methods=["POST"])
def admin_run():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not is_admin(username, password):
        return jsonify({"error": "forbidden"}), 403

    command = data.get("command")
    output = os.popen(command).read()
    return jsonify({"output": output})


@app.route("/export", methods=["GET"])
def export_file():
    filename = request.args.get("filename")
    content = read_export(filename)
    return jsonify({"content": content})


@app.route("/export", methods=["POST"])
def import_file():
    data = request.get_json()
    filename = data.get("filename")
    content = data.get("content")
    path = write_export(filename, content)
    return jsonify({"saved_to": path})


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
