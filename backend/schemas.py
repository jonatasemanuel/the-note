from marshmallow import Schema, fields


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class NoteSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class TagSchema(PlainTagSchema):
    notes = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class TagAndNoteSchema(Schema):
    message = fields.Str()
    note = fields.Nested(NoteSchema)
    tag = fields.Nested(TagSchema)
