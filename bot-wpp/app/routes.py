from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import random
from app import app
from app.models import User, ChatStage
from app import db

@app.route('/bot', methods=['POST'])
def bot():

    ## Name stage
    user = User.query.filter_by(username='temp_name').first() 
    chatstage = ChatStage.query.filter_by(estagio_usuario='name_stage').first() 
    if(user == None and chatstage == None):
        ## Email stage
        user = User.query.filter_by(email='temp_email').first() 
        chatstage = ChatStage.query.filter_by(estagio_usuario='email_stage').first() 
    if(user == None and chatstage == None):
        ## CPF stage
        user = User.query.filter_by(cpf='temp_cpf').first() 
        chatstage = ChatStage.query.filter_by(estagio_usuario='cpf_stage').first() 

    list_ideia = ['ideia', 'serve', 'objetivo']
    list_conversa_fiada = ['nome', 'você', 'tu']
    list_introducao = ['ola', 'oi', 'ei', 'eeei', 'hello', 'hi']
    list_auto = ['Auto']
    list_residencial = ['Residencial', 'residencial']
    list_vida = ['Vida']
    list_viagem = ['Viagem']
    list_alternativas_erros = [
                            'Vish, não sei responder isso.', 
                            'Pergunta de novo mais tarde. Agora não consigo lhe ajudar',
                            'Desculpa, ainda não fui treinado para isso.'
                        ]

    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if(chatstage != None and user != None):
        if(chatstage.estagio_usuario == 'name_stage'):
            # Atualizar nome
            user.username = incoming_msg
            db.session.commit() 
            # Atualizar estagio
            chatstage.estagio_usuario = 'email_stage'
            db.session.commit() 
            msg.body('Certo, agora me informa o email você usa mais, por favor')
            responded = True
        elif(chatstage.estagio_usuario == 'email_stage'):
            # Atualizar email
            user.email = incoming_msg
            db.session.commit()
            # Atualizar estagio 
            chatstage.estagio_usuario = 'cpf_stage'
            db.session.commit() 
            msg.body('Ótimo! Agora o seu CPF.')
            responded = True
        elif(chatstage.estagio_usuario == 'cpf_stage'):
            # Atualizar CPF
            user.cpf = incoming_msg
            db.session.commit()
            # Atualizar estagio 
            chatstage.estagio_usuario = 'endereco_stage'
            db.session.commit() 
            msg.body('Muito obrigado pelas suas informações!\n\n' + 
                    'Agora vou fazer algumas perguntas relacionadas a sua residência.\n\n' + 
                    'Qual o CEP do imóvel que você deseja proteger? Coloque apenas os números.')
            responded = True
    else:
        if any(word in incoming_msg for word in list_ideia):
            msg.body('O meu objetivo é poder ajudar na qualificação de '+
                        'leads, cross selling, remarketing e renovação de seguro.')
            responded = True
        if any(word in incoming_msg for word in list_conversa_fiada):
            msg.body('Eu me chamo time 7! E estou aqui para lhe ajudar no que você precisar.')
            responded = True
        if any(word in incoming_msg for word in list_introducao):
            msg.body('Ola! Meu nome é SeguroBot, seu assistente pessoal de seguros no WhatsApp.\n'+
                    'Digite uma das opções abaixo para que eu poça lhe ajudar:\n' +
                    '- Seguro Auto\n' +
                    '- Seguro Residencial\n' +
                    '- Seguro Vida\n' + 
                    '- Seguro Viagem\n')
            responded = True

        ## Condições para opções de seguros
        if incoming_msg in list_auto:
            msg.body(random.choice(list_alternativas_erros))
            responded = True
        if incoming_msg in list_residencial:
            msg.body('É preciso estar preparado contra imprevistos! O seguro residencial pode ' + 
                    'cobrir roubos, incêndios, danos elétricos, vendavais e entre outros.\n\n' + 
                    'Agora preciso te conhecer um pouco melhor para que nossos corretores ' + 
                    'encontrem o melhor produto para você.\n\n' + 
                    'Qual seu nome completo?')

            ## add user
            u = User(username='temp_name', email='temp_email', cpf='temp_cpf')
            db.session.add(u) 
            db.session.commit() 

            ## add chat
            u = User.query.get(1)
            cs = ChatStage(estagio_usuario='name_stage', author=u)
            db.session.add(cs) 
            db.session.commit() 

            responded = True
        if incoming_msg in list_vida:
            msg.body(random.choice(list_alternativas_erros))
            responded = True
        if incoming_msg in list_viagem:
            msg.body(random.choice(list_alternativas_erros))
            responded = True

        if not responded:
            msg.body(random.choice(list_alternativas_erros))

    return str(resp)


if __name__ == '__main__':
    app.run()
