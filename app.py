from flask import Flask, request
from openai import OpenAI
import json
import os

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def chat():
    if request.is_json:
        data = request.get_json()
        user_prompt = data.get('prompt', '')
        setModel = data.get('model', '')
        apikey = os.getenv("API_KEY")
    else:
        return {"error": "Invalid request format"}

    if not user_prompt:
        return {"error": "No prompt provided"}

    client = OpenAI(api_key=apikey)

    # Api format
    response = client.responses.create(
        model=setModel,
        input=user_prompt
    )

    output = response.output_text

    return app.response_class(
        response=json.dumps({"response": output}, ensure_ascii=False),
        mimetype="application/json"
    )
