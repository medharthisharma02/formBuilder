# Define document-related data structures and database interactions
from . import db


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    # Define other fields as necessary
