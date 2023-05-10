from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
import os

# Define the directory containing the documents
doc_dir = 'E:\ValGenesis\Python Files\ValGenesis_ML_model\documents'

# Get a list of the file names in the directory
doc_files = os.listdir(doc_dir)

# Create an empty list to store the TF-IDF results for each document
doc_tfidf = []

# Initialize the vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# Loop through each document file and extract its TF-IDF features
for doc_file in doc_files:
    # Read the document file and extract its text
    with open(os.path.join(doc_dir, doc_file), 'r') as f:
        doc_text = f.read()
        
    # Calculate the TF-IDF features for the document
    tfidf = vectorizer.fit_transform([doc_text])
    
    # Get the feature names and their corresponding scores for the document
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf.toarray()[0]
    
    # Combine the feature names and scores into a dataframe and sort by score
    df = pd.DataFrame({'feature_name': feature_names, 'score': scores})
    df = df.sort_values('score', ascending=False).head(25)
    
    # Add the TF-IDF results for the document to the doc_tfidf list
    doc_tfidf.append(df)

# Combine the TF-IDF results for all documents into a single dataframe
all_tfidf = pd.concat(doc_tfidf, ignore_index=True)

# Create a dictionary of labels for each document file
labels = {'document_0.txt': 0, 'document_1.txt': 1, 'document_2.txt': 2, 'document_3.txt': 3, 'document_4.txt': 4, 'document_5.txt': 5, 'document_6.txt': 6, 'document_7.txt': 7, 'document_8.txt': 8}

# Create a list of labels for each feature in the dataframe
all_labels = []
for doc_file in doc_files:
    label = labels[doc_file]
    all_labels += [label] * 25

# Split the labeled data into a training and validation set
X_train, X_val, y_train, y_val = train_test_split(all_tfidf, all_labels, test_size=0.2, random_state=42)
