from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer as PS
from os import listdir
import re

neg_data=[]
pos_data=[]

def doc_read(filename):
    file=open(filename,'r')
    text=file.read()
    file.close()
    tokens=text.lower()
    tokens= re.sub(r'[^\w\s]','',tokens)
    tokens=text.split()
    tokens = [word for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    ps=PS()
    tokens = [ps.stem(w) for w in tokens if not w in stop_words]
    tokens = [word for word in tokens if len(word) > 1]
    return tokens

def process_dir(directory):
    if(directory[-1]=='g'):
        for file in listdir(directory):
            path=directory+"/"+file
            tempv=doc_read(path)
            for i in tempv:
                neg_data.append(i)
    else:
        for file in listdir(directory):
            path=directory+"/"+file
            tempv=doc_read(path)
            for i in tempv:
                pos_data.append(i)

directory1="txt_sentoken/neg"
directory2="txt_sentoken/pos"
process_dir(directory1)
process_dir(directory2)

total_words=[neg_data,pos_data]
"""with open("extracted_words_samples.txt", "w") as file:
    file.write(str(total_words))
    
with open("test.txt", "r") as file:
    data2 = eval(file.readline())"""
bown=[]
bowp=[]
uniqWord1 = sorted(set(neg_data))
for word in uniqWord1:
    bown.append([neg_data.count(word), word])

uniqWord2 = sorted(set(pos_data))
for word in uniqWord2:
    bowp.append([pos_data.count(word), word])
    
finalp=[]
finaln=[]
for i in range(0,len(bown)):
    tmp1=bown[i]
    if(tmp1[0]>5):
        finaln.append(tmp1[1])

for i in range(0,len(bowp)):
    tmp2=bowp[i]
    if(tmp2[0]>5):
        finalp.append(tmp2[1])
        

common=list(set(finalp).intersection(finaln))
commonprob=[]
for i in common:
    probn=neg_data.count(i)
    probp=pos_data.count(i)
    probpos=probp/(probp+probn)
    probneg=probn/(probp+probn)
    commonprob.append([i,probpos,probneg])

        
def Result():
    print("Enter a string to judge sentiment:")
    S=str(input())
    S=S.lower()
    S= re.sub(r'[^\w\s]','',S)
    S=S.split()
    S=[word for word in S if word.isalpha()]
    stop_words=set(stopwords.words('english'))
    ps=PS()
    S = [ps.stem(w) for w in S if not w in stop_words]
    S= [word for word in S if len(word) > 1]
    good=0
    bad=0
    for i in S:
        if(i in common):
            tmpvar1=common.index(i)
            tmpvar2=commonprob[tmpvar1]
            good=good+(S.count(i)*tmpvar2[1])
            bad=bad+(S.count(i)*tmpvar2[2])
        elif(i in finalp):
            good=good+1
        elif(i in finaln):
            bad=bad+1
    for i in range(0,len(S)):
        if(S[i]=='highli' or S[i]=='much'):
            if(S[i+1] in common):
                tmpvar1=common.index(S[i])
                tmpvar2=commonprob[tmpvar1]
                good=good+(2*S.count(i)*tmpvar2[1])
                bad=bad+(2*S.count(i)*tmpvar2[2])
            elif(S[i+1] in finaln):
                bad=bad+2
            elif(S[i+1] in finalp):
                good=good+2
    if(good>bad):
        print("\nPositive")
    else:
        print("\nNegative")

def main():
    r=1
    while(r!=0):
        print("press 0 to exit and 1 to continue")
        reply=int(input())
        if(reply==1):
            Result()
        else:
            r=0
main()