import os
import socket
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  # Get container hostname/ID and region info
  hostname = socket.gethostname()
  return render_template("index.html", server_id=hostname)


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)