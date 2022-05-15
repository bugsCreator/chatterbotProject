# ChatBot

This is the final project of NSDC Course. Made with ML and Some libraries. In this project we learn about chatbot and
how can manually train it with our dataset.

## Summary

#### In this project we create a chat bot using chatterbot library and we train it with our dataset that are downloaded from given website.

## Technologies

- NLP
- ML
- File System
- Serialized Dataset

## How to

### Steps:

- Install python on system
- goto python directory
- then goto script folder and open terminal here (type cmd in search bar and press enter)
- type in cmd "pip install chatterbot"

Now system is ready to code

To get path of python and its binaries

```
import sys
for a in sys.path:
    a.replace('\\\\','\\')
    print(a)
```

or just run

```
python -c "import sys; print('\n'.join(sys.path))"
```

You can see similar

```
'C:\Users\aryan\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages'
```

This is our library path

```
C:\Users\aryan\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0
```

This is our binary path

You have to copy these and save for later

our main.py

```
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
```

Run this code and check for errors

if you have this error

<img src="https://i.ibb.co/Dk5P1tx/ab867f4c-c66b-429e-8430-9b01846bdb45.jpg" />

simple solution of it is just click on last blue text line and follow these steps

<img src ="https://i.ibb.co/Hg9NJ7Z/3fcf36af-f428-4923-b5ba-82ad1653306b.jpg" />

Remove this if block and do like below picture

<img src ="https://i.ibb.co/DpzRSgK/0e5c0b43-3fe5-483d-861e-a73f0fe1e692.jpg" alt="0e5c0b43-3fe5-483d-861e-a73f0fe1e692" />

Now run the code and test it if you face any issues let me know [jay787815@gmail.com](mailto:jay787815@gmail.com)

When all things work properly download the dataset or if you have that's well and good

now you have to create a convert.py

```
# convert dataset to our input format
#dataset link : https://www.kaggle.com/datasets/fac8c12f58184d77b9479fa2d57f3f55589a30a0ca9f6adaccc007eac952bec4?resource=download

text ="""
categories:
  - My Own
  - This is my own data
conversations:
"""
txt = "\n"
fs = open("dialogs.txt",'r')
data = fs.read()
fs.close()
data =data.split("\n")
for d in data:
    question ,answer = d.split("\t")
    # print(question ,answer)
    txt = txt+"  - - "+question+"\n"
    txt = txt + "    - " + answer + "\n"

print(text+txt)

```

Run this code and you will get a test.yml dataset 
in this code we are converting dataset format to our format

now goto your library folder that we get earlier 
``
\site-packages\chatterbot_corpus\data\custom
``

Copy and paste it there 
Now come to main.py and replace this code there

```
trainer.train("chatterbot.corpus.custom.test",
			"chatterbot.corpus.english.conversations" )
```
with 
```
trainer.train("chatterbot.corpus.english.conversations" )
```

now you have bot with your datset you can create own one by editing ``site-packages\chatterbot_corpus\data\custom\myown.yml`` 


Happy coding :)



## Sources

- [Dataset Link](https://www.kaggle.com/datasets/fac8c12f58184d77b9479fa2d57f3f55589a30a0ca9f6adaccc007eac952bec4?resource=download)
- [Chatterbot](https://chatterbot.readthedocs.io/en/stable/)

## Authors

- [@bugsCreator](https://github.com/bugsCreator)