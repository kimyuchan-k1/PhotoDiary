from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


#db 모델 생성 user 정보 모델
class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(80), unique= True, nullable=False)
    password = db.Column(db.string(120),nullable=False)



