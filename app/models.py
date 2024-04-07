# Add any model classes for Flask-SQLAlchemy here

from datetime import datetime
from app import db


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    poster = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return f"Movie('{self.title}', '{self.description}', '{self.poster}', '{self.created_at}')"