import os
import re

# Create a folder to save the documents
if not os.path.exists("documents"):
    os.makedirs("documents")

# Open the preprocessed text file
with open("Preprocessed_text.txt", "r") as file:
    text = file.read()

# Split the text into individual documents
documents = re.split(r'\[Document -\d+\]', text)

# Remove empty strings from the documents list
documents = [doc.strip() for doc in documents if doc.strip()]

# Write each document to a separate file in the documents folder
for i, doc in enumerate(documents):
    filename = f"document_{i}.txt"
    with open(os.path.join("documents", filename), "w") as file:
        file.write(doc)
    print(f"Saved {filename} in the documents folder")
