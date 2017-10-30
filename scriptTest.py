import glob
import os
import string
import re


file_list = glob.glob(os.path.join(os.getcwd(), "Document", "*"))

corpusss = []

for file_path in file_list:
    with open(file_path) as f_input:
        next(f_input)
        next(f_input)
        next(f_input)
        lines = f_input.read()
        lines = re.sub('-1', '', lines)
        corpusss.append(lines)

print(corpusss)



def build_lexicon(corpus):
    lexicon = set()
    for doc in corpus:
        lexicon.update([word for word in doc.split()])
    return lexicon

def tf(term, document):
    return freq(term, document)

def freq(term, document):
    return document.split().count(term)

vocabulary = build_lexicon(corpusss)

doc_term_matrix = []
print('Our vocabulary vector is [' + ', '.join(list(vocabulary)) + ']')

for doc in corpusss:
    print('The doc is "' + doc + '"')
    tf_vector = [tf(word, doc) for word in vocabulary]
    tf_vector_string = ', '.join(format(freq, 'd')for freq in tf_vector)
    print('the tf vector for Document %d is [%s]'%((corpusss.index(doc)+1), tf_vector_string))
    doc_term_matrix.append(tf_vector)

print('All Combined here is our master document term matrix: ')
print(doc_term_matrix)
