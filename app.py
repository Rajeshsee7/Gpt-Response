from flask import Flask, request
from openai import OpenAI
import json

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def add():
    if request.is_json:
        data = request.get_json()
        user_prompt = data.get('prompt', '')
        apikey = data.get('apikey', '')
    else:
        return {"error": "Invalid request format"}

    if not user_prompt:
        return {"error": "No prompt provided"}

    client = OpenAI(api_key=apikey)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_prompt}]
    )

    output = response.choices[0].message.content

    return app.response_class(
        response=json.dumps({"response": output}, ensure_ascii=False),
        mimetype="application/json"
    )
