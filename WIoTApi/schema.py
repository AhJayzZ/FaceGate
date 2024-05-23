from flask_marshmallow import Marshmallow
ma = Marshmallow()

class ItemSchema(ma.Schema):
    """
    Schema
    """
    class Meta:
        fields = (
        'id', 
        'name',
        'state',
        'in_time',
        'out_time'
        )