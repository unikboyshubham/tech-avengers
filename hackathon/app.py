from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy  # Uncomment if using SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Configure your database
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #suppress a warning
# db = SQLAlchemy(app)  # Initialize SQLAlchemy

# Assuming you have a database model for Leaderboard
# from models import LeaderboardEntry

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/learning')
def learning():
    return render_template('learning.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Process quiz answers, calculate score (replace with actual logic)
        score = calculate_quiz_score(request.form)  # Replace with actual quiz processing
        username = request.form.get('username', 'Anonymous')

        # Assuming you have a LeaderboardEntry model
        # new_entry = LeaderboardEntry(username=username, score=score)
        # db.session.add(new_entry)
        # db.session.commit()

        return redirect(url_for('leaderboard'))

    return render_template('quiz.html')


def calculate_quiz_score(form_data):
    # Dummy function for calculating quiz score.  REPLACE with your actual logic.
    score = 0
    if form_data.get('q1') == 'a':  # Example: if answer to question 1 is 'a'
        score += 10
    # Add more questions and scoring logic here
    return score


@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/game1')
def game1():
    return render_template('game1.html')

@app.route('/game2')
def game2():
    return render_template('game2.html')

@app.route('/leaderboard')
def leaderboard():
    # Assuming you want to fetch leaderboard entries from the database
    # leaderboard_entries = LeaderboardEntry.query.order_by(LeaderboardEntry.score.desc()).limit(10).all()
    # return render_template('leaderboard.html', entries=leaderboard_entries)

    # Example dummy leaderboard data if no database is set up:
    dummy_entries = [
        {'username': 'Alice', 'score': 95},
        {'username': 'Bob', 'score': 80},
        {'username': 'Charlie', 'score': 70}
    ]
    return render_template('leaderboard.html', entries=dummy_entries)



if __name__ == '__main__':
    app.run(debug=True)
