from flask import flask
app = flask(__name__)

@app.route("/")
def hello_world():
 return "aichatbot"

 if __name__ == "__main_":
  app.run()
