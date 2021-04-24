from chatbot_engine import chatbot_engine

from flask import Flask, render_template, request

chatbot_engine_obj = chatbot_engine()

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot_engine_obj.get_response(userText))


if __name__ == "__main__":
    app.run()