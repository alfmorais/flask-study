from flask import Flask, jsonify, request
from itsdangerous import json

app = Flask(__name__)


stores = [
    {
        "name": "My Wonderfull Store",
        "items": [
            {
                "name": "My Item",
                "price": 19.99,
            }
        ]
    }
]


@app.route("/")  # example: https://google.com.br/
def home():
    return "Hello, world!"

# POST - used to receive data
# GET - used to send data back only


# POST /store data: {name: }
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": [],
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string: name>
@app.route("/store/<string:name>")  # http://127.0.0.1.5000/store/some_name
def get_store(name):
    # Iterate over stores
    # If the store name matches, return it
    # If none match, return an error message
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    message = "store not found"
    return jsonify({"message": message})


# GET /store
@app.route("/store")  # http://127.0.0.1.5000/store/some_name
def get_stores():
    return jsonify({"stores": stores})


# POST /store/<string:name>/item {name: , price: }
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"],
            }
            store["items"].append(new_item)
            return jsonify(store)
    message = "store not found"
    return jsonify({"message": message})


# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
    message = "store not found"
    return jsonify({"message": message})


app.run(port=5000)
