import json
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from db.mongo import CreateConnection
import requests
import random
import string

def verificar_email(email):
    collection = CreateConnection()
    user = collection.find({"event.user.email": email})
    if user:
        if (user[0]['event']['subscription']['status'] == "active"):
            create_user = criar_usuario(user[0]['event']['user']['email'], user[0]['event']['user']['firstName'])
            # print(create_user)
            return ('Assinatura ativa', create_user)
        else:
            return ('Assinatura inativa', None)
    else:
        return ('E-mail não encontrado.', None)
    
def criar_usuario(email, nome):
    tamanho = 12  # Defina o tamanho da senha desejada
    # Combine caracteres minúsculos, maiúsculos, dígitos e símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Gere a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    user_name = email.split('@')[0]
    user ={
        'email': f'{email}',
        'username': f'{user_name}',
        'displayName': f'{nome}',
        'password': 'Pa$$w0rd'
    }
    
    headers = {
        'User-Agent': 'PostmanRuntime/7.39.0',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }
    
    response_create_user = requests.post('http://localhost:5000/api/account/register', headers=headers, json=user)
    if response_create_user.status_code == 200:
        print ('Usuário criado com sucesso.')
        return user