from typing import Any, Dict

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from prometheus_fastapi_instrumentator import Instrumentator

from .endpoints import example, logs


class CustomFastAPI(FastAPI):
    def openapi(self) -> Dict[str, Any]:
        if self.openapi_schema:
            return self.openapi_schema
        openapi_schema = get_openapi(
            title="UI gateway service",
            version="0.0.0",
            description="An intermediary component between Glaciation "
            "Frontend and Metadata Service. The service adapts user "
            "interface queries into a series of SPARQL requests to "
            "MetadataService and telemetry requests from Storage Service. "
            "The service also checking user permissions via oauth server "
            "and filters the KGs that a user is not allowed to access.",
            contact={
                "name": "HIRO-MicroDataCenters",
                "email": "all-hiro@hiro-microdatacenters.nl",
            },
            license_info={
                "name": "MIT",
                "url": "https://github.com/glaciation-heu/ui_gateway/"
                "blob/main/LICENSE",
            },
            routes=self.routes,
        )
        self.openapi_schema = openapi_schema
        return self.openapi_schema


app = CustomFastAPI()


Instrumentator().instrument(app).expose(app)


app.include_router(example.router)
app.include_router(logs.routes.router)
