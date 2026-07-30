from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from app.vision.api.router import router as vision_router
from app.api.routes.austin import router as austin_router
from app.api.ws.austin_ws import router as ws_router
from app.core.health import router as health_router
from app.billing.router import router as billing_router
from app.twin.router import router as twin_router
from fastapi.staticfiles import StaticFiles
from app.property.api.router import router as property_router
from fastapi import APIRouter

from app.property.api.graph import router as graph_router

router = APIRouter()

router.include_router(graph_router)

# -------------------------
# CREATE APP FIRST
# -------------------------
app = FastAPI(
    title="Austin V3",
    version="0.1.0",
    description="Austin AI API"
)


# -------------------------
# CUSTOM OPENAPI
# -------------------------
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    schema = get_openapi(
        title="Austin V3",
        version="0.1.0",
        description="Austin AI API",
        routes=app.routes,
    )

    schema["components"]["securitySchemes"] = {
        "ApiKeyAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "x-api-key"
        }
    }

    for path in schema["paths"]:
        for method in schema["paths"][path]:
            schema["paths"][path][method]["security"] = [
                {"ApiKeyAuth": []}
            ]

    app.openapi_schema = schema
    return app.openapi_schema


app.openapi = custom_openapi


# -------------------------
# MIDDLEWARE
# -------------------------


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------
# ROUTERS
# -------------------------
app.include_router(austin_router, prefix="/austin")
app.include_router(ws_router)
app.include_router(health_router)
app.include_router(twin_router)
app.include_router(billing_router)
app.include_router(vision_router)
app.include_router(property_router)
app.mount("/storage",StaticFiles(directory="storage"),name="storage",)

# -------------------------
# STARTUP
# -------------------------
@app.on_event("startup")
async def startup():
    print("INFO: Austin V3 initialized successfully")