from db import db


class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)
    note_id = db.Column(db.String(),
                        db.ForeignKey("notes.id"),
                        nullable=False)
    note = db.relationship("NoteModel", back_populates="tags")
    notes = db.relationship("NoteModel", back_populates="tags",
                            secondary="note_tags")
