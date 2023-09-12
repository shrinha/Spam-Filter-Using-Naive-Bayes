import streamlit as st
import string
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps=PorterStemmer()



def conditioning(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text=text.lower()
    res=[]
    for i in text.split():
      if i not in stopwords.words('english'):
        res.append(ps.stem(i))
    return res





def predict_message(message):
  message=conditioning(message)
  P_spam_given_w=Pspam
  P_ham_given_w=Pham
  
  for i in message:
      if i in spam_dict:
          P_spam_given_w*=P_w_spam[i]
      if i in ham_dict:
          P_ham_given_w*=P_w_ham[i]
  
  if P_spam_given_w > P_ham_given_w:
      st.header("SPAM")
  else:
      st.header("HAM")
      

model=pickle.load(open('model.pkl','rb'))

spam_dict=model[0]
ham_dict=model[1]
Pspam=model[2]
Pham=model[3]
P_w_spam=model[4]
P_w_ham=model[5]




st.title("Email/SMS SPAM Classifer")
message=st.text_area("Enter the message")

if st.button('Predict'):
    print("Button Pressed")
    predict_message(message)      
