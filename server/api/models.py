from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    position = db.Column(db.Text, nullable=False)
    addr = db.Column(db.Text, default='')
    min_wage = db.Column(db.Integer, default=0)
    max_wage = db.Column(db.Integer, default=0)
    description = db.Column(db.Text, nullable=False)
    posted = db.Column(db.DateTime, default=db.func.now())
