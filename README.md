# AI-Powered E-commerce SQL Q&A

🚀 This Flask application uses Google Gemini to convert natural language business questions about e-commerce data into SQL queries and displays the results.
Transform business questions into SQL queries using Google Gemini and get real-time insights from your e-commerce database.

## Features

- Converts English questions to SQLite queries automatically
- Executes queries against a real e-commerce database
- Powered by Google Gemini AI
- Simple web interface

## Setup

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate  # Windows

Gemini Pro: https://deepmind.google/technologies/gemini/pro/

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
### Get an API key:
https://aistudio.google.com/apikey

3. **Get Google API Key**:
   Go to Google AI Studio
   Generate your Gemini API key
   Create a .env file in the project folder:
   ```text
   GOOGLE_API_KEY="your-api-key-here"

4. **Prepare database**:
   Place your SQLite database file named ecommerce.db in the project root
   ``` bash
   python sql.py
   python checkdb.py
   python web.py
   Then open http://localhost:5000 in your browser.
5. **Run the Application**:
    ``` bash
   python web.py
   Then open http://localhost:5000 in your browser.
