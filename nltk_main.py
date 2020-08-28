#Natural Language Processing

import string
from collections import Counter
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

txt=open('data.txt',encoding='utf-8').read()
lw=txt.lower()

cleaned_txt = lw.translate(str.maketrans('','',string.punctuation))
#print(cleaned_txt)

t_w = word_tokenize(cleaned_txt,"english")
#print(t_w)

final_words = []

for word in t_w:
    if word not in stopwords.words("english"):
        final_words.append(word)

#print(final_words)

em_list = []

with open('emotion.txt','r') as emo:
    for l in emo:
        c_l = l.replace("\n","").replace("'",'').strip()
        w,em = c_l.split(":")

        if w in final_words:
            em_list.append(em)

print(em_list)
c= Counter(em_list)
print(c)

def final_emotion(final_txt):
    result = SentimentIntensityAnalyzer().polarity_scores(final_txt)
    post = result['pos']
    negat = result['neg']
    if post>negat :
        print("Overall Emotion is Postive")
    elif negat>post :
        print("Overall Emotion is Negative")
    else:
        print("Neutral")

final_emotion(cleaned_txt)

fig, ax1 = plt.subplots()
ax1.bar(c.keys(), c.values())
fig.autofmt_xdate()
plt.savefig('result.png')
plt.show()


