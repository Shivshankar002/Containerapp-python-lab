from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Azure Container Apps Lab</title>
        </head>
        <body>
            <h1>Hello from Azure Container Apps!</h1>
            <p>This application was updated locally from VS Code.</p>
            <p>The latest version was deployed through GitHub Actions.</p>
        </body>
    </html>
    """


@app.route("/info")
def info():
    return {
        "application": "Container Apps Python Lab",
        "platform": "Azure Container Apps",
        "deployment": "GitHub Source Code",
        "port": os.environ.get("PORT", "8080")
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)