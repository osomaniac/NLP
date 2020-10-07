# corpus = colleciton of teck
# corpora = plural of corpus

from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)
# print(blob.sentences)
# print(blob.words)
# print(blob.tags)
# print(blob.noun_phrases)
# print(blob.sentiment)
# print(round(blob.sentiment.polarity,3)) # polarity = positive or negative 
# print(round(blob.sentiment.subjectivity,3)) # subjectivity = subjective vs not, how much feeling??

#sentences = blob.sentences

'''
for s in sentences:
    print(s)
    print(s.sentiment)
    print(round(s.sentiment.polarity,3))
    print(round(s.sentiment.subjectivity,3))
'''

from textblob.sentiments import NaiveBayesAnalyzer
blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
# print(blob.sentiment)
sentences = blob.sentences
'''
for s in sentences:
    print(s)
    print(s.sentiment)
'''
'''
print(blob.detect_language())
spanish = blob.translate(to='es')
russian = blob.translate(to='ru')
english = russian.translate(to='en')
print(russian)
print(spanish)
print(english)
'''

from textblob import Word

'''
index = Word('index')
print(index.pluralize())

animals = TextBlob('dog cat fish sheep horse pony bird').words
print(animals.pluralize())

cacti = Word('cacti')
print(cacti.singularize())

word = Word('theyr')
print(word.spellcheck())
word = word.correct()
print(word)
'''
sentence = TextBlob('Ths sentense has misspelld wrds.')
sentence = sentence.correct()
print(sentence)