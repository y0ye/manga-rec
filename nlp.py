import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    # Use pandas.read_csv with delimiter='\t', header=None, names=['sentence', 'label']
    #################
    df = pd.read_csv(low_memory=False, filepath_or_buffer='manga.csv', delimiter=',', header=None, names=['manga_id', 'title', 'type', 'score', 'scored_by', 'status', 'volumes', 'chapters', 'start_date', 'end_date', 'members', 'favorites', 'sfw', 'approved', 'created_at_before', 'updated_at', 'real_start_date', 'real_end_date', 'genres', 'themes', 'demographics', 'authors', 'serializations', 'synopsis', 'background', 'main_picture', 'url', 'title_english', 'title_japanese', 'title_synonyms'] )
    #################
    pass
except FileNotFoundError:
    print("Dataset files not found. Please ensure the dataset files are in the current directory.")
    exit()

df.drop(columns=['type', 'score', 'scored_by', 'status', 'volumes', 'chapters', 'start_date', 'end_date', 'members', 'favorites', 'sfw', 'approved', 'created_at_before', 'updated_at', 'real_start_date', 'real_end_date', 'demographics', 'authors', 'serializations','background', 'main_picture', 'url', 'title_japanese', 'title_english', 'title_synonyms'], inplace=True, axis=1)

print(df.head(5))

# Check for missing values using df.isnull().sum()
print("\nMissing values in each column:")
#################
print(df.isnull().sum())
#################

# Check for duplicates using df.duplicated().sum()
print("\nNumber of duplicate rows:")
#################
print(df.duplicated().sum())
#################

# Visualize label distribution using df['label'].value_counts()
print("\nLabel distribution:")
#################
print(df['genres'].value_counts())
#################

# Drop rows with missing synopsis
print("Dropping rows with missing synopsis....")
df.dropna(subset=['synopsis'], inplace=True)
print("\nMissing values in each column:")
#################
print(df.isnull().sum())
#################

# Initialize stop words
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation and special characters using re.sub()
    text = re.sub(r'[^\w\s]', '', text)
    # Remove digits using re.sub()
    text = re.sub(r'\d+', '', text)
    # Split text into words (tokens) using str.split()
    words = text.split()
    # Remove stop words
    words = [word for word in words if word not in stop_words]
    return words

# Apply preprocessing to the 'sentence' column using df['sentence'].apply()
#################
df = df.assign(tokens=df['synopsis'].apply(preprocess_text))
#################
print(df.head(5))

# Step 4: Build Vocabulary and Tokenize Text
# Build vocabulary
vocab_size = 10000  # Set vocabulary size
all_tokens = [token for tokens in df['tokens'] for token in tokens]
most_common_tokens = Counter(all_tokens).most_common(vocab_size - 2)  # Reserve 2 indices for special tokens

# Create mappings
word_to_idx = {word: idx + 2 for idx, (word, _) in enumerate(most_common_tokens)}
word_to_idx['<PAD>'] = 0
word_to_idx['<UNK>'] = 1
idx_to_word = {idx: word for word, idx in word_to_idx.items()}

def tokens_to_indices(tokens):
    # Convert tokens to indices, use '<UNK>' for unknown words
    indices = [word_to_idx.get(token, word_to_idx['<UNK>']) for token in tokens]
    return indices

# Convert tokens to indices
df['indices'] = df['tokens'].apply(tokens_to_indices)

# User input: Get the user's desired manga title or a snippet of synopsis
user_input = input("Enter a manga title or a brief synopsis to get recommendations: ")

# If user input is a title, find the corresponding synopsis
if user_input in df['title'].values:
    user_synopsis = df.loc[df['title'] == user_input, 'synopsis'].values[0]
else:
    user_synopsis = user_input  # Use the user's input directly if it's a synopsis

# Combine the user input (synopsis) with all available synopses
all_synopses = df['synopsis'].tolist() + [user_synopsis]

# Initialize a TfidfVectorizer to convert text to TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english')

# Fit the vectorizer on all synopses (including user input)
tfidf_matrix = vectorizer.fit_transform(all_synopses)

# Compute cosine similarity between the user input and all synopses
cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

# Get indices of the most similar manga
top_n = 10  # Number of recommendations to show
similar_indices = cosine_sim.argsort()[0][-top_n:][::-1]

# Print out the top N most similar manga
print("\nTop {} recommendations based on your input:".format(top_n))
for idx in similar_indices:
    recommended_title = df.iloc[idx]['title']
    print(f" - {recommended_title}")
