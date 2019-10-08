from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), unique=True, nullable=False)
    task = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<List %r>' % self.user

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "task": self.task
        }