# FAQ Chatbot

This project is a simple FAQ chatbot made using Python and Natural Language Processing. It takes a question from the user, compares it with the questions stored in an FAQ dataset, and gives the most relevant answer.

The project uses NLTK for preprocessing and Scikit-learn for TF-IDF and cosine similarity.

## Features

- Reads FAQ questions and answers from a CSV file
- Converts text to lowercase
- Removes punctuation and stopwords
- Tokenizes the questions using NLTK
- Uses TF-IDF to convert text into numerical vectors
- Uses cosine similarity to find the closest FAQ
- Returns the answer of the most similar question
- Runs through a simple command-line interface

## Technologies Used

- Python
- NLTK
- Pandas
- Scikit-learn
- CSV

## Project Structure


FAQ_Chatbot/
│
├── chatbot.py
├── faq.csv
├── README.md
└── requirements.txt

## How It Works

The chatbot works in a few basic steps.

First, the FAQ data is loaded from faq.csv.

The questions are then preprocessed using NLTK. The preprocessing includes converting the text to lowercase, tokenizing it, and removing punctuation and stopwords.

After preprocessing, TF-IDF is used to convert the questions into numerical vectors.

When the user enters a question, the same preprocessing is applied to it. The chatbot then compares the user's question with all the FAQ questions using cosine similarity.

The question with the highest similarity score is selected and its corresponding answer is displayed.

## Example
========== FAQ Chatbot ==========
Type 'exit' to stop.

You : How can I return my product?

Bot : You can return products within 30 days with the original receipt.

You : How do I track my package?

Bot : Use the tracking link sent to your email after shipping.

You : I forgot my password

Bot : Click on the 'Forgot Password' option on the login page.

You : exit

Bot : Thank you!
## FAQ Dataset

The current dataset contains questions related to common e-commerce topics such as:

Return policy
Order tracking
International shipping
Order cancellation
Payment methods
Customer support
Delivery time
Product exchange
Cash on delivery
Password reset

The questions and answers can be changed in faq.csv according to the required topic.

## Installation

Make sure Python is installed on your system.

Install the required libraries:

pip install pandas nltk scikit-learn

The required packages can also be installed using:

pip install -r requirements.txt
## Running the Project

Open the project folder in the terminal and run:

python chatbot.py

The chatbot will start in the terminal and wait for a question.

Type exit to close the chatbot.

Similarity Threshold

The chatbot uses a similarity threshold to avoid returning an unrelated answer.

if score < 0.30:
    return "Sorry, I couldn't find a relevant answer."

If the similarity score is lower than the threshold, the chatbot tells the user that it could not find a suitable answer.

## Future Improvements

Some improvements that can be added to the project are:

Add a web-based chat interface
Use Streamlit for a better UI
Add more FAQs
Use SpaCy for better text preprocessing
Use BERT or Sentence Transformers for better semantic matching
Add spelling correction
Store FAQs in a database
Add voice input and output

## Author

Harsh Sharma
Electronics and Communication Engineering Student

