from datetime import datetime

from db import db


class NoteModel(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    note = db.Column(db.Text)
    tags = db.relationship("TagModel",
                           back_populates="note",
                           lazy="dynamic")
    created_date = db.Column(db.DateTime(), default=datetime.now)
    updated_date = db.Column(db.DateTime(), default=datetime.now,
                             onupdate=datetime.now)
    # notes = db.relationship("NoteModel",
    #                         back_populates="note",
    #                         lazy="dynamic",
    #                         cascade="all, delete")
