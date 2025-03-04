# models.py
# from app import db  # Import the db instance from app.py

# class LeaderboardEntry(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False)
#     score = db.Column(db.Integer, nullable=False)

#     def __repr__(self):
#         return f'<LeaderboardEntry {self.username} {self.score}>'

from app import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
