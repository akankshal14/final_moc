from fastapi import FastAPI
from src.router.user_router import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from src.router.slot_router import router as slot_router
from contextlib import asynccontextmanager
from src.database.session import session
from src.utils.seed import seed
from src.utils.logger import logger
from src.router.enrollment_router import router as enrollment_router
from src.router.moc_router import router as moc_router
from src.router.admin_router import router as admin_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = session()
    try:
        seed(db)
        logger.info("Seeding completed")
    except Exception as e:
        logger.error(f"Seeding failed: {str(e)}")
    finally:
        db.close()

    yield



app=FastAPI(lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(slot_router)
app.include_router(enrollment_router)
app.include_router(moc_router)
app.include_router(admin_router)

@app.get("/")
async def root():
    return {"message": "MOC system"}
