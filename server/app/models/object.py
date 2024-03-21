from typing import NewType

from enum import Enum


class ObjectType(Enum):
    GLACIATION_NODE = "GLACIATION_NODE"
    KUBERNETES_NODE = "KUBERNETES_NODE"
    WORKLOAD = "WORKLOAD"
    NETWORK = "NETWORK"
    DATASET = "DATASET"
    TELEMETRY = "TELEMETRY"


ObjectID = NewType("ObjectID", str)
