from chatterbot import ChatBot

chatbot = ChatBot (
    "bot",
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
#chatbot.train ('chatterbot.corpus.spanish')
while True:
	usuario =input(">>> ")
	respuesta = chatbot.get_response(usuario)
	print ("Alexa: "+str(respuesta))