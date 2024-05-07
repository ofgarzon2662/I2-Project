import os
import uuid
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Column, String
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()


class Model:
    id = Column(UUID(as_uuid=True) if os.environ.get('DB_SQLITE', None) is None else String,
                primary_key=True,
                default=uuid.uuid4 if os.environ.get('DB_SQLITE', None) is None else lambda: uuid.uuid4().hex)
    createdAt = Column(DateTime, default=datetime.now())
    updatedAt = Column(DateTime, default=datetime.now())