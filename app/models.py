# Add any model classes for Flask-SQLAlchemy here

from datetime import date
from app import db


class Movies(db.Model):
    
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    poster = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.Date)

    def __repr__(self):
        return '<Movie: %r>' % (self.title)
    
    def __init__(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        today = date.today()
        self.created_at = today.strftime('%Y-%m-%d')

    def get_id(self):
            return str(self.id)
