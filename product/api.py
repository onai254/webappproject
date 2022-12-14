from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self, id):
        # return product with specified id
        return {"product": "Product with id {}".format(id)}

api.add_resource(Product, "product/<int:id>")

if __name__ == "__main":
    app.run(host='0.0.0.0', port=80, debug=True)