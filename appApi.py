from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

app = Flask(__name__, static_folder='frontend', template_folder='frontend')
# CORS(app)               # Enable CORS for all routes


# # Database setup
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'  # using sqllite simplicity
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# db = SQLAlchemy(app)
# migrate = Migrate(app,db)


# @app.route('/api/login', methods=['POST'])

# Serve the veu (frontend)
@app.route('/')
def index():
    return send_from_directory(app.template_folder, 'index.html')

# Serve other static files (CSS, JS, ...)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)


# API route
@app.route('/api/login', methods = ['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Here, you would typically verify the username and password
    # For demonstration, we'll jsut echo back the data
    
    return jsonify({
        'username' : username,
        'password' : password   # Avoid sending passwords in real work
    })
    
if __name__ == '__main__' :
    app.run(debug=True)