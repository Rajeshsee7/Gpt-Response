from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    if request.is_json:
data = request.get_json()
num1 = data.get('num1', '')
apikey = data.get('apikey', '')
        
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return jsonify({"response": response.choices[0].message.content})

   
