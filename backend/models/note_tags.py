from db import db


class NoteTags(db.Model):
    __tablename__ = "notes_tags"

    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer, db.ForeignKey("notes.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))
