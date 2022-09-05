from flask import ( Blueprint, render_template )
# import json to display database data
import json

# open the pets.json file by passing it as an arguement
# also passes the open() function to make the pets.json file readable
pets = json.load(open('pets.json'))
# print(pets)

bp = Blueprint('pet',  __name__, url_prefix="/pets")

# default route is GET unless specified
@bp.route('/')
def index(): 
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:id>')
def show(id): 
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)