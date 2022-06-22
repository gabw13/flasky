from app import db

# class Car(db.Model):
#     # i want car to be a subclass of db.Model
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     # this is saying, i want this to be primary key
#     driver = db.Column(db.String)
#     team = db.Column(db.String)
#     mass_kg = db.Column(db.Integer)


# class Car:
#     def __init__(self, id, driver, team, mass_kg):
#         self.id = id
#         self.driver = driver
#         self.team = team
#         self.mass_kg = mass_kg


# cars =[

#     Car(7, "Sainz", "Ferrari", 795),
#     Car(88, "SHARLES", "Ferrari", 800),
#     Car(94, "Danny Ric", "McLaren", 1138)
# ]

# print(cars)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))
    mass_kg = db.Column(db.Integer)
    #driver = db.relationship("Driver", backref="cars")

    def to_dict(self):
        return {
                "id": self.id,
                "driver": self.driver.name,
                "team": self.driver.team,
                "mass_kg": self.mass_kg
            }
    def to_dict_basic(self):
        return {
                "id": self.id,
                "mass_kg": self.mass_kg
            }