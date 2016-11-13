import nltk
from nltk.corpus import stopwords

sentence = ""
stop_words = set(stopwords.words("english"))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','#'])

file = open('Paragraph.txt', 'r')

for lin in file:
    sentence += lin

print("{ " + sentence + " }")
# Divide sentence to tokens after remove stop_words......
tokens = nltk.word_tokenize(sentence)

for i in tokens:
    if i in stop_words:
        tokens.remove(i)

print(tokens)

# Tagged tokens .....
tagged = nltk.pos_tag(tokens)
tagged[0:tokens.__sizeof__()]
print("\n")
print(tagged)

#Entities in One Sentence....
entities = nltk.chunk.ne_chunk(tagged)
print("\n")
print (entities)






