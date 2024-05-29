import telebot
from dotenv import load_dotenv
import os
from verify_email import verificar_email

load_dotenv()  # take environment variables from .env

# Substitua 'SEU_TOKEN_AQUI' pelo token fornecido pelo BotFather
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Crie uma instância do bot
bot = telebot.TeleBot(token=TOKEN, parse_mode='MARKDOWN')

# Trata o comando /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Olá! Por favor, digite o e-mail que foi usado na compra da Hubla:")

# Trata mensagens de texto
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    email = message.text
    verificar_retorno, usuario = verificar_email(email)
    if(verificar_retorno == 'Assinatura ativa'):
        # print(usuario)
        bot.reply_to(message, f'Suas credenciasi de acesso são: \n*Login:* {usuario["email"]} \n*Senha*: {usuario["password"]}')
    elif(verificar_retorno == 'Assinatura inativa'):
        # Aqui você pode validar o e-mail ou realizar outras ações com ele
        bot.reply_to(message, f"Assinatura inativa.")
    else:
        bot.reply_to(message, f"E-mail não encontrado.")

# Inicia o bot
bot.polling()
