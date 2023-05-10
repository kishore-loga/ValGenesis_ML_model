import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

with open("pdf_output.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Convert text to lowercase
text = text.lower()

# Remove unwanted characters
text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

# Tokenize the text
tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
tokens = [token for token in tokens if not token in stop_words]

#Stemming the text
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in tokens]

stemmed_text = " ".join(stemmed_tokens)

with open("Preprocessed_text.txt", "w") as file:
    file.write(stemmed_text)


