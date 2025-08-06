from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    
    # Define the system message to constrain responses to cybersecurity
    system_message = (
        "You are a cybersecurity expert assistant. "
        "Provide long, detailed, and comprehensive answers to user questions. "
        "If a user asks for an explanation, include examples, best practices, and step-by-step details."
    )

    completion = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": message}
        ],
        max_tokens=1000  # Increase this value for longer responses
    )
    
    if completion.choices[0].message:
        return jsonify({"response": completion.choices[0].message.content})
    else:
        return jsonify({"response": "Failed to Generate response!"})

if __name__=='__main__':
    app.run()
