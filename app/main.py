from flask import (
    jsonify,
    Flask,
    request,
    Response,
)

from merger import merge_pdf

app = Flask(__name__)

@app.route("/merge")
def merge():
	pass
