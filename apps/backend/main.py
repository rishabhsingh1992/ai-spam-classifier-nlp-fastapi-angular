from functools import lru_cache

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings, SettingsConfigDict

from classifier import classify_text
from schemas import ClassifyRequest, ClassifyResponse, EmailClassifyRequest


class Settings(BaseSettings):
    allowed_origins: str = "http://localhost:4200"
    sentry_dsn: str = ""
    ai_api_key: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

app = FastAPI(title="AI Spam Classifier API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.allowed_origins.split(",") if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/classify", response_model=ClassifyResponse)
def classify(payload: ClassifyRequest) -> ClassifyResponse:
    return classify_text(payload.text)


@app.post("/classify/email", response_model=ClassifyResponse)
def classify_email(payload: EmailClassifyRequest) -> ClassifyResponse:
    return classify_text(f"{payload.subject} {payload.body}")
