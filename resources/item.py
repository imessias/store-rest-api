#import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument("store_id",
        type=str,
        required=True,
        help="Every item needs a store id."
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        return {"message": "Item not found."}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "An item with name '{}' already exists.".format(name)}, 400 
        
        data = Item.parser.parse_args()
        
        item = ItemModel(name, **data)

        try:
            item.save_to_bd()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        #connection = sqlite3.connect("data.db")
        #cursor = connection.cursor()
#
        #query = "DELETE FROM items WHERE name=?"
        #cursor.execute(query, (name,))
#
        #connection.commit()
        #connection.close()

        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {"message": "Item deleted."}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        #updated_item = ItemModel(name, data["price"])

        if item is None:
            #try:
            #    updated_item.insert()
            #except:
            #    return {"message": "An error occurred inserting item."}, 500
            item = ItemModel(name, **data)
        else: 
            #try:
            #    updated_item.update()
            #except:
            #    return {"message": "An error occurred updating item."}, 500
            item.price = data["price"]
            item.store_id = data["store_id"]

        item.save_to_bd()

        return item.json()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        #connection = sqlite3.connect("data.db")
        #cursor = connection.cursor()
#
        #query = "SELECT * FROM items"
        #result = cursor.execute(query)
#
        #items = []
        #for row in result:
        #    items.append({"name": row[0], "price": row[1]})
#
        #connection.commit()
        #connection.close()

        return {"items": [item.json() for item in ItemModel.query.all()]}