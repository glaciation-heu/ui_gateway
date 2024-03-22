from enum import Enum

from classy_fastapi import Routable, get

from app.services.logs import LogsService

from ..models.logs import LogsItem

TAGS: list[str | Enum] = ["Logs"]


class LogsRoutes(Routable):
    def __init__(self, service: LogsService) -> None:
        super().__init__()
        self.__service = service

    @get(
        "/logs/",
        operation_id="get_logs_list",
        summary="Get a list of logs",
        response_model=list[LogsItem],
        tags=TAGS,
    )
    async def read_items(self) -> list[LogsItem]:
        """
        Returns a list of logs with the ability to paginate, search and
        filter.
        """
        return self.__service.get_list()


service = LogsService()
routes = LogsRoutes(service)
