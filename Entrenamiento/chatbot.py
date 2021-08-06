from chatterbot import ChatBot

chatbot = ChatBot (
    "bot",
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
chatbot.train ('chatterbot.corpus.spanish')