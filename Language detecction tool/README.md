# Language Translation Tool

A simple web-based language translation tool that allows users to enter text, select source and target languages, and get the translated text using a translation API.

## Features

- Translate text between different languages
- Select source and target languages
- Simple and user-friendly interface
- Copy translated text
- Works directly in the web browser
- Uses an API to process translations

## Technologies Used

- HTML5
- CSS3
- JavaScript
- Translation API
- Fetch API

## Project Structure

Language-Translator/
│
├── index.html
├── style.css
├── script.js
└── README.md

## How It Works

The user enters text in the input box and selects the source and target languages.

When the Translate button is clicked, JavaScript sends the entered text and selected languages to the translation API using the Fetch API.

The API processes the request and returns the translated text in JSON format. JavaScript then extracts the translated result and displays it on the webpage.

User Input
     ↓
Select Languages
     ↓
Click Translate
     ↓
JavaScript Fetch Request
     ↓
Translation API
     ↓
JSON Response
     ↓
Translated Text

API

The project uses a translation API to process the entered text.

The API request contains:

Input text
Source language
Target language

The API returns the translated text as a JSON response.

Example response:

{
    "responseData": {
        "translatedText": "नमस्ते"
    }
}
Supported Languages

The current version includes languages such as:

English
Hindi
French
Spanish
German

More languages can be added by adding their language codes to the language selection dropdowns.


## Future Improvements

Add more languages
Add automatic language detection
Add voice input
Add text-to-speech
Add translation history
Improve the user interface
Add mobile responsive design
Add support for longer text
Add a backend to securely handle API credentials
Learning Outcomes

Through this project, I learned:

Basics of HTML and CSS
JavaScript DOM manipulation
Working with APIs
Using the Fetch API
Handling JSON responses
Using asynchronous JavaScript with async and await
Handling errors in API requests
Building a simple web application

## Author

Harsh Sharma
Electronics and Communication Engineering Student

