import os
import telebot
from google import genai

# Puxa as chaves de configuração do Railway
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Inicializa o Bot do Telegram e o Gemini
bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Bem-vindo ao Bot Debatedor KJV! Envie qualquer argumento ou passagem bíblica, e defenderemos a sã doutrina com base na KJV. Como posso debater com você hoje?")

@bot.message_handler(func=lambda message: True)
def responder_gemini(message):
    try:
        # Cria o contexto para o robô agir como um debatedor teológico baseado na KJV
        contexto = (
            "Você é um debatedor teológico experiente e fiel defensor da sã doutrina bíblica "
            "com base estrita na Bíblia King James Version (KJV). Responda ao usuário argumentando "
            "e debatendo de forma profunda, respeitosa e teologicamente sólida. "
            "Aqui está o argumento do usuário: "
        )
        
        # Envia a pergunta para a Inteligência Artificial do Gemini
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=contexto + message.text,
        )
        
        # Envia a resposta da IA de volta para o usuário no Telegram
        bot.reply_to(message, response.text)
        
    except Exception as e:
        print(f"Erro: {e}")
        bot.reply_to(message, "Desculpe, tive um problema interno ao processar seu argumento com a IA. Tente novamente.")

# Mantém o robô rodando direto
bot.infinity_polling()
