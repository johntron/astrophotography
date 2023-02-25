from nltk import PorterStemmer, WordNetLemmatizer, wordpunct_tokenize

stemmer = PorterStemmer()
lemmer = WordNetLemmatizer()


def tokenize(str: str):
    return wordpunct_tokenize(str.lower().strip())


def normalize(str: str):
    return ' '.join(tokenize(str))


def stem(str: str):
    tokens = tokenize(str)
    stems = [stemmer.stem(token) for token in tokens]
    return ' '.join(stems)
