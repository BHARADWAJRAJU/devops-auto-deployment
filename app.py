from flask import Flask, jsonify
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>DevOps Auto-Deployment & Server Monitoring System</h1>
    <p>Application is running successfully!</p>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "hostname": socket.gethostname()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
