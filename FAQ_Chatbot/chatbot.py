import pandas as pd
import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

# Read FAQ
faq = pd.read_csv("faq.csv")

questions = faq["Question"].tolist()
answers = faq["Answer"].tolist()

# Stopwords
stop_words = set(stopwords.words("english"))

# ---------------- PREPROCESS ----------------
def preprocess(text):
    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word not in string.punctuation
        and word not in stop_words
    ]

    return " ".join(tokens)

# Preprocess questions
processed_questions = [preprocess(q) for q in questions]

# TF-IDF
vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(processed_questions)

# ---------------- RESPONSE ----------------
def get_response(user_question):

    cleaned = preprocess(user_question)

    user_vector = vectorizer.transform([cleaned])

    similarity = cosine_similarity(user_vector, question_vectors)

    index = similarity.argmax()

    score = similarity[0][index]

    if score < 0.30:
        return "Sorry, I couldn't find a relevant answer."

    return answers[index]

# ---------------- CHATBOT ----------------
print("========== FAQ Chatbot ==========")
print("Type 'exit' to stop.\n")

while True:

    user = input("You : ")

    if user.lower() == "exit":
        print("Bot : Thank you!")
        break

    response = get_response(user)

    print("Bot :", response)