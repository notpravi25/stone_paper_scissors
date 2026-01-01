from flask import Flask
import os
import random
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Stone Paper Scissors</h1>
    <p>Choose one:</p>

    <a href="/play/stone"><button>🪨 Stone</button></a>
    <a href="/play/paper"><button>📄 Paper</button></a>
    <a href="/play/scissors"><button>✂️ Scissors</button></a>
    """


@app.route("/play/<inp>")
def play(inp):
    choices = ["stone", "paper", "scissors"]

    if inp not in choices:
        return "Invalid choice"

    comp = random.choice(["stone","paper","scissors"])

    if inp == comp:
        result = "tie it iss"
    elif inp == "stone" and comp == "scissors":
        result = "you won"
    elif inp =="scissors" and comp == "paper":
        result = "you won" 
    elif inp =="paper" and comp == "stone":
        result = "you won"
    else:
        result = "computer won brother :("
    return f"""

<h1>Stone Paper Scissors</h1>
<p>You: {inp}</p>
<p>Computer: {comp}</p>
<h2>{result}</h2>
<p>"wanna continue playing???"</p>
<a href = "/"><button>✅ Lessssssssssgooooo!!!</button></a>
<a href = "//"><button>❌ Nah bro, I'm done.</button></a>
"""

@app.route("/stop")
def stop():
    return """
    <h1>Thanks for playing! 👋</h1>
    <p>Refresh the page if you want to play again.</p>
    """


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
