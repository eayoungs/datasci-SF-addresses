"""Models and database functions for SFMTA Board Resolutions project."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


##############################################################################
# Model definitions

class Resolutions(db.Model):
    """SFMTA Board Resolutions"""

    __tablename__ = "SFMTA_Resolutions"

    resolution = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    resolution_number = db.Column(db.String(100), nullable=False)
    resolution_letter = db.Column(db.String(100), nullable=False)
    sequence = db.Column(db.Integer(50), nullable=False)
    dpw_street1 = db.Column(db.String(100), nullable=False)
    dpw_street2 = db.Column(db.String(100), nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    action = db.Column(db.String(100))
    category = db.Column(db.String(100))
    res_type = db.Column(db.String(100))
    description = db.Column(db.String(300))


    def __repr__(self):

        return "<Resolution=%s Resolution Number=%s>" % (self.resolution,
                                                         self.resolution_number)


##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///resolution_data'

    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
