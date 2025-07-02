from fastapi import FastAPI

from src.database.postgres import init_db
from src.utils.logUtil import log, console_logging_config

from src.routes import router as api_router

app = FastAPI(title="Template Api FastApi")


def init_application():
    console_logging_config()
    init_db()
    log.info("Starting application!")


@app.on_event("startup")
async def init_app():
    init_application()


@app.get("/")
def get_health_check():
    return {"Welcome to Template API FastApi"}


@app.get("/health")
def get_health_check():
    return {"OK"}


app.include_router(api_router)
