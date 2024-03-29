# Spam-Filter-Using-Naive-Bayes
A spam filtering based on Naive Bayes classifier with add-one
smoothing to avoid zero counts 
The same has been deployed on Streamit and can be found here: https://spam-filter-using-naive-bayes-predictor.streamlit.app/

## Problem
Designing a spam filtering based on Naive Bayes classifier and deploying it for demo. You have to implement for both multinomial and multivariate Naive Bayes classifier versions. To avoid zero counts, make sure you also implement the add-one smoothing.
## Dataset
The SMS Spam Collection v.1 (hereafter the corpus) is a set of SMS-tagged messages that have been collected for SMS Spam research. It contains one set of SMS messages in English of 5,574 messages, tagged according to being ham (legitimate) or spam. 

### 1.1. Compilation
-------------

This corpus has been collected from free or free for research sources at the Web:

- A collection of between 425 SMS spam messages extracted manually from the Grumbletext Web site. This is a UK forum in which cell phone users make public claims about SMS spam messages, most of them without reporting the very spam message received. The identification of the text of spam messages in the claims is a very hard and time-consuming task, and it involved carefully scanning hundreds of web pages. The Grumbletext Web site is: http://www.grumbletext.co.uk/
- A list of 450 SMS ham messages collected from Caroline Tag's PhD Theses available at http://etheses.bham.ac.uk/253/1/Tagg09PhD.pdf
- A subset of 3,375 SMS ham messages of the NUS SMS Corpus (NSC), which is a corpus of about 10,000 legitimate messages collected for research at the Department of Computer Science at the National University of Singapore. The messages largely originate from Singaporeans and mostly from students attending the University. These messages were collected from volunteers who were made aware that their contributions were going to be made publicly available. The NUS SMS Corpus is available at: http://www.comp.nus.edu.sg/~rpnlpir/downloads/corpora/smsCorpus/
- The amount of 1,002 SMS ham messages and 322 spam messages extracted from the SMS Spam Corpus v.0.1 Big created by Jos  Mar a G mez Hidalgo and public available at: http://www.esp.uem.es/jmgomez/smsspamcorpus/


### 1.2. Statistics
-------------

There is one collection:

- The SMS Spam Collection v.1 (text file: smsspamcollection) has a total of 4,827 legitimate SMS messages (86.6%) and a total of 747 (13.4%) spam messages.


### 1.3. Format
-------------

The files contain one message per line. Each line is composed by two columns: one with label (ham or spam) and other with the raw text. Here are some examples:

ham   What you doing?how are you? \
ham   Ok lar... Joking wif u oni... \
ham   dun say so early hor... U c already then say... \
ham   MY NO. IN LUTON 0125698789 RING ME IF UR AROUND! H* \
ham   Siva is in hostel aha:-. \
ham   Cos i was out shopping wif darren jus now n i called him 2 ask wat present he wan lor. Then he started guessing who i was wif n he finally guessed darren lor. \
spam   FreeMsg: Txt: CALL to No: 86888 & claim your reward of 3 hours talk time to use from your phone now! ubscribe6GBP/ mnth inc 3hrs 16 stop?txtStop \
spam   Sunshine Quiz! Win a super Sony DVD recorder if you canname the capital of Australia? Text MQUIZ to 82277. B \
spam   URGENT! Your Mobile No 07808726822 was awarded a L2,000 Bonus Caller Prize on 02/09/03! This is our 2nd attempt to contact YOU! Call 0871-872-9758 BOX95QU \

Note: messages are not chronologically sorted.


### 2. Usage
-------------

We offer a comprehensive study of this corpus in the following paper that is under review. This work presents a number of statistics, studies, and baseline results for several machine learning methods.

[1] Almeida, T.A., G mez Hidalgo, J.M., Yamakami, A. Contributions to the study of SMS Spam Filtering: New Collection and Results. Proceedings of the 2011 ACM Symposium on Document Engineering (ACM DOCENG'11), Mountain View, CA, USA, 2011. (Under review)


### 3. About
-------------

The corpus has been collected by Tiago Agostinho de Almeida (http://www.dt.fee.unicamp.br/~tiago) and Jos  Mar a G mez Hidalgo (http://www.esp.uem.es/jmgomez).

We would like to thank Dr. Min-Yen Kan (http://www.comp.nus.edu.sg/~kanmy/) and his team for making the NUS SMS Corpus available. See: http://www.comp.nus.edu.sg/~rpnlpir/downloads/corpora/smsCorpus/. He is currently collecting a bigger SMS corpus at http://wing.comp.nus.edu.sg:8080/SMSCorpus/

## Code

The script reads the dataset stored in SmSSpamCollection.txt and conditions the words by removing unnecessary characters and symbols
https://github.com/shrinha/Spam-Filter-Using-Naive-Bayes/blob/99f222eb2c10c314057f1558d6f2192b1ac2fb0e/Naive%20Bayes%20Spam%20Filter.py#L17-L20

The input message that has to be predicted is stored in the message variable
https://github.com/shrinha/Spam-Filter-Using-Naive-Bayes/blob/99f222eb2c10c314057f1558d6f2192b1ac2fb0e/Naive%20Bayes%20Spam%20Filter.py#L84-L85

The script calculates the probability of each word being a part of a spam message and finally predicts whether the input message is spam or ham
https://github.com/shrinha/Spam-Filter-Using-Naive-Bayes/blob/99f222eb2c10c314057f1558d6f2192b1ac2fb0e/Naive%20Bayes%20Spam%20Filter.py#L91

## Colaboratory

The ipynb file has been provided to show the building of the model, which was later trained. The trained model is pickled and used in app.py for deployment on streamlit
