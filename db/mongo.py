from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env

def CreateConnection():
    # Configuração do cliente MongoDB
    client = MongoClient(os.getenv('MONGO_URI'))
    # client = MongoClient('mongodb+srv://ronaldo:saXsrKL23dtQ3b8V@botporteiro.betnrod.mongodb.net/?retryWrites=true&w=majority&appName=BotPorteiro')
    db = client['hubla_dados']
    collection = db['assinaturas']
    
    return collection