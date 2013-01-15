import re
from nltk import wordpunct_tokenize


def get_all_words(text):
    #text = text.encode('utf-8')
    text = text.lower()
    text = re.sub('\d+', ' ', text)
    text = re.sub(ur'\p{P}+', ' ', text)
    
    #print text.encode()
    
    all_tokens = set(wordpunct_tokenize(text.decode('utf-8')))
    result = [token.encode('utf-8') for token in all_tokens if len(token) < 7 and len(token) > 3] 
    return result