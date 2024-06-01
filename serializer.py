from sqlalchemy.orm import class_mapper
import datetime

def serialize_model_instance(model_instance):
    serialized_data = {}
    mapper = class_mapper(model_instance.__class__)
    for column in mapper.columns:
        value = getattr(model_instance, column.key)
        if isinstance(value, datetime.date):
            serialized_data[column.key] = value.isoformat()
        else:
            serialized_data[column.key] = value
    return serialized_data
