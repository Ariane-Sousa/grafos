import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from graphs.views import graph_view as controllers
from graphs import schemas
from shared.dependencies import get_db
from typing import List

router = APIRouter()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


@router.post("/graphs/", response_model=schemas.Graph)
def create_graph(graph: schemas.GraphCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating graph: {graph}")
    return controllers.create_graph(db, graph)


@router.get("/graphs/{graph_id}", response_model=schemas.Graph)
def read_graph(graph_id: int, db: Session = Depends(get_db)):
    logger.info(f"Reading graph with ID: {graph_id}")
    db_graph = controllers.get_graph(db, graph_id)
    if db_graph is None:
        raise HTTPException(status_code=404, detail="Graph not found")
    return db_graph


@router.get("/graphs/", response_model=List[schemas.Graph])
def get_all_graphs(db: Session = Depends(get_db)):
    logger.info("Getting all graphs")
    return controllers.get_all_graphs(db)


@router.get("/graphs/{graph_id}/nodes/", response_model=List[schemas.Node])
def get_all_nodes_in_graph(graph_id: int, db: Session = Depends(get_db)):
    logger.info(f"Getting all nodes in graph with ID: {graph_id}")
    return controllers.get_all_nodes_in_graph(db, graph_id)


@router.get("/graphs/{graph_id}/edges/", response_model=List[schemas.Edge])
def get_all_edges_in_graph(graph_id: int, db: Session = Depends(get_db)):
    logger.info(f"Getting all edges in graph with ID: {graph_id}")
    return controllers.get_all_edges_in_graph(db, graph_id)


@router.post("/graphs/{graph_id}/nodes/", response_model=schemas.Node)
def create_node(graph_id: int, node: schemas.NodeCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating node for graph ID {graph_id}: {node}")
    return controllers.create_node(db, graph_id, node)


@router.post("/graphs/{graph_id}/edges/", response_model=schemas.Edge)
def create_edge(graph_id: int, edge: schemas.EdgeCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating edge for graph ID {graph_id}: {edge}")
    return controllers.create_edge(db, graph_id, edge)


@router.get("/graphs/{graph_id}/routes/", response_model=schemas.Routes)
def get_all_routes_between_two_points(
    graph_id: int,
    source_node_id: int,
    target_node_id: int,
    max_stops: int,
    db: Session = Depends(get_db),
):
    logger.info(
        f"Getting all routes between {source_node_id} and {target_node_id} with a maximum of {max_stops} stops"
    )
    routes = controllers.get_all_routes_between_two_points(
        db, graph_id, source_node_id, target_node_id, max_stops
    )
    if not routes:
        raise HTTPException(status_code=404, detail="Routes not found")
    return routes


@router.get("/graphs/{graph_id}/shortest-route/", response_model=schemas.Route)
def get_shortest_route_between_two_points(
    graph_id: int,
    source_node_id: int,
    target_node_id: int,
    db: Session = Depends(get_db),
):
    logger.info(f"Getting shortest route between {source_node_id} and {target_node_id}")
    route = controllers.get_shortest_route_between_two_points(
        db, graph_id, source_node_id, target_node_id
    )
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")
    return route
