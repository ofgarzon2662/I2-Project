from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_base
import uuid
import os
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

db = SQLAlchemy()

class Model():
    id = Column(UUID(as_uuid=True) if os.environ.get('DB_SQLITE', None) is None else String,
                primary_key=True,
                default=uuid.uuid4 if os.environ.get('DB_SQLITE', None) is None else lambda: uuid.uuid4().hex)

    createdAt = Column(DateTime, default=datetime.now())
    expireAt = Column(DateTime)

    def __init__(self, expireAt):
        self.expireAt = expireAt