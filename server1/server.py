import os
import os.path
from flask import redirect
from flask import Flask
app = Flask("Server 1")

@app.route("/")
def index():
  return redirect("/static/index.html")

if __name__ == "__main__":
  app.debug = True
  app.run(port=5000)
