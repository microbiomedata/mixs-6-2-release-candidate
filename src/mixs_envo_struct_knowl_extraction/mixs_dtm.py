import random
import re
import string

import nltk
import pandas as pd
from linkml_runtime import SchemaView
from nltk.corpus import words
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('words')

dest_dir = "generated"

schema_sheet = "GSC_MIxS_6_usage_populated_no_blank_cols.tsv"

schema_sheet_column = "Definition"

output_file = f"{dest_dir}/{schema_sheet}.dtm.tsv"

df_raw = pd.read_csv(f"{dest_dir}/{schema_sheet}", sep='\t', dtype=str)

schema_file = f"{dest_dir}/GSC_MIxS_6.yaml"

print(df_raw.shape)

df_desc = df_raw[~df_raw['description'].isnull()]
print(df_desc.shape)

dl_slot_desc = df_desc[["slot", "description"]]
# remove duplicate rows
dl_slot_desc = dl_slot_desc.drop_duplicates()
print(dl_slot_desc.shape)

dl_slot_desc_unique = dl_slot_desc.copy()

dl_slot_desc_unique['unique'] = dl_slot_desc_unique['slot'] + "|" + dl_slot_desc_unique.index.astype(str)

# Create an instance of CountVectorizer with stop word removal, custom tokenizer, and modified token pattern
vectorizer = CountVectorizer(
    stop_words='english',
    tokenizer=lambda text: text.split(),
    token_pattern=r'[a-zA-Z]{2,}',
    # max_features=2500,
    # max_df=0.01
)

# Fit the vectorizer on the Definition column and transform it into a document-term matrix
matrix = vectorizer.fit_transform(dl_slot_desc_unique['description'])

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

dtm_df = pd.DataFrame(filtered_matrix.toarray(), columns=stemmed_feature_names, index=dl_slot_desc_unique['unique'])

row_slot = dtm_df.index.str.split('|', expand=True)

dtm_df.index = row_slot

dtm_df.to_csv(output_file, index=True, sep='\t')

view = SchemaView(schema_file)
