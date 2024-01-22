from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@bp.route('/submit', methods=['POST'])
def submit():
    subreddit = request.form.get('subreddit')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    
    print(f"Fetching data for {subreddit} from {start_date} to {end_date}")
    
    return redirect(url_for('main.index'))

def register_routes(app):
    app.register_blueprint(bp)
