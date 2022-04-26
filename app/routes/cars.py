from flask import Blueprint, jsonify

class Car:
    def __init__(self, id, driver, team, mass_kg):
        self.id = id
        self.driver = driver
        self.team = team
        self.mass_kg = mass_kg


cars =[
    Car(7, "Sainz", "Ferrari", 795),
    Car(88, "SHARLES", "Ferrari", 800),
    Car(94, "Danny Ric", "McLaren", 1138)
]

print(cars)

cars_bp = Blueprint("cars", __name__, url_prefix = "/cars")
# if we do it this way, we would need to start the route with an empty str "" or no url_prefix and "/cars" in the route
# url_prefix defines the way that every single route starts
# empty string is saying ok only use url_prefix
# if url_prefix is here, and you put something else in the string for 

@cars_bp.route("", methods = ["GET"])
# this decorator says this is how the client needs to make a request -> when they make this request, run the get_all_cars function and return response
def get_all_cars():
    response = [] 
    for car in cars:
        response.append(
            {
                "id": car.id,
                "driver": car.driver,
                "team":car.team,
                "mass_kg": car.mass_kg
            }
        )
    return jsonify(response)

