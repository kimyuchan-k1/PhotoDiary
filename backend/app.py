from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager



app = Flask(__name__)
app.config['SQLALCA']
@app.route('/')
def hello_world() :
    return 'Hello, World!'

if __name__ == '__main__' :
    app.run(debug=True)
    