#!flask/bin/python
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
import requests
import json
import random
import string
from datetime import date


app = Flask(__name__)

today = date.today().strftime("%Y-%m-%d")


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


headers = {
    'accept': 'application/json',
    'X-Api-Key': '1e0d86b2-d0b2-4ddb-96b4-cdc907f7e5a8',
    'Content-Type': 'application/json',
}


@app.route('/s', methods=['POST'])
def simulation():
    params = (
        ('cnpj', '11321351000110'),
        ('codigoModeloProposta', 'YZ'),
    )

    #nome, endereco, dataNascimento, renda
    content = request.json

    data = {'simulacoes': [{'proponente': {'tipoRelacaoSeguradoId': 1, 'nome': content['nome'], 'cpf': content['cpf'], 'dataNascimento': content['dataNascimento'],
                                           'profissaoCbo': '2410-05', 'renda': content['renda'], 'sexoId': 1, 'uf': 'MG', 'declaracaoIRId': 1}, 'periodicidadeCobrancaId': 30, 'prazoCerto': 30}]}

    response = requests.post(
        'https://gateway.gr1d.io/sandbox/mongeralaegon/v1/simulacao', headers=headers, params=params, data=json.dumps(data))
    return response.json()


@app.route('/p', methods=['POST'])
def proposal():

    url = f'https://gateway.gr1d.io/sandbox/mongeralaegon/v1/proposta/{randomString(12)}'

    params = (
        ('empresa', '11321351000110'),
    )

    content = request.json

    dataf = {'PROPOSTA': {'NUMERO': '0', 'DT_PROTOCOLO': today, 'DT_ASSINATURA': today, 'DT_INDEXACAO': today, 'DADOS_PROPONENTE': {'MATRICULA': '0', 'NOME': 'CENARIO DE TESTE 001', 'DT_NASCIMENTO': '1994-10-27', 'IDADE': '24', 'SEXO': 'MASCULINO', 'ESTADO_CIVIL': 'SOLTEIRO', 'CPF': '24011549061', 'TITULAR_CPF': 'true', 'EMAIL': 'TESTEPROPOSTA@GMAIL.COM', 'RESIDE_BRASIL': 'true', 'RENDA_MENSAL': '5000.00', 'NUM_FILHOS': '0', 'PPE': 'false', 'DOCUMENTOS': {'DOCUMENTO': {'NATUREZA_DOC': 'RG', 'DOCUMENTO': '36969739-X', 'ORGAO_EXPEDIDOR': 'SSP', 'DATA_EXPEDICAO': '2012-07-26'}}, 'ENDERECOS': {'TP_CORRESPONDENCIA': 'RESIDENCIAL', 'ENDERECO': [{'TIPO': 'RESIDENCIAL', 'LOGRADOURO': 'TRAVESSA BELAS ARTES', 'NUMERO': '15', 'COMPLEMENTO': 'ANEXO', 'BAIRRO': 'CENTRO', 'CIDADE': 'RIO DE JANEIRO', 'ESTADO': 'RJ', 'CEP': '20060000'}]}, 'TELEFONES': {'TELEFONE': [{'TIPO': 'CELULAR', 'DDI': '55', 'DDD': '21', 'NUMERO': '991122345'}, {'TIPO': 'RESIDENCIAL', 'DDI': '55', 'DDD': '21', 'NUMERO': '37222800'}]}, 'PROFISSAO': {'CODIGO': '2410-05', 'DESCRICAO': 'ADVOGADO', 'CATEGORIA': 'EMPREGADO', 'EMPRESA': {'NOME': 'MONGERAL AEGON'}}}, 'PLANOS': {'VL_TOTAL': '188.79', 'PLANO': [{'CODIGO': '1780', 'NOME': 'DOENÇAS GRAVES', 'VL_AP_INICIAL': '0.00', 'VL_PORTAB': '0.00', 'TP_TRIBUTACAO': 'NENHUM', 'DT_CONCESSAO': '1900-01-01', 'PRAZO_CERTO': '0', 'PRAZO_DECRESCIMO': '0', 'COBERTURAS': {'COBERTURA': {'CODIGO': '34', 'VL_CONTRIB': '53.58', 'VL_COBERTURA': '120000.00'}}}, {'CODIGO': '1548', 'NOME': 'INVALIDEZ TOTAL POR ACIDENTE', 'VL_AP_INICIAL': '0.00', 'VL_PORTAB': '0.00', 'TP_TRIBUTACAO': 'NENHUM', 'DT_CONCESSAO': '1900-01-01', 'PRAZO_CERTO': '0', 'PRAZO_DECRESCIMO': '0', 'COBERTURAS': {'COBERTURA': {'CODIGO': '74', 'VL_CONTRIB': '15.21', 'VL_COBERTURA': '200000.00'}}}, {'CODIGO': '1811', 'NOME': 'VGBL PRIVATE TOP', 'VL_AP_INICIAL': '0.00', 'VL_PORTAB': '0.00', 'TP_TRIBUTACAO': 'REGRESSIVA', 'DT_CONCESSAO': '2045-01-29', 'PRAZO_CERTO': '0', 'FUNDOS': {'FUNDO': [{'CODIGO': '10102', 'NOME': 'MONGERAL AEGON RENDA FIXA PRIVATE TOP PREVIDÊNCIA FUNDO DE INVESTIMENTO', 'PC_CONTRIB': '60.00', 'PC_APORTE': '0.00', 'PC_PORTAB': '0.00'}, {'CODIGO': '10105', 'NOME': 'MONGERAL AEGON MULTIMERCADO PREVIDÊNCIA', 'PC_CONTRIB': '40.00', 'PC_APORTE': '0.00', 'PC_PORTAB': '0.00'}]}, 'COBERTURAS': {
        'COBERTURA': {'CODIGO': '1', 'VL_CONTRIB': '120.00', 'VL_COBERTURA': '0.00'}}}]}, 'BENEFICIARIOS': {'BENEFICIARIO': [{'NOME': 'BENEFICIARIO DE TESTE', 'NASCIMENTO': '1974-07-28', 'PARENTESCO': 'CONJUGE', 'PARTICIPACAO': '100.00', 'CD_PLANO': '1811'}]}, 'DECLARACOES': {'DPS': {'TIPO_DPS': 'TITULAR', 'PESO': '103', 'ALTURA': '1.80', 'PERGUNTAS': {'PERGUNTA': [{'NUMERO': '1', 'QUESTAO': 'Encontra-se com algum problema de saude ou faz uso de algum medicamento atualmente? Em caso afirmativo, informar qual.', 'RESPOSTA': 'false', 'OBS_RESPOSTA': ''}, {'NUMERO': '2', 'QUESTAO': 'Sofre ou ja sofreu de doencas do coracao, insuficiencia cardiaca, hipertensao arterial, problemas circulatorios ou cardiovasculares? Em caso afirmativo, informar quais e se ja foi submetido a alguma cirurgia.', 'RESPOSTA': 'false', 'OBS_RESPOSTA': ''}, {'NUMERO': '3', 'QUESTAO': 'Sofre ou sofreu de deficiencia de orgaos, membros ou sentidos, incluindo doencas ortopedicas relacionadas a esforcos repetitivos (ler e Dort)', 'RESPOSTA': 'false', 'OBS_RESPOSTA': ''}, {'NUMERO': '4', 'QUESTAO': 'Fez alguma cirurgia, biopsia ou esteve internado nos ultimos cinco anos?', 'RESPOSTA': 'false', 'OBS_RESPOSTA': ''}, {'NUMERO': '5', 'QUESTAO': 'Esta afastado(a) do trabalho?', 'RESPOSTA': 'false', 'OBS_RESPOSTA': ''}, {'NUMERO': '6', 'QUESTAO': 'Pratica esportes perigosos, tais como: para-quedismo, motociclismo (competicoes ou exibicoes), boxe, rodeio, alpinismo, automobilismo (competicoes ou exibicoes) e mergulho? Informar quais.', 'RESPOSTA': 'false', 'OBS_RESPOSTA': ''}, {'NUMERO': '7', 'QUESTAO': 'E fumante? Em caso afirmativo, informar a quantidade media de cigarros por dia.', 'RESPOSTA': 'false', 'OBS_RESPOSTA': ''}]}}}, 'DADOS_COBRANCA': {'PERIODICIDADE': 'MENSAL', 'TIPO_COBRANCA': 'BOLETO', 'DIA_VENCIMENTO': '25', 'COMP_DEBITO': '07/2019', 'NUM_CONVENIO': '0'}, 'USO_MONGERAL': {'CONV_ADESAO': 'AD0332', 'ACAO_MARKETING': '0493', 'ALTERNATIVA': '1', 'SUCURSAL': 'F22', 'DIR_REGIONAL': '16057572', 'GER_SUCURSAL': '03002658', 'GER_COMERCIAL': '18040942', 'AGENTE': '0', 'CORRETOR1': '07037818', 'CORRETOR2': '0', 'AGENTE_FIDELIZACAO': '0', 'MODELO_PROPOSTA': 'YZ', 'MODELO_PROPOSTA_GED': 'YZ', 'TIPO_COMISSAO': '1'}}}

    response = requests.post(url, headers=headers,
                             params=params, data=json.dumps(dataf))

    return response.json()


if __name__ == '__main__':
    app.run(debug=True)

