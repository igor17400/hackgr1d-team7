from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bot', methods=['POST'])
def bot():

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
                'cobrir roubos, incêndios, danos elétricos, vendavais e entre outros.')
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