from flask import Flask, render_template


app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



# @app.route("/user/<userName>")
# def user(userName):
#     return f"Bonjour {userName}"

@app.route('/contact')
def contact():
    return render_template('contact.html', name="Contact")

if __name__=='__main__':
    app.run(debug=True)