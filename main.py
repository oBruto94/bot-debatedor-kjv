import os
import telebot

API_TOKEN = os.environ.get('TELEGRAM_TOKEN', 'COLE_SEU_TOKEN_DO_BOTFATHER_AQUI')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    boas_vindas = (
        "⚔️ *Bem-vindo ao Bot Debatedor KJV!* ⚔️\n\n"
        "Pronto para examinar as Escrituras? Envie qualquer argumento, "
        "passagem bíblica, e defenderemos a sã doutrina "
        "com base na KJV.\n\n"
        "Como posso debater com você hoje?"
    )
    bot.reply_to(message, boas_vindas, parse_mode='Markdown')
@bot.message_handler(func=lambda message: True)
def debater(message):
    texto_usuario = message.text.lower()
    if "graça" in texto_usuario or "salvação" in texto_usuario:
        resposta = "De acordo com as Escrituras (Efésios 2:8), pela graça sois salvos, por meio da fé. A KJV mantém firme o fundamento da Graça Incondicional!"
    elif "lei" in texto_usuario or "obras" in texto_usuario:
        resposta = "Lembre-se do que a sã doutrina expõe: o homem não é justificado pelas obras da lei, mas pela fé em Jesus Cristo (Gálatas 2:16)."
    else:
        resposta = f"Analisando o seu argumento: '{message.text}'...\n\nÀ luz da teologia bíblica e da precisão da KJV, precisamos ponderar se essa afirmação se sustenta. Qual o seu próximo ponto?"
    bot.reply_to(message, resposta)
if __name__ == '__main__':
    print("Bot Debatedor KJV ativo...")
    bot.infinity_polling()
