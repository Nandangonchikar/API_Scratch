from .database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text

#ThisPost tells how the table should be there. like what xcolumns and all
class Post(Base):
    __tablename__ = 'posts'

    #define columns
    id=Column(Integer, primary_key=True,nullable=False)
    title=Column(String, nullable=False)
    content=Column(String, nullable=False)
    published=Column(Boolean, server_default='TRUE',nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))