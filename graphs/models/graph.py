from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from shared.database import Base


class Graph(Base):
    __tablename__ = "graph"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Node(Base):
    __tablename__ = "node"
    id = Column(Integer, primary_key=True, index=True)
    graph_id = Column(Integer, ForeignKey("graph.id"))
    coordinates = Column(Geometry(geometry_type="POINT", srid=4326))
    graph = relationship("Graph", back_populates="nodes")


class Edge(Base):
    __tablename__ = "edge"
    id = Column(Integer, primary_key=True, index=True)
    graph_id = Column(Integer, ForeignKey("graph.id"))
    from_node_id = Column(Integer, ForeignKey("node.id"))
    to_node_id = Column(Integer, ForeignKey("node.id"))
    graph = relationship("Graph", back_populates="edges")
    from_node = relationship("Node", foreign_keys=[from_node_id])
    to_node = relationship("Node", foreign_keys=[to_node_id])


Graph.nodes = relationship("Node", order_by=Node.id, back_populates="graph")
Graph.edges = relationship("Edge", order_by=Edge.id, back_populates="graph")
