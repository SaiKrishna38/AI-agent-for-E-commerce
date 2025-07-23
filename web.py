from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
load_dotenv()

import os
import sqlite3
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

PROMPT = """
You are an expert in converting English business questions to SQL queries!
The SQL database file is ecommerce.db and it has these tables:

PRODUCT_LEVEL_AD_SALES_METRICS (date TEXT, item_id INTEGER, ad_sales REAL, impressions INTEGER, ad_spend REAL, clicks INTEGER, units_sold INTEGER)
PRODUCT_LEVEL_TOTAL_SALES_METRICS (date TEXT, item_id INTEGER, total_sales REAL, total_units_ordered INTEGER)
PRODUCT_LEVEL_ELIGIBILITY (eligibility_datetime_utc TEXT, item_id INTEGER, eligibility TEXT, message TEXT)

Always generate valid SQLite SQL. Do NOT include the word 'SQL:' in your answer. Do not use ```
"""

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([prompt, question])
    return response.text

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
    except Exception as e:
        rows = [("SQL ERROR: " + str(e),)]
    conn.close()
    return rows

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form.get('question')
        if question:
            try:
                sql_query = get_gemini_response(question, PROMPT)
                results = read_sql_query(sql_query, "ecommerce.db")
                return render_template('index.html', 
                                     question=question,
                                     sql_query=sql_query,
                                     results=results)
            except Exception as e:
                return render_template('index.html', 
                                     error=str(e))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)