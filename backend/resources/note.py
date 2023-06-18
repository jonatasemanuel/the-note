from db import db
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_sqlalchemy import SQLAlchemy
from models import NoteModel
from schemas import NoteSchema
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("Notes", __name__, description="Operations on notes")


@blp.route("/note")
class NoteList(MethodView):
    @blp.response(200, NoteSchema(many=True))
    def get(self):
        return NoteModel.query.all()

    @blp.arguments(NoteSchema)
    @blp.response(201, NoteSchema)
    def post(self, note_data):
        note = NoteModel(**note_data)

        try:
            db.session.add(note)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return note
