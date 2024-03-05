from .base_model import BaseModel
from sqlalchemy.orm import Mapped 
from schemas.user_schema import UserSchema


class UserModel(BaseModel):
    username: Mapped[str]
    steam_token: Mapped[str]
    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            username=self.username,
            steam_token=self.steam_token,
        )