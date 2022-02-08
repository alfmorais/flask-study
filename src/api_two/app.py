from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

items = []

class Items(Resource):
    def get(self, name: str):

        for item in items:
            item_name = item["name"]
            if item_name == name:
                return item
        return {"message": f"The item {name} was not found!"}, 404

    def post(self, name):
        item = {"name": name, "price": 12.00}
        items.append(item)
        return item, 201

    def put(self, name):
        pass

    def delete(self, name):
        pass


api.add_resource(Items, "/items/<string:name>")

app.run(port=5000)
