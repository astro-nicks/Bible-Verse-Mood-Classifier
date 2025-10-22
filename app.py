import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("verses.csv")

# Sample mock training data
texts = ["I am happy", "I feel sad", "I am afraid", "I am at peace", "I am hopeful"]
labels = ["joy", "sadness", "fear", "peace", "hope"]

# Train a simple model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

st.title("📖 Bible Verse Mood Classifier")
st.write("Type how you feel, and get an uplifting Bible verse!")

user_input = st.text_input("How are you feeling today?")

if st.button("Get Verse"):
    if user_input:
        X_input = vectorizer.transform([user_input])
        prediction = model.predict(X_input)[0]

        verse_row = data[data['emotion'] == prediction].sample(1).iloc[0]
        st.subheader(f"Emotion detected: {prediction.capitalize()}")
        st.write(f"💬 {verse_row['verse']}")
        st.caption(f"📖 {verse_row['reference']}")
