import json
from flask import Flask
from faker import Faker
from faker_vehicle import VehicleProvider
from datetime import datetime,timedelta
import os
import random
import Park

fake = Faker()
fake.add_provider(VehicleProvider)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Real Time Car Park Analysis</p>"

def serialize_datetime(obj): 
    if isinstance(obj, datetime): 
        return obj.isoformat() 
    raise TypeError("Type not serializable") 

PARK_1 = fake.uuid4()
PARK_2 = fake.uuid4()
PARK_3 = fake.uuid4()
PARK_4 = fake.uuid4()
PARK_5 = fake.uuid4()

@app.route("/park-1")
def createCar():
    carobj = json.dumps(fake.vehicle_object())
    carobj = json.loads(carobj)
    
    days  = random.randint(1, 60)
    hours = random.randint(9, 20)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 60)

    ts = datetime.now() - timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    

    car = Park.CarPark(
        City= fake.city(),
        Plate= fake.license_plate(),
        Name=fake.name(),
        Make= carobj['Make'],
        Model= carobj['Model'],
        Category= carobj['Category'],
        Year = carobj['Year'],
        ID=PARK_1,
        TS=ts
    )

    return json.dumps(car.__dict__, indent=4, sort_keys=True, default=serialize_datetime)


@app.route("/park-2")
def createCar2():
    carobj = json.dumps(fake.vehicle_object())
    carobj = json.loads(carobj)

    days  = random.randint(1, 60)
    hours = random.randint(9, 20)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 60)

    ts = datetime.now() - timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    

    car = Park.CarPark(
        City= fake.city(),
        Plate= fake.license_plate(),
        Name=fake.name(),
        Make= carobj['Make'],
        Model= carobj['Model'],
        Category= carobj['Category'],
        Year = carobj['Year'],
        ID=PARK_2,
        TS=ts
    )

    return json.dumps(car.__dict__, indent=4, sort_keys=True, default=serialize_datetime)


@app.route("/park-3")
def createCar3():
    carobj = json.dumps(fake.vehicle_object())
    carobj = json.loads(carobj)
    hours = random.randint(9, 20)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 60)

    days  = random.randint(1, 60)
    ts = datetime.now() - timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    

    car = Park.CarPark(
        City= fake.city(),
        Plate= fake.license_plate(),
        Name=fake.name(),
        Make= carobj['Make'],
        Model= carobj['Model'],
        Category= carobj['Category'],
        Year = carobj['Year'],
        ID=PARK_3,
        TS=ts
    )

    return json.dumps(car.__dict__, indent=4, sort_keys=True, default=serialize_datetime)


@app.route("/park-4")
def createCar4():
    carobj = json.dumps(fake.vehicle_object())
    carobj = json.loads(carobj)
    
    days  = random.randint(0, 60)
    hours = random.randint(1, 20)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 60)

    days  = random.randint(1, 60)
    ts = datetime.now() - timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    

    car = Park.CarPark(
        City= fake.city(),
        Plate= fake.license_plate(),
        Name=fake.name(),
        Make= carobj['Make'],
        Model= carobj['Model'],
        Category= carobj['Category'],
        Year = carobj['Year'],
        ID=PARK_4,
        TS=ts
    )

    return json.dumps(car.__dict__, indent=4, sort_keys=True, default=serialize_datetime)


@app.route("/park-5")
def createCar5():
    carobj = json.dumps(fake.vehicle_object())
    carobj = json.loads(carobj)
    
    days  = random.randint(0, 60)
    hours = random.randint(9, 20)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 60)

    ts = datetime.now() - timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    

    car = Park.CarPark(
        City= fake.city(),
        Plate= fake.license_plate(),
        Name=fake.name(),
        Make= carobj['Make'],
        Model= carobj['Model'],
        Category= carobj['Category'],
        Year = carobj['Year'],
        ID=PARK_5,
        TS=ts
    )

    return json.dumps(car.__dict__, indent=4, sort_keys=True, default=serialize_datetime)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True) 
