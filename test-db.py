from app import db
from app.models import User, ChatStage, Imovel

### USERS
def add_user():
    u = User(username='temp_name', email='temp_email', cpf='temp_cpf')
    db.session.add(u)
    db.session.commit()

def change_user_name():
    user = User.query.filter_by(username='temp_name').first() 
    user.username = 'igor'
    db.session.commit() 

def delete_user():
    users = User.query.all()
    for u in users:
        db.session.delete(u)
    db.session.commit()

def display_users():
    users = User.query.all()
    for u in users:
        print(u.id, u.username, u.email, u.cpf)


### CHATS
def add_chat():
    u = User.query.get(1)
    cs = ChatStage(estagio_usuario='name_stage', author=u)
    db.session.add(cs)
    db.session.commit()

def change_chat_name():
    cs = ChatStage.query.filter_by(estagio_usuario='name_stage').first() 
    cs.estagio_usuario = 'email_stage'
    db.session.commit() 

def delete_chats():
    chats = ChatStage.query.all()
    for c in chats:
        db.session.delete(c)
    db.session.commit()

def display_chats():
    chats = ChatStage.query.all()
    for c in chats:
        print(c.id, c.author.username, c.estagio_usuario)



### IMOVEIS
def add_imovel():
    u = User.query.get(1)
    im = Imovel(cep='temp_cep', tipo_imovel='temp_tipo', num_casa='temp_num', valor='temp_valor', proprietario=u)
    db.session.add(im)
    db.session.commit()

def change_imovel_cep():
    im = Imovel.query.filter_by(cep='temp_cep').first() 
    im.cep = '71680365'
    db.session.commit() 

def change_imovel_tipo():
    im = Imovel.query.filter_by(tipo_imovel='temp_tipo').first() 
    im.tipo_imovel = 'casa'
    db.session.commit() 

def change_imovel_num():
    im = Imovel.query.filter_by(num_casa='temp_num').first() 
    im.num_casa = '44'
    db.session.commit() 

def change_imovel_valor():
    im = Imovel.query.filter_by(valor='temp_valor').first() 
    im.valor = '1000000'
    db.session.commit() 

def delete_imovel():
    imoveis = Imovel.query.all()
    for i in imoveis:
        db.session.delete(i)
    db.session.commit()

def display_imoveis():
    imoveis = Imovel.query.all()
    for i in imoveis:
        print(i.id, i.cep, i.tipo_imovel, i.num_casa, i.valor, i.proprietario.username)


# change_user_name()

# change_chat_name()


# change_imovel_cep()
# change_imovel_tipo()
# change_imovel_num()
# change_imovel_valor()

### REMOVE
# delete_user()
# delete_chats()
# delete_imovel()

### ADD
# add_user()
# add_chat()
# add_imovel()


### DISPLAY
display_users()
display_chats()
display_imoveis()

