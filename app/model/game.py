import json
from app import db


class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.String, primary_key=True)
    state = db.Column(db.Text)
    song = db.Column(db.Text)
    scores = db.Column(db.Text)
    difficulty = db.Column(db.Text)
    
    def __init__(self, chatId, state, song=None, scores=json.dumps(dict()), difficulty=50):
        self.id = chatId
        self.state = state
        self.song = song
        self.scores = scores
        self.difficulty = difficulty

    def __repr__(self):
        return '<Game %r>' % self.state
