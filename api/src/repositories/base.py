from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_helper import db_helper


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError

    @abstractmethod
    async def update_one():
        raise NotImplementedError

    @abstractmethod
    async def delete_one():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        
        stmt = insert(self.model).values(**data).returning(self.model.id)
        obj = await self.session.execute(stmt)
        await self.session.commit()
        await self.session.close()
        return obj.scalar_one()

    async def find_one(self, id: int):
        
        obj = await self.session.get(self.model, id)
        if obj is None:
            await self.session.close()
            return None
        await self.session.close()
        return obj.to_read_model()

    async def find_all(self):
        
        stmt = select(self.model)
        obj = await self.session.execute(stmt)
        await self.session.close()
        obj = [row[0].to_read_model() for row in obj.all()]
        return obj

    async def update_one(self, id: int, data: dict):
        
        obj = await self.session.get(self.model, id)
        if obj is None:
            await self.session.close()
            return None
        for name, value in data.items():
            setattr(obj, name, value)
        await self.session.commit()
        
        return obj.id

    async def delete_one(self, id: int):
        
        obj = await self.session.get(self.model, id)
        if obj is None:
            await self.session.close()
            return None
        await self.session.delete(obj)
        await self.session.commit()
        await self.session.close()
        return id
