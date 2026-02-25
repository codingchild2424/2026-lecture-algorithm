"""Flask starter template for team projects."""
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html>
<head><title>{{ title }}</title>
<style>
body { font-family: Arial, sans-serif; max-width: 900px; margin: 40px auto; padding: 0 20px; }
nav { background: #333; padding: 10px; margin-bottom: 20px; }
nav a { color: white; margin-right: 15px; text-decoration: none; }
</style>
</head>
<body>
<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
</nav>
<h1>{{ title }}</h1>
<p>{{ message }}</p>
</body>
</html>"""


@app.route("/")
def index():
    return render_template_string(HTML, title="My Algorithm Web App", message="Welcome! Start building your project here.")


@app.route("/about")
def about():
    return render_template_string(HTML, title="About", message="This project demonstrates algorithms in a web application.")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
