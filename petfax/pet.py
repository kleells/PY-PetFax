from flask import ( Blueprint, render_template )
# import json to display database data
import json

# open the pets.json file by passing it as an arguement
# also passes the open() function to make the pets.json file readable
pets = json.load(open('pets.json'))
# print(pets)

bp = Blueprint('pet',  __name__, url_prefix="/pets")

@bp.route('/')
def index():
    # tell the route to render the index.html template to the application
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:id>')
def show(id): 
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)