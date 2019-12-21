import random
files="file"
words=["india","country","name","education","politics","general","program","journal","chain"]
for i in range(8):

    filelocation="../files/"+files+str(i)+".txt"
    with open(filelocation,"w") as obj:
        word_count=random.randint(0,40)
        for i in range(word_count):
            index=random.randint(0,len(words)-1)
            word=words[index]
            obj.write(word)
            if(i!=word_count-1):
                obj.write(",")
