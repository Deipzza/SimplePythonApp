from flask import Flask, render_template

app = Flask(__name__)  # Create a Flask instance.

@app.route("/")
def home():
    """Returns the main app page."""
    
    return render_template("index.html")

@app.route("/surprise")
def surprise():
    """Returns tan easter egg page."""

    return '<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank">Click me for an easter egg ;)</a>'