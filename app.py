# config
from flask import Flask
app = Flask(__name__)

# INDEX ROUTE
@app.route('/')
def index():
    return 'Hello, this is PetFax!'

# pets INDEX route
@app.route('/pets')
def pets():
    return 'These are our pets available for adoption!'