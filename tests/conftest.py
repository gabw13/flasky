# pytest will construct data cleanly at beginning and removed at end of test
# lets you write tests in a much simpler way
import pytest
from app import create_app
from app import db
from flask.signals import request_finished

@pytest.fixture
def app():
    app = create_app({"TESTING": True}) # passing in a dict

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove() 
    
    with app.app_context():
        db.create_all()
        yield app
        # will create our db and allow us to 
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

# @pytest.fixture
# def seven_cats(app):
#     jazz = Cat(id=1, name='Jazz', color='black', age=8)
#     cosmo = Cat(id=1, name='Cosmo', color='tuxedo', age=8)
#     lily = Cat(id=1, name='Lily', color='brown and black', age=6)
#     ellis = Cat(id=1, name='Ellis', color='orange', age=2)
#     monster = Cat(id=1, name='Monster', color='grey', age=14)
#     simba = Cat(id=1, name='Simba', color='orange', age=8)
#     jenkins = Cat(id=1, name='Jenkins', color='tuxedo', age=4)

#     db.session.add(jazz)
#     db.session.add(cosmo)
#     db.session.add(lily)
#     db.session.add(ellis)
#     db.session.add(monster)
#     db.session.add(simba)
#     db.session.add(jenkins)

#     db.session.commit()

# or can write db.session_all([])

@pytest.fixture
def three_cars(app):
    ferrari = Car(id=1, driver="Tanya", team="Ferrari", mass_kg=700)
    tesla = Car(id=2, driver="Jura", team="Tesla", mass_kg=790)
    mcLaren = Car(id=3, driver="Alice", team="McLauren", mass_kg=900)

    db.session.add(ferrari)
    db.session.add(tesla)
    db.session.add(mcLaren)

    db.session.commit()