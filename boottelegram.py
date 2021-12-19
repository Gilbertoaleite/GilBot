
import telebot

CHAVE_API = ""

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "Estamos enviando o nosso técnico, e em breve ele estará chegando.")

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para reclamação ou elogio envie um email para gilbertoaleite@hotmail.com")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Estamos te encaminhando para atendimento humano, aguarde um momento.")

@bot.message_handler(commands=["opcao4"])
def opcao4(mensagem):
    bot.send_message(mensagem.chat.id, "Nosso Linkedin: https://www.linkedin.com/in/gilbertoaleite")

@bot.message_handler(commands=["opcao5"])
def opcao5(mensagem):
    bot.send_message(mensagem.chat.id, "Nosso Git: https://www.github.com/gilbertoaleite")


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Olá seja bem vindo(a) ao canal do telegram do Gil Technology.
    Escolha uma das opção para continuar (Clique no item):
    /opcao1 Suporte técnico
    /opcao2 Reclamação ou elogico de um atendimento técnico
    /opcao3 Falar com um atendente
    /opcao4 Nosso Likendin 
    /opcao5 Nosso github
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()
