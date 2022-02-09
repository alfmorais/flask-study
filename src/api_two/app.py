from flask import Flask, request
from flask_jwt import JWT, jwt_required
from flask_restful import Api, Resource

from security import authenticate, identity


app = Flask(__name__)
app.secret_key = "alfredo"
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []


class Items(Resource):
    @jwt_required()
    def get(self, name: str):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"message": item}, 200 if item else 404

    def post(self, name):
        condition = next(filter(lambda x: x["name"] == name, items), None)

        if condition is not None:
            return {"message": f"An item with name {name} already exists."}, 400

        data = request.get_json()
        price = data.get("price", False)
        item = {"name": name, "price": price}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Items, "/items/<string:name>")
api.add_resource(ItemList, "/items")

app.run(port=5000, debug=True)
