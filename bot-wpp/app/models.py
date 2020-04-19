from datetime import datetime
from app import db

##db.session.rollback()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    cpf = db.Column(db.String(120), index=True, unique=True)
    chatstages = db.relationship('ChatStage', backref='author', lazy='dynamic')
    imoveis = db.relationship('Imovel', backref='proprietario', lazy='dynamic')
    seguro_familia = db.relationship('SeguroFamilia', backref='user_infos', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class ChatStage(db.Model):
    __tablename__ = 'chat_stage'
    id = db.Column(db.Integer, primary_key=True)
    estagio_usuario = db.Column(db.String(120), index=True)
    fluxo_de_dialogo = db.Column(db.String(120), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<ChatStage {}>'.format(self.estagio_usuario)


class Imovel(db.Model):
    __tablename__ = 'imovel'
    id = db.Column(db.Integer, primary_key=True)
    renda = db.Column(db.String(120), index=True)
    cep = db.Column(db.String(120), index=True)
    tipo_imovel = db.Column(db.String(120), index=True)
    num_casa = db.Column(db.String(120), index=True)
    valor = db.Column(db.String(120), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Imovel {}>'.format(self.tipo_imovel)


class SeguroFamilia(db.Model):
    __tablename__ = 'seguro_familia'
    id = db.Column(db.Integer, primary_key=True)
    data_nascimento = db.Column(db.String(120), index=True)
    sexo = db.Column(db.String(120), index=True)
    cep = db.Column(db.String(180), index=True)
    problema_de_saude = db.Column(db.String(180), index=True)
    doencas = db.Column(db.String(180), index=True)
    deficiencia = db.Column(db.String(180), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<SeguroFamilia {}>'.format(self.problema_de_saude)

