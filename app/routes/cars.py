from flask import Blueprint, jsonify, request, make_response

from app import db
from app.models.cars import Car

cars_bp = Blueprint("cars", __name__, url_prefix = "/cars")
# if we do it this way, we would need to start the route with an empty str "" or no url_prefix and "/cars" in the route
# url_prefix defines the way that every single route starts
# empty string is saying ok only use url_prefix
# if url_prefix is here, and you put something else in the string for 

@cars_bp.route("", methods=["POST"])
def create_car():
    request_body = request.get_json()

    new_car = Car(
        driver=request_body["driver"],
        team=request_body["team"],
        mass_kg=request_body["mass_kg"]
        )
    
    db.session.add(new_car)
    db.session.commit()

    return{
        "id": new_car.id
    }, 201

@cars_bp.route("", methods = ["GET"])
# this decorator says this is how the client needs to make a request -> when they make this request, run the get_all_cars function and return response
def get_all_cars():
    params = request.args
    if "driver" in params:
        driver_name = params["driver"]
        cars = Car.query.filter_by(driver= driver_name)
    else:
        cars = Car.query.all()
    response = []
    cars = Car.query.all()
    for car in cars:
        response.append(
            {
                "id": car.id,
                "driver": car.driver,
                "team": car.team,
                "mass_kg": car.mass_kg
            }
        )
    return jsonify(response)

@cars_bp.route("/<car_id>", methods = ["GET"])
def get_one_car(car_id):
    try:
        car_id = int(car_id)
    except ValueError:
        return jsonify({"msg": f"Invalid car id:'{car_id}'. ID must be an integer."}), 400
    
    chosen_car = Car.query.get(car_id)
    
    if chosen_car is None:
        return jsonify({"msg": f"Could not find car with id {car_id}"}), 404

    # car_dict =  {
    #     "id": chosen_car.id,
    #     "driver": chosen_car.driver,
    #     "team": chosen_car.team,
    #     "mass_kg": chosen_car.mass_kg
    # }

    return jsonify({
        "id": chosen_car.id,
        "driver": chosen_car.driver,
        "team": chosen_car.team,
        "mass_kg": chosen_car.mass_kg
    }), 200

@cars_bp.route("/<car_id>", methods = ["PUT"])
def replace_one_car(car_id):
    try:
        car_id = int(car_id)
    except ValueError:
        return jsonify({"msg": f"Invalid car id:'{car_id}'. ID must be an integer."}), 400
    
    request_body = request.get_json()

    if "driver" not in request_body or \
        "team" not in request_body or \
        "mass_kg" not in request_body:
        return jsonify({"msg":f"Request must include driver, team, and mass_kg"}), 400

    chosen_car = Car.query.get(car_id)
    
    if chosen_car is None:
        return jsonify({"msg": f"Could not find car with id {car_id}"}), 404
    
    chosen_car.driver = request_body["driver"]
    chosen_car.team = request_body["team"]
    chosen_car.mass_kg = request_body["mass_kg"]
    
    db.session.commit()

    return make_response(
        jsonify({"msg": f"successfully replaced car with id {car_id}"}), 
        200
    )

@cars_bp.route("/<car_id>", methods = ["DELETE"])
def delete_one_car(car_id):
    try:
        car_id = int(car_id)
    except ValueError:
        return jsonify({"msg": f"Invalid car id:'{car_id}'. ID must be an integer."}), 400
    
    chosen_car = Car.query.get(car_id)
    
    if chosen_car is None:
        return jsonify({"msg": f"Could not find car with id {car_id}"}), 404
    
    db.session.delete(chosen_car)
    db.session.commit()

    return jsonify({"msg": f"Deleted car with id {car_id}"})
