import os
import telebot
from google import genai
from google.genai import types

# Configuração dos Tokens através das Variáveis de Ambiente do Railway
API_TOKEN = os.environ.get('TELEGRAM_TOKEN')
GEMINI_TOKEN = os.environ.get('GEMINI_API_KEY')

bot = telebot.TeleBot(API_TOKEN)
client = genai.Client(api_key=GEMINI_TOKEN)

# Instrução de sistema para definir a personalidade teológica do Bot
SYSTEM_INSTRUCTION = (
    "Você é o 'Bot Debatedor KJV' (ou 'Amigo Fiel'). Seu objetivo é examinar as Escrituras, "
    "analisar argumentos ou passagens bíblicas enviados pelo usuário, e defender a sã doutrina "
    "com base estritamente na perspectiva teológica da Bíblia King James Version (KJV). "
    "Seja preciso, focado em teologia bíblica e responda detalhadamente aos pontos levantados."
)

@bot.message_handler(commands=['comecar', 'ajuda', 'start'])
def enviar_boas_vindas(message):
    boas_vindas = (
        "⚔️ *Bem-vindo ao Bot Debatedor KJV!* ⚔️\n\n"
        "Pronto para examinar as Escrituras? Envie qualquer argumento, "
        "passagem bíblica, e defenderemos a sã doutrina com base na KJV.\n\n"
        "Como posso debater com você hoje?"
    )
    bot.reply_to(message, boas_vindas, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def debatedor(message):
    try:
        # Envia o texto do usuário para o modelo Gemini analisar com a instrução de sistema
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=message.text,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
            ),
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Erro ao processar a análise teológica. Verifique se as chaves da API estão corretas.")

if __name__ == "__main__":
    bot.infinity_polling()
