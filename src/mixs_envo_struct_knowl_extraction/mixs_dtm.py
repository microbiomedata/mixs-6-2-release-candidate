import random
import re
import string

import nltk
import pandas as pd
from nltk.corpus import words
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('words')

dest_dir = "generated"

combined_sheets = "mixs_v6.xlsx.harmonized.tsv"

output_file = f"{dest_dir}/{combined_sheets}.dtm.tsv"


def gen_rand_letter_number(k=2):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=k))
    return random_string


def replace_punctuation_and_whitespace(text):
    stripped = text.strip()

    # Replace punctuation and whitespace with underscores
    replaced = re.sub(r'\W+', '_', stripped)

    # Remove consecutive underscores
    final_result = re.sub(r'_{2,}', '_', replaced)

    # trim leading and trailing whitespace

    return final_result


df = pd.read_csv(f"{dest_dir}/{combined_sheets}", sep='\t', dtype=str)

# Create an instance of CountVectorizer with stop word removal, custom tokenizer, and modified token pattern
vectorizer = CountVectorizer(
    stop_words='english',
    tokenizer=lambda text: text.split(),
    token_pattern=r'[a-zA-Z]{2,}',
    # max_features=2500,
    # max_df=0.01
)

# Fit the vectorizer on the Definition column and transform it into a document-term matrix
matrix = vectorizer.fit_transform(df['Definition'])

# Get the feature names (terms)
feature_names = vectorizer.get_feature_names_out()

# Load a dictionary of valid words (e.g., from NLTK's word corpus)
valid_words = set(words.words())

# Filter the feature names to include only dictionary words
dictionary_feature_names = [word for word in feature_names if word in valid_words]

# Apply stemming to the dictionary feature names using PorterStemmer
stemmer = PorterStemmer()
stemmed_feature_names = [stemmer.stem(word) for word in dictionary_feature_names]

# Filter the document-term matrix to include only the columns corresponding to the dictionary feature names
filtered_matrix = matrix[:, [vectorizer.vocabulary_[word] for word in dictionary_feature_names]]

# # Create a new DataFrame for the filtered document-term matrix with the stemmed dictionary feature names
# dtm_df = pd.DataFrame(filtered_matrix.toarray(), columns=stemmed_feature_names, index=df['unique_id'])
dtm_df = pd.DataFrame(filtered_matrix.toarray(), columns=stemmed_feature_names)

dtm_df.to_csv(output_file, index=True, sep='\t')
