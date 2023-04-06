import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("lion")
word2 = nlp("antelope")
word3 = nlp("water")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('lion antelope fish water')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
