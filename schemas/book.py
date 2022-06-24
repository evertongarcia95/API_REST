from ma import ma
from models.book import BookModel
from marshmallow import fields


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel
        load_instance = True
