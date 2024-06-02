from typing import List, Optional, Type
from sqlalchemy.orm import Session
from graphs.models.graph import Graph, Node, Edge
from graphs import schemas
from sqlalchemy import func
import heapq


def create_graph(db: Session, graph_data: schemas.GraphCreate):
    graph = Graph(name=graph_data.name)
    db.add(graph)
    db.commit()
    db.refresh(graph)
    return graph


def get_graph(db: Session, graph_id: int):
    return db.query(Graph).filter(Graph.id == graph_id).first()


def get_all_graphs(db: Session) -> list[Type[Graph]]:
    return db.query(Graph).all()


def get_all_nodes_in_graph(db: Session, graph_id: int) -> List[schemas.Node]:
    graph = db.query(Graph).filter(Graph.id == graph_id).first()
    if not graph:
        return []
    return graph.nodes


def get_all_edges_in_graph(db: Session, graph_id: int) -> List[schemas.Edge]:
    graph = db.query(Graph).filter(Graph.id == graph_id).first()
    if not graph:
        return []
    return graph.edges


def create_node(db: Session, graph_id: int, node_data: schemas.NodeCreate):
    node = Node(graph_id=graph_id, coordinates=node_data.coordinates)
    db.add(node)
    db.commit()
    db.refresh(node)
    return node


def create_edge(db: Session, graph_id: int, edge_data: schemas.EdgeCreate):
    edge = Edge(
        graph_id=graph_id,
        from_node_id=edge_data.from_node_id,
        to_node_id=edge_data.to_node_id,
    )
    db.add(edge)
    db.commit()
    db.refresh(edge)
    return edge


def get_all_routes_between_two_points(
    db: Session, graph_id: int, source_node_id: int, target_node_id: int, max_stops: int
) -> Optional[List[schemas.Route]]:
    graph = db.query(Graph).filter(Graph.id == graph_id).first()
    if not graph:
        return None

    queue = [(0, [source_node_id])]
    routes = []
    while queue:
        current_distance, current_path = heapq.heappop(queue)
        current_node_id = current_path[-1]

        if current_node_id == target_node_id:
            routes.append({"path": current_path, "total_distance": current_distance})
            continue

        if len(current_path) > max_stops + 1:
            continue

        neighbors = db.query(Edge).filter(Edge.from_node_id == current_node_id).all()

        for neighbor in neighbors:
            new_path = current_path + [neighbor.to_node_id]
            new_distance = current_distance + calculate_edge_distance(db, neighbor)
            heapq.heappush(queue, (new_distance, new_path))

    return {"routes": routes}



def get_shortest_route_between_two_points(
    db: Session, graph_id: int, source_node_id: int, target_node_id: int
) -> Optional[schemas.Route]:
    graph = db.query(Graph).filter(Graph.id == graph_id).first()
    if not graph:
        return None

    heap = [(0, source_node_id)]
    distances = {node.id: float("inf") for node in graph.nodes}
    distances[source_node_id] = 0
    previous_nodes = {}

    while heap:
        current_distance, current_node_id = heapq.heappop(heap)

        if current_node_id == target_node_id:
            break

        if current_distance > distances[current_node_id]:
            continue

        neighbors = db.query(Edge).filter(Edge.from_node_id == current_node_id).all()

        for neighbor in neighbors:
            distance_to_neighbor = current_distance + calculate_edge_distance(
                db, neighbor
            )
            if distance_to_neighbor < distances[neighbor.to_node_id]:
                distances[neighbor.to_node_id] = distance_to_neighbor
                heapq.heappush(heap, (distance_to_neighbor, neighbor.to_node_id))
                previous_nodes[neighbor.to_node_id] = current_node_id

    shortest_route = []
    current_node = target_node_id
    while current_node in previous_nodes:
        shortest_route.append(current_node)
        current_node = previous_nodes[current_node]
    shortest_route.append(source_node_id)
    shortest_route.reverse()

    return {"path": shortest_route, "total_distance": distances[target_node_id]}


def calculate_edge_distance(db: Session, edge: Edge) -> float:
    from_node = db.query(Node).filter(Node.id == edge.from_node_id).first()
    to_node = db.query(Node).filter(Node.id == edge.to_node_id).first()

    if not from_node or not to_node:
        return 0.0

    return db.scalar(func.ST_Distance(from_node.coordinates, to_node.coordinates)) or 0.0

