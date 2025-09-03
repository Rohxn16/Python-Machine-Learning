from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

words = ["Python", "Pythoner", "Pythoned", "Pythonic", "Pythoner"]
sent = "I "
for w in words:
    print(ps.stem(w))