from typing import Any

from app.models.logs import Level
from app.models.object import ObjectType


class LogsService:
    def get_list(self) -> list[dict[str, Any]]:
        return [
            {
                "id": "ac740dbd-441e-4ecf-b0fc-95963b5a8551",
                "created": "2024-03-08T04:00:00.000Z",
                "level": Level.INFO,
                "text": "Node is starting...",
                "objectType": ObjectType.KUBERNETES_NODE,
                "objectID": "94bc5906-b08e-4952-86ee-0f0bbad79000",
            },
            {
                "id": "27f43277-a952-4813-90fa-f761fc9247d5",
                "created": "2024-03-08T04:01:00.000Z",
                "level": Level.ERROR,
                "text": "Unknown error",
                "objectType": ObjectType.KUBERNETES_NODE,
                "objectID": "94bc5906-b08e-4952-86ee-0f0bbad79000",
            },
        ]
