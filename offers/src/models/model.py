from datetime import datetime
import uuid
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, DateTime
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()

class Model:
    id = db.Column(UUID(as_uuid=True) if os.environ.get('DB_SQLITE', None) is None else String,
                primary_key=True,
                default=uuid.uuid4 if os.environ.get('DB_SQLITE', None) is None else lambda: uuid.uuid4().hex)
    createdAt = db.Column(DateTime, default=datetime.now())