from flask import ( Blueprint, render_template, request, redirect ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

# route that goes to '/' and import the request pacakge from flask
@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        print(request.form)
        # imprt redirect from flask and use redirect method to run if
        # the request.method is NOT POST
        return redirect('/facts')

    return render_template('facts/index.html')

# default route is GET unless specified
@bp.route('/new')
def new(): 
    return render_template('facts/new.html')