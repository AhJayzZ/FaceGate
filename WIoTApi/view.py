from model import Item, db
from schema import ItemSchema
from flask import Flask, jsonify, request

def get(id=None):
    """
    get Shipment
    """
    try:
        if id is None:
            shipment = Item.query.filter().all()
            shipment_schema =  ItemSchema(many=True)
            return shipment_schema.jsonify(shipment)
        else:
            shipment = Item.query.filter_by(id=id).first()
            shipment_schema = ItemSchema()
            return shipment_schema.jsonify(shipment)
    except Exception as e:
        jsonify({"error":"There was an error please contact the administrator"})
        

def post():
    
    """
    Add shipment
    """
    data = request.get_json()
    try:
        new_shipment = Item(**data)
        shipment_schema = ItemSchema()
        db.session.add(new_shipment)
        db.session.commit()
        return shipment_schema.jsonify(new_shipment)
    except Exception as e:
        print(e)
        jsonify({"error":"There was an error please contact the administrator"})        


def read_name_list(name):
    """
    get Shipment
    """
    try:
        shipment = Item.query.filter_by(name=name, state='in').first()
        shipment_schema = ItemSchema()
        return shipment_schema.jsonify(shipment)
    except Exception as e:
        jsonify({"error":"There was an error please contact the administrator"})

def put(name):
    """
    Update shipment
    """
    try:
            
        data = request.get_json()
        shipment = Item.query.filter_by(name=name, state='in').first()
        shipment = Item.query.filter_by(name=name)
        shipment.update(data)
        db.session.commit()
                
        return jsonify(data)
    except Exception as e:
        jsonify({"error":"There was an error please contact the administrator"})# Routess