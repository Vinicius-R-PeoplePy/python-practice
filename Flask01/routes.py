from flask import Flask, render_template, redirect, url_for, flash, request 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager, login_user 
from werkzeug.security import generate_password_hash 

app  = Flask(__name__)
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Route for user registration 
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if user exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please login.')
            return redirect(url_for('login'))
        
        # Create new user
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration succesful! Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')