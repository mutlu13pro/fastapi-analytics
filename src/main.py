from fastapi import FastAPI
from api.events import router as events_router

app = FastAPI()

# /api/router
app.include_router(events_router, prefix="/api/events")
# TODO: REST API
# api/eventss

@app.get("/")
def read_root():
    return {"message": "Hello Worlde"}


@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}
