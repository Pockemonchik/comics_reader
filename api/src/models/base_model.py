
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Mapped,mapped_column, DeclarativeBase



class BaseModel(DeclarativeBase):
    __abstract__ = True
    @declared_attr.directive
    def __tablename__(self) -> str:
        return f"{self.__name__.lower()}s"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    