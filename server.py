import uuid
import datetime
from flask import Flask, jsonify

app = Flask(__name__)

data = []


@app.route('/', methods=['GET'])
def register():
    data.insert(0, {str(datetime.datetime.now()): uuid.uuid4()})
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)
