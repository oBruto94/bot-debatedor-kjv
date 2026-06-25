import os
import telebot
import google.generativeai as genai

# Puxa as chaves de configuração do Railway
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configura a IA da Google com a sua chave
genai.configure(api_key=GEMINI_API_KEY)

# Inicializa o Bot do Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Bem-vindo ao Bot Debatedor KJV! Envie qualquer argumento ou passagem bíblica, e defenderemos a sã doutrina com base na KJV. Como posso debater com você hoje?")

@bot.message_handler(func=lambda message: True)
def responder_gemini(message):
    try:
        # Define o modelo clássico e estável da Google
        model = genai.GenerativeModel('gemini-pro')
        
        # Cria o contexto teológico
        contexto = (
            "Você é um debatedor teológico experiente e fiel defensor da sã doutrina bíblica "
            "com base estrita na Bíblia King James Version (KJV). Responda ao usuário argumentando "
            "e debatendo de forma profunda, respeitosa e teologicamente sólida. "
            "Aqui está o argumento do usuário: "
        )
        
        # Gera a resposta
        response = model.generate_content(contexto + message.text)
        
        # Envia de volta para o Telegram
        bot.reply_to(message, response.text)
        
    except Exception as e:
        print(f"Erro: {e}")
        bot.reply_to(message, "Desculpe, tive um problema ao processar seu argumento. Tente novamente.")

# Mantém o robô rodando
bot.infinity_polling()
