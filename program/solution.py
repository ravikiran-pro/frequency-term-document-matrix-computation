import csv
import os
total=[]
def individual_count(filename,tokens,counter):
    file_location="../files/"+filename
    counter[0]=filename
    word=""
    with open(file_location,"r") as obj:
        for i in obj.read():
            if i is ",":
                i=tokens.index(word)
                counter[i]+=1
                total[i]+=1
                word=""
            else:
                word+=i
    writer(counter)

def get_overall_tokens():
    tokens=["filename"]
    for i in files:
        file_location="../files/"+i 
        column=[]
        word=""
        with open(file_location,"r") as obj:
            for i in obj.read():
                if i is ",":
                    if word not in tokens:
                        tokens.append(word)
                    word=""
                else:
                    word+=i
    writer(tokens)
    return tokens

def writer(list):
    with open('../output/unigrams.csv', mode='a') as obj:
        obj_w = csv.writer(obj, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        obj_w.writerow(list)

if __name__=="__main__":
    files=os.listdir("../files")
    tokens=get_overall_tokens()
    counter=[]
    for i in tokens:
        counter.append(0)
    counter[0]="total"
    total.extend(counter)
    for i in range(len(files)):
        individual_count(files[i],tokens,counter[:])
    writer(total)
