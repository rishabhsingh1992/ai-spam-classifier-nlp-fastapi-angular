from functools import lru_cache

import spacy

from schemas import ClassifyResponse

SPAM_TOKENS = {"free", "winner", "prize", "offer", "urgent", "click"}


@lru_cache
def load_nlp() -> spacy.language.Language:
    return spacy.load("en_core_web_sm")


def classify_text(text: str) -> ClassifyResponse:
    doc = load_nlp()(text)
    lemmas = {token.lemma_.lower() for token in doc if token.is_alpha}
    hit_count = len(SPAM_TOKENS & lemmas)

    if hit_count:
        confidence = min(0.55 + 0.1 * hit_count, 0.99)
        return ClassifyResponse(label="spam", confidence=confidence)

    return ClassifyResponse(label="ham", confidence=0.86)
