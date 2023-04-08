import string 


f=open('SMSSpamCollection.txt' , 'r')


vocab={}
spamcount=0
hamcount=0

Nspam=0 
Nham=0

spam_dict={}
ham_dict={}

def conditioning(word):
    word = word.translate(str.maketrans('', '', string.punctuation))
    res=word.lower()
    return res 


    
for i in f:
    line=i.split()
    if line[0]=='spam':
        spamcount+=1
        line.pop(0)
        for word in line:
            Nspam+=1
            word=conditioning(word)
            if word in spam_dict:
                spam_dict[word]+=1
            else:
                spam_dict[word]=1



    else:
        hamcount+=1
        line.pop(0)
        for word in line:
            Nham+=1
            word=conditioning(word)
            if word in ham_dict:
                ham_dict[word]+=1
            else:
                ham_dict[word]=1
         
   


Pspam=spamcount/(spamcount+hamcount)
Pham=1-Pspam

s1=set(spam_dict.keys())
s2=set(ham_dict.keys())
vocab=s1.union(s2)
Nvocab=len(vocab)



print(spam_dict)
print()
print()
print(ham_dict)
print()
print()
print(Nvocab)
print(Nspam)
print(Nham)

P_w_spam={}
P_w_ham={}

for i in spam_dict:
    P_w_spam[i]=(spam_dict[i] + 1)/(Nspam+Nvocab)


for i in ham_dict:
    P_w_ham[i]=(ham_dict[i] + 1)/(Nham+Nvocab)


message="I have a brother"
message=conditioning(message)

P_spam_given_w=Pspam
P_ham_given_w=Pham


for i in message.split():
    if i in spam_dict:
        P_spam_given_w*=P_w_spam[i]
    if i in ham_dict:
        P_ham_given_w*=P_w_ham[i]



print(P_spam_given_w, P_ham_given_w)

if P_spam_given_w > P_ham_given_w:
    print("SPAM")
else:
    print("HAM")


