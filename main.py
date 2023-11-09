from flask import Flask, render_template


app=Flask(__name__)



# route => templates

@app.route('/')
def index():
    return render_template('index.html', name="Acceuil")


@app.route('/contact')
def contact():
    return render_template('contact.html', name="contact")


@app.route('/formation')
def formation():
    return render_template('formation.html', name="formation")


@app.route('/propos')
def propos():
    return render_template('propos.html', name="propos")

if __name__=='__main__':
    app.run(debug=True)