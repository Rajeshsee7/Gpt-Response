from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    try:
        if not request.is_json:
            return jsonify({"error": "Invalid request format"}), 400

        data = request.get_json()

        prompt = data.get("prompt")
        api_key = data.get("apikey")

        if not prompt:
            return jsonify({"error": "Prompt missing"}), 400
        if not api_key:
            return jsonify({"error": "API key missing"}), 400
        
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message.content

        return jsonify({"response": output})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
