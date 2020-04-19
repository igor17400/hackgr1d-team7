from datetime import datetime
from app import db

##db.session.rollback()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    cpf = db.Column(db.String(120), index=True, unique=True)
    chatstages = db.relationship('ChatStage', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class ChatStage(db.Model):
    __tablename__ = 'chat_stage'
    id = db.Column(db.Integer, primary_key=True)
    estagio_usuario = db.Column(db.String(120), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<ChatStage {}>'.format(self.body)