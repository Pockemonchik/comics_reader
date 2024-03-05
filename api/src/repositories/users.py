from models import UserModel
from repositories.base import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model = UserModel
