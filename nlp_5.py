import spacy

nlp = spacy.load('en')
## nlp = spacy.load('en_core_web_sm') use this if the above load does not work

document = nlp('In 1994, Tim Berners-Lee founded the World Wide Web Consortium (W3C), \
                devoted to developing web technologies.') ## \ is a continuation character so you can continue to write even on two lines

for entity in document.ents:
    print(entity.text, ':', entity.label_)

