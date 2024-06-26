from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.users.routes import router as users_router
from starlette.responses import RedirectResponse

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")



app.include_router(users_router)
