from crypt import methods
import json
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random_cafe():

    if request.method == "GET":
        cafes = db.session.query(Cafe).all()
        random_cafe = random.choice(cafes)

        cafe = {
            "id": random_cafe.id,
            "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "has_sockets": random_cafe.has_sockets,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "can_take_calls": random_cafe.can_take_calls,
            "seats": random_cafe.seats,
            "coffee_price": random_cafe.coffee_price,
        }

        return jsonify(cafe)

@app.route("/all", methods=["GET"])
def all_cafes():
    cafes = db.session.query(Cafe).all()

    all_cafes = []

    for cafe in cafes:
        cafe_item = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "has_sockets": cafe.has_sockets,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "can_take_calls": cafe.can_take_calls,
            "seats": cafe.seats,
            "coffee_price": cafe.coffee_price,
        }
        all_cafes.append(cafe_item)
    
    # return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    return jsonify(all_cafes)

@app.route("/search", methods=["GET"])
def search_cafe():
    location = request.args.get("loc")
    try:
        cafe = db.session.query(Cafe).filter_by(location=location).first()
        data = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "has_sockets": cafe.has_sockets,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "can_take_calls": cafe.can_take_calls,
            "seats": cafe.seats,
            "coffee_price": cafe.coffee_price,
        }
    except:
        print("deu ruim")
        data = {
            "error": {
                "Not Found": "Sorry, we don't have a coffee at that location"
                }
        }
    return jsonify(data)

def str_to_bool(v):
    if v in ['True', ' true', 'T', 't', 'Yes', 'yes', 'y', '1']:
        return True
    else:
        return False

## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_new_cafe():

    data = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=str_to_bool(request.form.get("has_sockets")),
        has_toilet=str_to_bool(request.form.get("has_toilet")),
        has_wifi=str_to_bool(request.form.get("has_wifi")),
        can_take_calls=str_to_bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price")
        )

    db.session.add(data)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_cafe(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()

    if cafe:
        cafe.coffee_price = new_price

        db.session.commit()

        return jsonify(response={"success": "Successfully updated the price."})

    return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})

## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")

    if api_key == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()

        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted cafe."})
            
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})

    return jsonify({"error:": "Sorry, that's not allowed. Make sure you have the correct api_key."})
if __name__ == '__main__':
    app.run(debug=True)
