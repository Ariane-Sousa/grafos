from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_create_graph():
    new_graph = {"name": "Test Graph"}
    response = client.post("/graphs/", json=new_graph)
    assert response.status_code == 200
    assert response.json()["name"] == new_graph["name"]


def test_read_graph():
    response = client.get("/graphs/1")
    assert response.status_code == 200


def test_create_node():
    new_node = {"id": 1, "coordinates": "POINT(-74.935242 41.730610)"}
    response = client.post("/graphs/1/nodes/", json=new_node)
    assert response.status_code == 200

    new_node = {"id": 2, "coordinates": "POINT(-70.935242 35.730610)"}
    response = client.post("/graphs/1/nodes/", json=new_node)
    assert response.status_code == 200


def test_create_edge():
    new_edge = {"from_node_id": 1, "to_node_id": 1}
    response = client.post("/graphs/1/edges/", json=new_edge)
    assert response.status_code == 200

