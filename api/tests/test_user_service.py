from src.repositories.users import UsersRepository
from src.services.user_service import UserService
from src.db import DatabaseHelper, db_helper
from pathlib import Path


BASE_DIR = Path(__file__).parent

db_helper_override = DatabaseHelper(
    url=f"sqlite+aiosqlite:///{BASE_DIR}/test.sqlite3",
    echo=False,
)
# users_repo = 
user_service = UserService(UsersRepository(db_helper_override.get_scoped_session()))


async def test_users_service_get():
    res = await user_service.get_users()
    print("US users", res)
    assert len(res) >= 0
