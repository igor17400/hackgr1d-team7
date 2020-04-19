from app import db
from app.models import User, ChatStage  

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
    print(users)


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

# add_user()
# change_user_name()
delete_user()
# display_users()

# add_chat()
# change_chat_name()
delete_chats()
# display_chats()

