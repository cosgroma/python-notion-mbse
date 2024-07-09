from bson import ObjectId


class PydanticObjectId(ObjectId):
    @classmethod
    def validate(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        if isinstance(v, str) and ObjectId.is_valid(v):
            return str(ObjectId(v))
        raise ValueError("Invalid ObjectId")

    @classmethod
    def __get_pydantic_json_schema__(cls, model_config, handler):
        return {"type": "string", "format": "ObjectId"}
