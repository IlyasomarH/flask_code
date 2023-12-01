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






# ajout 


@app.route('/AjoutUser', methods=["GET", "POST"])
def AjoutUser():
    if request.method=='POST':
        if request.form['pass']== request.form['repass']:
            try:
                
                Nouveau_user=User(request.form['Nom'],request.form['email'] ,request.form['pass'])
                db.session.add(Nouveau_user)
                db.session.commit()
                return redirect(url_for('table'))
            except:
                flash(" persone n'avait pas ajouter ")
        else:
            flash('le deux mot de passes doivent etre egaux') 
            return  render_template('ajoutUser.html')    
    else:
          flash('formulaire n est pas soummis ')      
    return render_template('ajoutUser.html')




# supprimition


@app.route('/suppuser/<int:id>/supprimer')
def suppuser(id):
    try:
        
        user = db.get_or_404(User, id)
        session.pop('user.email',None)
        session.pop('user.username',None)
        db.session.delete(user)
        db.session.commit()
        flash('un user a ete supprimer')
        return redirect(url_for('table'))
    except:
        flash("un user n' a pas  ete supprimer")





@app.route('/modifier/<int:id>/user', methods=['POST', 'GET'])
def modifier(id):
    user1= db.get_or_404(User, id)
    if request.method=='POST':
        try:
            
            user1.Nom=request.form['Nom']
            user1.email=request.form['email']
            user1.password=request.form['pass']
            db.session.commit()
            # user=modifierUser(id, request.form['Nom'], request.form['email'], request.form['password'])
            
            return redirect(url_for('table'))
        except:
            flash("user n'a pas ete modfier")
            return render_template("modifier.html", id)
    else:
        flash('un probleme au niveau de formulaire')
        # return render_template('tableauBord.html')
        
        # return render_template('modifier.html')
    return render_template('modifier.html', user=user1)

@app.route('/modifierUnUser/<int:id>/user')
def modifierUser(id, Nom, email, password):
    user = db.get_or_404(User, id)

    
    user.Nom=Nom
    user.email=email
    user.password=password
    db.session.commit()
    return user


@app.route('/seDeconnecter')
def seDeconnecter():
    session.pop('email', None)
    return  redirect(url_for('index'))









@app.route('/table')
def table():
    if  session :
        
        if session['email']=='ilyas@gmail.com':
            
            users= User.query.all()
            return render_template('tableauBord.html', utilisateurs=users)
        else:
            return redirect(url_for('connexion'))
    else:
        flash("se connecter au tant que Administrasteur")
        
        return redirect(url_for('connexion'))
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
            flash("veuillez remplir tout les champs")
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
    
    
    
    
    