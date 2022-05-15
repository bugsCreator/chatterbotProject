# Import "chatbot" from
# chatterbot package.
from chatterbot import ChatBot
import nltk
# Inorder to train our bot, we have
# to import a trainer package
# "ChatterBotCorpusTrainer"
from chatterbot.trainers import ChatterBotCorpusTrainer


# Give a name to the chatbot “corona bot”
# and assign a trainer component.
chatbot=ChatBot('corona bot')
#C:\Users\aryan\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\Roaming
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
#
# # Now let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.conversations" )

while True:
	a = input("Enter Text :")
	if a =="exit":
		break
	response = chatbot.get_response(a)
	print(response)



