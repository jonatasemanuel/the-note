from db import db


class NoteModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    tags = db.relationship("TagModel", back_populate="tasks",
                           secondary="tasks_tags")