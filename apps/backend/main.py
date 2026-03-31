from functools import lru_cache

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings, SettingsConfigDict

from apps.backend.schemas import ClassifyRequest, ClassifyResponse, EmailClassifyRequest


class Settings(BaseSettings):
    sentry_dsn: str = ""
    ai_api_key: str = ""
    allowed_origins: str = "http://localhost:4200"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()


def parse_allowed_origins(value: str) -> list[str]:
    origins = [origin.strip() for origin in value.split(",")]
    return [origin for origin in origins if origin]


def classify_text(text: str) -> ClassifyResponse:
    spam_tokens = {"free", "winner", "prize", "offer", "urgent", "click"}
    normalized = text.lower()
    hit_count = sum(token in normalized for token in spam_tokens)

    if hit_count:
        confidence = min(0.55 + 0.1 * hit_count, 0.99)
        return ClassifyResponse(label="spam", confidence=confidence)

    return ClassifyResponse(label="ham", confidence=0.86)


settings = get_settings()
app = FastAPI(title="AI Spam Classifier API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=parse_allowed_origins(settings.allowed_origins),
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
    merged_text = f"{payload.subject} {payload.body}"
    return classify_text(merged_text)
