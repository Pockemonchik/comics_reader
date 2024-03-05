
from repositories.users import UsersRepository
from services.user_service import UserService
from db.db_helper import db_helper


def user_service():
    return UserService(UsersRepository(db_helper.get_scoped_session()))

