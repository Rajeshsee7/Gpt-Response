from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Render

@app.route("/ask", methods=["POST"])
def add():
    if request.is_json:
        data = request.get_json()
        input = data.get('prompt', '')
        apikey = data.get('apikey', '')
    
    API_KEY = apikey
    client = OpenAI(api_key=API_KEY)  
    prompt = input
    if not prompt:
        return jsonify({"error": "No prompt provided"})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content

return app.response_class(
    response=json.dumps({"response": output}, ensure_ascii=False),
    mimetype="application/json"
)
