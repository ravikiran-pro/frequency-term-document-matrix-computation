import random
files="file"
words=["india","country","name","education","politics","general","program","journal","chain","coder","python","generate","simple","city","proverty","hindustan","jai hind"]
n=int(input("Enter number of  files to be generated"))
for i in range(n):
    filelocation="../files/"+files+str(i)+".txt"
    with open(filelocation,"w") as obj:
        word_count=random.randint(0,1000)
        for i in range(word_count):
            index=random.randint(0,len(words)-1)
            word=words[index]
            obj.write(word)
            if(i!=word_count-1):
                obj.write(",")
