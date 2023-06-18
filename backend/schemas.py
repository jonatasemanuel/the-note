from marshmallow import Schema, fields


class NoteSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
