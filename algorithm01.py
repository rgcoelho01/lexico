import ConexaoPostgres
from nltk.util import ngrams

def get_ngrams(text, n ):
    n_grams = ngrams(text, n)
    return [ ' '.join(grams) for grams in n_grams]

def freq(text): 
    unique_words = set(text)
    print(unique_words)
    for words in unique_words: 
        print('Frequencia de :', words , ':', text.count(words)) 

with open('stopwords.txt') as stopwords:
    list_stopwords = stopwords.read().split()

with open('punctuation.txt') as punctuation:
    list_punctuation = punctuation.read().split()

#text = "Ipap papai nosso am? viu nosso a e u viu viu viu in aware that que viu voce que era voce que nltk only offers bigrams and trigrams, adivinha so...  but is there a way to split my text in four-grams, five-grams or even hundred-grams."
text = "Ipap papai nosso am? viu papai nosso .  a e u viu viu e u viu in aware that que viu "
# Convert text to lowercase
text = text.lower()

# Split a string into a list
text_split = text.split()


#Remove Punctuation
list_punctuation_str = ''.join(list_punctuation)
text_no_punctuation =[]
for x in text_split:
    if x.strip(list_punctuation_str) > '':
        text_no_punctuation.append(x.strip(list_punctuation_str))

# Number of words
ngrams2 = get_ngrams(text_no_punctuation,2)
ngrams3 = get_ngrams(text_no_punctuation,3)
ngrams4 = get_ngrams(text_no_punctuation,4)

#Remove Stopwords only ngram = 1
text_no_stopwords = []
for x in text_no_punctuation:
    if x not in list_stopwords:
        text_no_stopwords.append(x)

ngrams1 = text_no_stopwords
total_grams1 = len(ngrams1)
total_grams2 = len(ngrams2)
total_grams3 = len(ngrams3)
total_grams4 = len(ngrams4)


print (total_grams1)
print (ngrams1)
freq(get_ngrams(ngrams1,1))
print (total_grams2)
print (ngrams2)
freq(get_ngrams(ngrams2,1))
print (total_grams3)
print (ngrams3)
freq(get_ngrams(ngrams3,1))
print (total_grams4)
print (ngrams4)
freq(get_ngrams(ngrams4,1))
