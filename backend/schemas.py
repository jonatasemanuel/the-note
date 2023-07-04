from marshmallow import Schema, fields


class PlainNoteSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    note = fields.Str(required=False)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class PlainNoteUpdateSchema(Schema):
    title = fields.Str(required=True)
    notes = fields.Str(required=False)
    updated_date = fields.DateTime()


class NoteSchema(PlainNoteSchema):
    tags = fields.List(fields.Nested(PlainTagSchema()))


class TagSchema(PlainTagSchema):
    note_id = fields.Int(load_only=True)
    notes = fields.List(fields.Nested(PlainNoteSchema()))


class TagAndNoteSchema(Schema):
    message = fields.Str()
    note = fields.Nested(NoteSchema)
    tag = fields.Nested(TagSchema)
