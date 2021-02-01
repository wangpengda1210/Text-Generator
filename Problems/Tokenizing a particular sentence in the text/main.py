from nltk.tokenize import sent_tokenize
from nltk.tokenize import regexp_tokenize

sentence = sent_tokenize(input())[int(input())]
print(regexp_tokenize(sentence, "[A-z']+"))
