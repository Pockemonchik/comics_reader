from pydantic import BaseModel, ConfigDict

class UserSchemaBase(BaseModel):
    username: str
    steam_token: str


class UserSchemaCreate(UserSchemaBase):
    pass

class UserSchemaUpdate(UserSchemaCreate):
    pass

class UserSchemaUpdatePartial(UserSchemaCreate):
    username: str | None
    steam_token: str | None


class UserSchema(UserSchemaBase):
    model_config = ConfigDict(from_attributes=True)
    id: int