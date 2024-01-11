import json
from flask import Flask
from faker import Faker
from faker_vehicle import VehicleProvider
import Park
from datetime import datetime

fake = Faker()
fake.add_provider(VehicleProvider)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Real Time Car Park Analysis</p>"

PARK_1 = fake.uuid4()
PARK_2 = fake.uuid4()
PARK_3 = fake.uuid4()
PARK_4 = fake.uuid4()
PARK_5 = fake.uuid4()

@app.route("/park-1")
def createCar():
    carobj = json.dumps(fake.vehicle_object())
    carobj = json.loads(carobj)

    car = Park.CarPark(
        City= fake.city(),
        Plate= fake.license_plate(),
        Name=fake.name(),
        Make= carobj['Make'],
        Model= carobj['Model'],
        Category= carobj['Category'],
        Year = carobj['Year'],
        ID=PARK_1,
        TS=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    )

    return json.dumps(car.__dict__)


@app.route("/park-2")
def createCar2():
    carobj = json.dumps(fake.vehicle_object())
    carobj = json.loads(carobj)

    car = Park.CarPark(
        City= fake.city(),
        Plate= fake.license_plate(),
        Name=fake.name(),
        Make= carobj['Make'],
        Model= carobj['Model'],
        Category= carobj['Category'],
        Year = carobj['Year'],
        ID=PARK_1,
        TS=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    )

    return json.dumps(car.__dict__)


@app.route("/park-3")
def createCar3():
    carobj = json.dumps(fake.vehicle_object())
    carobj = json.loads(carobj)

    car = Park.CarPark(
        City= fake.city(),
        Plate= fake.license_plate(),
        Name=fake.name(),
        Make= carobj['Make'],
        Model= carobj['Model'],
        Category= carobj['Category'],
        Year = carobj['Year'],
        ID=PARK_1,
        TS=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    )

    return json.dumps(car.__dict__)


@app.route("/park-4")
def createCar4():
    carobj = json.dumps(fake.vehicle_object())
    carobj = json.loads(carobj)

    car = Park.CarPark(
        City= fake.city(),
        Plate= fake.license_plate(),
        Name=fake.name(),
        Make= carobj['Make'],
        Model= carobj['Model'],
        Category= carobj['Category'],
        Year = carobj['Year'],
        ID=PARK_1,
        TS=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    )

    return json.dumps(car.__dict__)


@app.route("/park-5")
def createCar5():
    carobj = json.dumps(fake.vehicle_object())
    carobj = json.loads(carobj)

    car = Park.CarPark(
        City= fake.city(),
        Plate= fake.license_plate(),
        Name=fake.name(),
        Make= carobj['Make'],
        Model= carobj['Model'],
        Category= carobj['Category'],
        Year = carobj['Year'],
        ID=PARK_1,
        TS=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    )

    return json.dumps(car.__dict__)


if __name__ == '__main__':
    app.run(host='192.168.1.42', port=5000)
