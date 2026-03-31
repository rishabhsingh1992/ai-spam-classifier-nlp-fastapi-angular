from typing import Literal

from pydantic import BaseModel, Field


class ClassifyRequest(BaseModel):
    text: str = Field(..., min_length=1)


class EmailClassifyRequest(BaseModel):
    subject: str = Field(..., min_length=1)
    body: str = Field(..., min_length=1)


class ClassifyResponse(BaseModel):
    label: Literal["spam", "ham"]
    confidence: float = Field(..., ge=0.0, le=1.0)
