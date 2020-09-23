from flask import Flask , render_template , request #allows you to render any HTML file

from flask_sqlalchemy import SQLAlchemy 
# initialize app


app = Flask(__name__)
# data base

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///static/database/users.db'

db = SQLAlchemy(app)



# model schema
class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))

# Route
@app.route('/')
def index():
    return 'Data science optimizer'



# Adding HTML added homepage
@app.route('/home')
def home():
    return render_template('home.html')



    
    # Returns False because the first key is false.
    # For dictionaries the all() function checks the keys, not the values.

# Templating
@app.route('/about')
def about():
    # to pass in data from the backend
    mission = 'Optimizing Data and ML models'

    return render_temame = request.form["lastname"]
        single_user= User(firstname=firstname, lastname=lastname)
        db.session.add(single_user)
        db.session.commit()

    return render_template('home.html', firstname= firstname, lastname= lastname)

@app.route('/allusers')
# storing everythingplate('about.html', mission=mission)


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        firstname= request.form["firstname"]
        lastn inside userslist 
def allusers():
    userslist= User.query.all()
    print(userslist)
    return render_template('results.html', userslist=userslist)


@app.route('/profile/<firstname>')
def profile(firstname):
    user = User.query.filter_by(firstname= firstname).first()
    return render_template('profile.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)