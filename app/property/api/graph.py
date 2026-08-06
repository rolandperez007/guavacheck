from fastapi import APIRouter

from app.property.engines.graph_engine import PropertyGraphEngine

router = APIRouter(
    prefix="/properties",
    tags=["Property Graph"],
)

engine = PropertyGraphEngine()


@router.get("/{property_id}/graph")
def get_property_graph(property_id: str):

    return engine.build(property_id)
