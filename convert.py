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
