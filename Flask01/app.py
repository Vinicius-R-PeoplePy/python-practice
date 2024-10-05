from flask import Flask, render_template, jsonify, request, redirect, url_for, flash 
import psycopg2, psycopg2.extras
import json 
from decouple import config
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt 
from datetime import datetime


app = Flask(__name__)
app.secret_key = '123'
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
login_manager.login_view = 'login'


# Load database configuration from .env file 
DB_HOST = config('DB_HOST') # localhost
DB_NAME = config('DB_NAME') # your_project
DB_USER = config('DB_USER') # postgres 
DB_PASS = config('DB_PASS') # 123...

def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    return conn 
# add all the contents to .gitignore
# .env file 

class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id 
        self.username = username 
        self.email = email 
        self.password = password 

@login_manager.user_loader 
def load_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    user_data = cur.fetchone()
    cur.close()
    conn.close()

    if user_data:
        return User(user_data[0], user_data[1], user_data[2], user_data[3])
    return None


@app.route('/')
def index():
    return render_template('main.html', username=current_user)


@app.route('/quiz')
@login_required
def quiz():
    return render_template('index.html')

@app.route('/intermediary')
@login_required
def intermediary():
    return render_template('intermediary.html')



@app.route('/api/intermediary/questions/<int:question_id>', methods=['GET'])
def get_intermediary_question(question_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM questions WHERE id = %s AND category = %s;', (question_id, 'intermediary'))
    question = cur.fetchone()
    cur.close()
    conn.close()

    if question is None:
        return jsonify({'error': 'Question not found'}), 404

    formatted_question = {
        'question': question[1],
        'choices': question[2],  # Assuming choices is already in list format
        'correct': question[3]
    }
    return jsonify(formatted_question)




# Route to retrieve questions via Postman
@app.route('/api/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM questions WHERE id = %s;', (question_id,))
    question = cur.fetchone()
    cur.close()
    conn.close()

    if question is None:
        return jsonify({'error': 'Question not found'}), 404

    formatted_question = {
        'question': question[1],
        'choices': question[2],  # Ensure choices is a list
        'correct': question[3]
    }
    return jsonify(formatted_question)


@app.route('/api/questions', methods=['POST'])
def add_question():
    data = request.get_json()

    # Ensure the data is a list of questions
    if not isinstance(data, list):
        return jsonify({'error': 'Expected a list of questions'}), 400

    # Open database connection
    conn = get_db_connection()
    cur = conn.cursor()

    # Loop through each question in the list
    for index, item in enumerate(data):
        question = item.get('question')
        choices = item.get('choices')
        correct_choice = item.get('correct_choice')

        # Validate data
        if not all([question, choices, correct_choice]):
            # Return which question is missing data and what fields are missing
            missing_fields = []
            if not question:
                missing_fields.append('question')
            if not choices:
                missing_fields.append('choices')
            if not correct_choice:
                missing_fields.append('correct_choice')

            return jsonify({
                'error': f'Missing data for question at index {index}',
                'missing_fields': missing_fields,
                'question_data': item
            }), 400

        try:
            # Insert each question into the database
            cur.execute(
                'INSERT INTO questions (question, choices, correct_choice) VALUES (%s, %s, %s)',
                (question, json.dumps(choices), correct_choice)
            )
        except Exception as e:
            # Handle any database errors
            return jsonify({'error': str(e)}), 500

    # Commit changes
    conn.commit()

    # Close cursor and connection
    cur.close()
    conn.close()

    # Return success message
    return jsonify({'message': 'Questions added successfully'}), 201



# Route to update a specific questions via Postman
@app.route('/api/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    data = request.get_json()
    question = data.get('question')
    choices = data.get('choices')
    correct_choice = data.get('correct_choice')

    if not all([question, choices, correct_choice]):
        return jsonify({'error': 'Missing data'}), 400
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE questions SET question = %s, choices = %s, correct_choice = %s WHERE id = %s',
        (question, json.dumps(choices), correct_choice, question_id)
    )
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': f'Question {question_id} updated successfully'}), 200

# Route to delete questions via Postman
@app.route('/api/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM questions WHERE id = %s', (question_id,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'Question deleted succesfully'}), 200

@app.route('/questions/<int:question_id>')
def show_question(question_id):
    return render_template('index.html', question_id=question_id)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = get_db_connection()
        cur = conn.cursor()

        try:
            cur.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                        (username, email, hashed_password))
            conn.commit()
            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash('Error during registration: ' + str(e), 'danger')
        finally:
            cur.close()
            conn.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE email = %s', (email,))
        user_data = cur.fetchone()
        cur.close()
        conn.close()

        if user_data and bcrypt.check_password_hash(user_data[3], password):
            user = User(user_data[0], user_data[1], user_data[2], user_data[3])
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your email and password.', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required 
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required 
def dashboard():
    return render_template('dashboard.html')


@app.route('/submit_score', methods=['POST'])
@login_required
def submit_score():
    data = request.get_json()
    print(f"Received data: {data}")

    if not data or 'correct_answers' not in data or 'incorrect_answers' not in data:
        return jsonify({'error': 'No data received'}), 400
    
    correct_answers = data.get('correct_answers', 0)
    incorrect_answers = data.get('incorrect_answers', 0)


    #if correct_answers is None or incorrect_answers is None:
    #   return jsonify({'error': 'Missing data'}), 400
    total_answers = correct_answers + incorrect_answers
    if total_answers > 0:
        percentage = (correct_answers / total_answers) * 100
    else:
        percentage = 0

    print(f"Submitting score: User ID: {current_user.id}, Correct: {correct_answers}, Incorrect: {incorrect_answers}, Percentage: {percentage}")

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO scores (user_id, correct_answers, incorrect_answers, percentage, date_completed)
            VALUES (%s, %s, %s, %s, %s)
        ''', (current_user.id, correct_answers, incorrect_answers, percentage, datetime.now()))
        conn.commit()
        cur.close()
        conn.close()
        
        print("Score submitted successfully")
        
        return jsonify({'message': 'Score submitted successfully'}), 200
    except Exception as e:
        print(f"Error submitting score: {e}")
        return jsonify({'error': 'Failed to submit score'}), 500



@app.route('/user_score')
@login_required 
def user_score():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            SELECT correct_answers, incorrect_answers, percentage, date_completed
            FROM scores 
            WHERE user_id = %s
            ORDER BY date_completed DESC
        ''', (current_user.id,))
        user_scores = cur.fetchall()
        print(f"Fetched scores for user {current_user.id}: {user_scores}")
        cur.close()
        conn.close()

        return render_template('user_score.html', scores=user_scores)
    except Exception as e:
        print(f"Error fetching scores: {e}")
        return jsonify({'error': 'Failed to fetch scores'}), 500






if __name__ == '__main__':
    app.run(debug=True)

