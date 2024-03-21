import uuid
from datetime import datetime

from pydantic import BaseModel

from app.models.logs import Level
from app.models.object import ObjectID, ObjectType


class LogsItem(BaseModel):
    id: uuid.UUID
    created: datetime
    level: Level
    text: str
    objectType: ObjectType
    objectID: ObjectID


class LogsItemInList(LogsItem):
    ...
