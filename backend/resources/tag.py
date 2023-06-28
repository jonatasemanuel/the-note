from db import db
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import NoteModel, TagModel
from schemas import TagAndNoteSchema, TagSchema
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("Tags", "tags", description="Operations on tags")


@blp.route("/note/<int:note_id>/tag")
class TagsInNote(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self, note_id):
        note = NoteModel.query.get_or_404(note_id)
        return note.tags.all()

    @blp.arguments(TagSchema)
    @blp.response(201, TagSchema)
    def post(self, tag_data, note_id):
        if TagModel.query.filter(
                TagModel.note_id == note_id,
                TagModel.name == tag_data["name"]).first():
            abort(
                    400,
                    message="A tag with that name already existis in that note"
                    )
        tag = TagModel(**tag_data, note_id=note_id)

        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(
                500,
                message=str(e)
            )

        return tag


@blp.route("/note/<int:note_id>/tag/<int:tag_id>")
class LinkTagsToItem(MethodView):
    @blp.response(201, TagSchema)
    def post(self, note_id,  tag_id):
        note = NoteModel.query.get_or_404(note_id)
        tag = TagModel.query.get_or_404(tag_id)

        note.tags.append(tag)

        try:
            db.session.add(note)
            db.session.commit()
        except SQLAlchemyError:
            abort(
                    500,
                    message="An error occured while inserting the tag."
                    )

    @blp.response(200, TagAndNoteSchema)
    def delete(self, note_id, tag_id):
        note = NoteModel.query.get_or_404(note_id)
        tag = TagModel.query.get_or_404(tag_id)

        note.tags.remove(tag)

        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError:
            abort(
                    500,
                    message="An error occured while inserting the tag."
                    )

        return {"message": "Note removed from tag", "note": note, "tag": tag}


@blp.route("/tag/<int:tag_id>")
class Tag(MethodView):
    @blp.response(200, TagSchema)
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag

    @blp.response(
            202,
            description="Deletes a tag if no item is tagged with it.",
            example={"message": "Tag deleted."}
            )
    @blp.alt_response(404, description="Tag not found.")
    @blp.alt_response(
            400,
            description="Returned if the tag is assigned to one or more notes.\
                    In this case, the tag is not deleted."
            )
    def delete(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)

        if not tag.notes:
            db.session.delete(tag)
            db.session.commit()
            return {"message": "Tag deleted."}
        abort(
                400,
                message="Could not delete tag. Make sure tag is not \
                        associated with any notes, then try again."
            )
