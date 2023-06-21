from marshmallow import Schema, fields


class PlainNoteSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    note = fields.Str(required=False)
    created_date = fields.DateTime()
    update_date = fields.DateTime()


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class NoteSchema(PlainNoteSchema):
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class TagSchema(PlainNoteSchema):
    notes = fields.List(fields.Nested(PlainNoteSchema()), dump_only=True)
