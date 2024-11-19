from pydantic import BaseModel

class TranslationRequest(BaseModel):
    english_text: str

class TranslationResponse(BaseModel):
    french_translation: str