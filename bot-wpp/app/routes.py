from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import random
from app import app
from app.models import User, ChatStage, Imovel, SeguroFamilia
from app import db

@app.route('/bot', methods=['POST'])
def bot():

    user = None
    chatstage = None
    imovel = None
    seguroFamilia = None

    ### ---------------------- logica comum de dialogo ----------------------------
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
    ### -----------------------------------------------------------------------------

    ### -------------- logica de dialogo para seguro residencial -------------------
    if(chatstage == None):
        ## CEP stage
        imovel = Imovel.query.filter_by(cep='temp_cep').first() 
        chatstage = ChatStage.query.filter_by(estagio_usuario='cep_stage').first() 
    if(chatstage == None and imovel == None):
        ## Tipo do imovel stage
        imovel = Imovel.query.filter_by(tipo_imovel='temp_tipo').first() 
        chatstage = ChatStage.query.filter_by(estagio_usuario='tipo_stage').first() 
    if(chatstage == None and imovel == None):
        ## Num da casa stage
        imovel = Imovel.query.filter_by(num_casa='temp_num').first() 
        chatstage = ChatStage.query.filter_by(estagio_usuario='num_stage').first() 
    if(chatstage == None and imovel == None):
        ## Num da casa stage
        imovel = Imovel.query.filter_by(valor='temp_valor').first() 
        chatstage = ChatStage.query.filter_by(estagio_usuario='valor_stage').first() 
    if(chatstage == None):
        chatstage = ChatStage.query.filter_by(estagio_usuario='end_stage').first() 
    ### -----------------------------------------------------------------------------

    ### -------------- logica de dialogo para seguro familia -----------------------
    seguroFamilia = SeguroFamilia.query.filter_by(cep='temp_cep').first() 
    if(chatstage == None):
        ## CEP stage
        chatstage = ChatStage.query.filter_by(estagio_usuario='cep_stage_seg_familia').first() 

    if(chatstage == None and seguroFamilia == None):
        ## Data de nascimento stage
        seguroFamilia = SeguroFamilia.query.filter_by(data_nascimento='temp_data_nascimento').first() 
        chatstage = ChatStage.query.filter_by(estagio_usuario='data_nascimento_stage_seg_familia').first() 
    
    if(chatstage == None and seguroFamilia == None):
        ## Sexo stage
        seguroFamilia = SeguroFamilia.query.filter_by(sexo='temp_sexo').first() 
        chatstage = ChatStage.query.filter_by(estagio_usuario='sexo_stage_seg_familia').first() 

    if(chatstage == None and seguroFamilia == None):
        ## Problema de saude stage
        seguroFamilia = SeguroFamilia.query.filter_by(problema_de_saude='temp_problema_de_saude').first() 
        chatstage = ChatStage.query.filter_by(estagio_usuario='problema_de_saude_stage_seg_familia').first() 

    if(chatstage == None and seguroFamilia == None):
        ## Doencas stage
        seguroFamilia = SeguroFamilia.query.filter_by(doencas='temp_doencas').first() 
        chatstage = ChatStage.query.filter_by(estagio_usuario='doencas_stage_seg_familia').first() 

    if(chatstage == None and seguroFamilia == None):
        ## Deficiencia stage
        seguroFamilia = SeguroFamilia.query.filter_by(deficiencia='temp_deficiencia').first() 
        chatstage = ChatStage.query.filter_by(estagio_usuario='deficiencia_stage_seg_familia').first() 
    ### -----------------------------------------------------------------------------

    print('user --> ', user)
    print('chatstage --> ', chatstage)
    print('imovel --> ', imovel)
    print('seguroFamilia --> ', seguroFamilia)
    

    list_ideia = ['ideia', 'serve', 'objetivo']
    list_conversa_fiada = ['nome', 'você', 'tu']
    list_introducao = ['ola', 'oi', 'ei', 'eeei', 'hello', 'hi']
    list_iteracao = ['desejo saber sobre mais um seguro']
    list_auto = ['Auto']
    list_residencial = ['Residencial', 'residencial', 'seguro residencial']
    list_familia = ['familia', 'seguro familia', 'seguro família']
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
            chatstage_fluxo = ChatStage.query.filter_by(fluxo_de_dialogo='seguro_residencial').first() 
            if(chatstage_fluxo != None and chatstage_fluxo.fluxo_de_dialogo == 'seguro_residencial'):
                chatstage.estagio_usuario = 'cep_stage'
            chatstage_fluxo = ChatStage.query.filter_by(fluxo_de_dialogo='seguro_familia').first() 
            if(chatstage_fluxo != None and chatstage_fluxo.fluxo_de_dialogo == 'seguro_familia'):
                chatstage.estagio_usuario = 'cep_stage_seg_familia'
            db.session.commit() 
            msg.body('Muito obrigado pelas suas informações!\n\n' + 
                    'Agora vou fazer algumas perguntas relacionadas a sua residência.\n\n' + 
                    'Qual o CEP do imóvel que você deseja proteger? Coloque apenas os números.')
            responded = True

    elif(chatstage != None and (imovel != None or seguroFamilia != None)):

        if(imovel != None):
            if(chatstage.estagio_usuario == 'cep_stage'):
                # Atualizar cep
                imovel.cep = incoming_msg
                db.session.commit() 
                # Atualizar estagio
                chatstage.estagio_usuario = 'tipo_stage'
                db.session.commit() 
                msg.body('Estamos quase terminando (:\n\n' + 
                        'Me diga qual é o seu tipo de imovel:\n'+
                        '- Casa\n' + 
                        '- Apartamento\n')
                responded = True
            elif(chatstage.estagio_usuario == 'tipo_stage'):
                # Atualizar tipo do imovel
                imovel.tipo_imovel = incoming_msg
                db.session.commit() 
                # Atualizar estagio
                chatstage.estagio_usuario = 'num_stage'
                db.session.commit() 
                msg.body('Qual é o número de sua residência?')
                responded = True
            elif(chatstage.estagio_usuario == 'num_stage'):
                # Atualizar o numero da residencia
                imovel.num_casa = incoming_msg
                db.session.commit() 
                # Atualizar estagio
                chatstage.estagio_usuario = 'valor_stage'
                db.session.commit() 
                msg.body('Qual o valor do imóvel?\n\n'+
                        'Este valor se refere a quanto seria gasto para reconstruir o imóvel'+
                        ' e não seu valor de mercado.')
                responded = True
            elif(chatstage.estagio_usuario == 'valor_stage'):
                # Atualizar o valor da residencia
                imovel.valor = incoming_msg
                db.session.commit() 
                # Atualizar estagio
                chatstage.estagio_usuario = 'end_stage'
                db.session.commit() 
                msg.body('Muito obrigada pelas informações!\n\n'+
                        'Nossos corretores estão buscando os melhores produtos para você, '+
                        'em breve você receberá as opções.')
                responded = True

        elif(seguroFamilia != None):
            if(chatstage.estagio_usuario == 'cep_stage_seg_familia'):
                # Atualizar cep Seguro Familia
                seguroFamilia.cep = incoming_msg
                db.session.commit() 
                # Atualizar estagio
                chatstage.estagio_usuario = 'data_nascimento_stage_seg_familia'
                db.session.commit() 
                msg.body('Excelente! Qual a sua data de nascimento?')
                responded = True
            elif(chatstage.estagio_usuario == 'data_nascimento_stage_seg_familia'):
                # Atualizar data_nascimento Seguro Familia
                seguroFamilia.data_nascimento = incoming_msg
                db.session.commit() 
                # Atualizar estagio
                chatstage.estagio_usuario = 'sexo_stage_seg_familia'
                db.session.commit() 
                msg.body('Qual o seu sexo?')
                responded = True
            elif(chatstage.estagio_usuario == 'sexo_stage_seg_familia'):
                # Atualizar sexo Seguro Familia
                seguroFamilia.sexo = incoming_msg
                db.session.commit() 
                # Atualizar estagio
                chatstage.estagio_usuario = 'problema_de_saude_stage_seg_familia'
                db.session.commit() 
                msg.body('Encontra-se com algum problema de saúde ou faz uso de algum medicamento atualmente?')
                responded = True
            elif(chatstage.estagio_usuario == 'problema_de_saude_stage_seg_familia'):
                # Atualizar doencas Seguro Familia
                seguroFamilia.problema_de_saude = incoming_msg
                db.session.commit() 
                # Atualizar estagio
                chatstage.estagio_usuario = 'doencas_stage_seg_familia'
                db.session.commit() 
                msg.body('Sofre ou ja sofreu de doenças do coração, insuficiencia cardiaca, hipertensao arterial, '+
                'problemas circulatorios ou cardiovasculares? Em caso afirmativo, informar quais e se ja foi submetido '+
                'a alguma cirurgia? ')
                responded = True
            elif(chatstage.estagio_usuario == 'doencas_stage_seg_familia'):
                # Atualizar doencas Seguro Familia
                seguroFamilia.doencas = incoming_msg
                db.session.commit() 
                # Atualizar estagio
                chatstage.estagio_usuario = 'deficiencia_stage_seg_familia'
                db.session.commit() 
                msg.body('Sofre ou sofreu de deficiência de orgãos, membros ou sentidos, incluindo doenças ortopédicas '+
                ' relacionadas a esforços repetitivos? ')
                responded = True
            elif(chatstage.estagio_usuario == 'deficiencia_stage_seg_familia'):
                # Atualizar doencas Seguro Familia
                seguroFamilia.deficiencia = incoming_msg
                db.session.commit() 
                # Atualizar estagio
                chatstage.estagio_usuario = 'end_stage'
                db.session.commit() 
                msg.body('Muito obrigada pelas informações!\n\n'+
                        'Nossos corretores estão buscando os melhores produtos para você, '+
                        'em breve você receberá as opções.')
                responded = True

    elif(chatstage != None and imovel == None and user == None and seguroFamilia == None):
        msg.body('Se quiser começar outra iteração basta dizer!')
        # Atualizar estagio
        chatstage.estagio_usuario = 'the_end'
        db.session.commit() 
        responded = True
        return str(resp)

    else:
        if any(word in incoming_msg for word in list_ideia):
            msg.body('O meu objetivo é poder ajudar na qualificação de '+
                        'leads, cross selling, remarketing e renovação de seguro.')
            responded = True
        if any(word in incoming_msg for word in list_conversa_fiada):
            msg.body('Eu me chamo Segurobot! E estou aqui para lhe ajudar no que você precisar.')
            responded = True
        if any(word in incoming_msg for word in list_introducao) or any(word in incoming_msg for word in list_iteracao):
            msg.body('Ola! Meu nome é SeguroBot, seu assistente pessoal de seguros no WhatsApp.\n'+
                    'Digite uma das opções abaixo para que eu possa lhe ajudar:\n' +
                    '- Seguro Auto\n' +
                    '- Seguro Residencial\n' +
                    '- Seguro Família\n' + 
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
            cs = ChatStage(estagio_usuario='name_stage', fluxo_de_dialogo='seguro_residencial', author=u)
            db.session.add(cs) 
            db.session.commit() 

            ## add imovel
            im = Imovel(cep='temp_cep', tipo_imovel='temp_tipo', num_casa='temp_num', valor='temp_valor', proprietario=u)
            db.session.add(im)
            db.session.commit()

            responded = True
        if incoming_msg in list_familia:
            msg.body('Este seguro tem por objetivo a proteção financeira familiar com o '+
                    'pagamento de uma indenização e/ou prestação de serviços complementares, '+ 
                    'em caso de morte natural ou por acidente do segurado ou seu cônjuge, '+ 
                    'suportando as despesas básicas da família por até 1 ano.\n\n' + 
                    'Me informa alguns de seus dados para que possamos achar o melhor seguro ' + 
                    'para você?\n\n' + 
                    'Me informa o seu nome completo por favor?')

            ## add user
            u = User(username='temp_name', email='temp_email', cpf='temp_cpf')
            db.session.add(u) 
            db.session.commit() 

            ## add chat
            cs = ChatStage(estagio_usuario='name_stage', fluxo_de_dialogo='seguro_familia', author=u)
            db.session.add(cs) 
            db.session.commit() 

            ## add infos SeguroFamilia
            sf= SeguroFamilia(data_nascimento='temp_data_nascimento', sexo='temp_sexo', cep='temp_cep', problema_de_saude='temp_problema_de_saude', doencas='temp_doencas', deficiencia='temp_deficiencia', user_infos=u)
            db.session.add(sf)
            db.session.commit()

            responded = True
        if incoming_msg in list_viagem:
            msg.body(random.choice(list_alternativas_erros))
            responded = True

        if not responded:
            msg.body(random.choice(list_alternativas_erros))

    return str(resp)


if __name__ == '__main__':
    app.run()

