from typing import List
from pydantic import BaseModel, validator
from geoalchemy2.elements import WKBElement
from geoalchemy2.shape import to_shape


class GraphBase(BaseModel):
    name: str


class GraphCreate(GraphBase):
    pass


class Graph(GraphBase):
    id: int

    class Config:
        orm_mode = True


class NodeBase(BaseModel):
    coordinates: str

    @validator("coordinates", pre=True)
    def parse_coordinates(cls, v):
        if isinstance(v, WKBElement):
            return to_shape(v).wkt
        return v


class NodeCreate(NodeBase):
    pass


class Node(NodeBase):
    id: int
    graph_id: int

    class Config:
        orm_mode = True


class EdgeBase(BaseModel):
    from_node_id: int
    to_node_id: int


class EdgeCreate(EdgeBase):
    pass


class Edge(EdgeBase):
    id: int
    graph_id: int

    class Config:
        orm_mode = True


class Route(BaseModel):
    path: List[int]
    total_distance: float


class Routes(BaseModel):
    routes: List[Route]
