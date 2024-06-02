import uvicorn
from fastapi import FastAPI
from shared.database import engine, Base
from graphs.models.graph import Node, Graph, Edge
from graphs.controller import graph_controller

Base.metadata.create_all(bind=engine, checkfirst=True)

app = FastAPI()

app.include_router(graph_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)