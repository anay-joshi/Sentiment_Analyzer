
import string
from collections import Counter
import matplotlib.pyplot as plt

import GetOldTweets3 as got

def fetch_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Sushant Singh Rajput') \
        .setSince("2020-07-01") \
        .setUntil("2020-08-30") \
        .setMaxTweets(200)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    tweets_text = [[i.text] for i in tweets]
    return tweets_text


txt= ""
tweets =  fetch_tweets()
for i in range(0,len(tweets)):
    txt = txt + " " + tweets[i][0]

lw=txt.lower()
cleaned_txt = lw.translate(str.maketrans('','',string.punctuation))
#print(cleaned_txt)

t_w = cleaned_txt.split()
#print(t_w)

stop_words =  ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []

for word in t_w:
    if word not in stop_words:
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

fig, ax1 = plt.subplots()
ax1.bar(c.keys(), c.values())
fig.autofmt_xdate()
plt.savefig('result.png')
plt.show()


