from models import *












# Interroger les données



















# route => templates

@app.route('/')
def index():
<<<<<<< HEAD
    return render_template('index.html', name="Acceuil")


@app.route('/contact')
def contact():
    return render_template('contact.html', name="contact")


=======
    return render_template('index.html', name="acceuil")



@app.route('/contact')
def contact():
    return render_template("contact.html" ,  name="contact")


@app.route("/propos")
def propos():
    return render_template('propos.html', name="propos")

>>>>>>> b12770b
@app.route('/formation')
def formation():
    return render_template('formation.html', name="formation")

<<<<<<< HEAD

@app.route('/propos')
def propos():
    return render_template('propos.html', name="propos")
=======
@app.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.Nom)).scalars()
    return render_template("list.html", users=users)


@app.route('/connexion')
def connexion():
    return render_template('connexion.html', name="connexion")

@app.route('/inscription',methods=["GET", "POST"])
def inscription():
    if request.method == "POST":
        try:
            # Nom=request.form['Nom']
            # email=request.form['email'],
            # password=request.form['pass'],
            
            Nouveau_user=User(request.form['Nom'],request.form['email'] ,request.form['pass'])
            db.session.add(Nouveau_user)
            db.session.commit() 
            return redirect('/connexion')
        except:
            flash("cette utilisateur existe deja, Veuillez renter un nouveau utilisateur")
            return render_template('inscription.html')  
        
    return render_template('inscription.html', name="inscription")
>>>>>>> b12770b

if __name__=='__main__':
        
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
    
    
    
    