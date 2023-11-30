from models import *












# Interroger les données



















# route => templates

@app.route('/')
def index():
    return render_template('index.html', name="Acceuil")


@app.route('/propos')
def propos():
    return render_template('propos.html', name="propos")



@app.route('/contact')
def contact():
    return render_template('contact.html', name="contact")


@app.route('/formation')
def formation():
    return render_template('formation.html', name="formation")





@app.route('/seDeconnecter')
def seDeconnecter():
    session.pop('email', None)
    return  redirect(url_for('index'))

@app.route('/table')
def table():
    return render_template('tableauBord.html')


@app.route("/users")    
def user_list():
    # users = db.session.execute(db.select(User).order_by(User.Nom)).scalars()
    users=User.query.all()
    return render_template("list.html", users=users)


@app.route('/connexion', methods=["GET", "POST"])
def connexion():
    # Users=User.query.all()
    if request.method=="POST":
        if request.form['email'] and request.form['pass']:
            
            if User.query.filter_by(email=request.form['email'] , password=request.form['pass'] ).all() :
                session['email']=request.form['email']
                return redirect(url_for('index'))
            else:
                flash("l'email ou le passowrd  n'est pas correct")
                return render_template('connexion.html')
        else:
            flash("l'email ou le passowrd  n'est pas correct ")
            return render_template('connexion.html')  
            
    return render_template('connexion.html', name="connexion")

@app.route('/inscription',methods=["GET", "POST"])
def inscription():
    if request.method == "POST":
        if request.form['pass']==request.form['repass']:
            
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
        else:
            
            flash("il faut que les deux password soit le meme")
            return render_template('inscription.html')  
    return render_template('inscription.html', name="inscription")

if __name__=='__main__':
        
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
    
    
    
    