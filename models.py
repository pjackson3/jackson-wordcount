"""Declares the data models for the app."""

from app import db
from sqlalchemy.dialects.mysql import JSON


class Result(db.Model):
    """A result."""
    __tablename__ = "results"

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
