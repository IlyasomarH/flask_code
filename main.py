from flask import Flask


app=Flask(__name__)


@app.route('/')
def index():
    return "asc"



@app.route("/user/<userName>")
def user(userName):
    return f"Bonjour {userName}"



if __name__=='__main__':
    app.run(debug=True)