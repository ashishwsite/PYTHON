# NLTK IS NATURAL LANGUAGE PROSCEESING TOOLKIT LIBREARY IN PHYTHON 
# NLTK HAS MANY __package__ WHICH HELP IN SENTENCE AND WORD formatING 
# ntlk.corpuas() isd used to anlalysis of large data
# nltk.stream() help in streaming of word  streaming means taking root word of sentence 
# ntlk .tokenisation () is help in creating token of word and sentece 
# nltk.corpus.stopwords() method is used to remove stop word from the sentence
# nltk.wordnet () is help in finding synonyms and antonyms in sentence
# nltk.pos_tag() is used to part of speach tagging in sentence 
# ntlk.chunk( ) is hellp in Named Entity Recognition (NER).
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')  # Download the necessary data (tokenizers)
text = "NLTK is a powerful library for natural language processing in Python."
tokens = word_tokenize(text)
print(tokens)
