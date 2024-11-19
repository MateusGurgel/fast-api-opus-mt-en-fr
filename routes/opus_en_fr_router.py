from fastapi import APIRouter
from dtos.opus_en_fr_dto import TranslationRequest, TranslationResponse
from services.opus_en_fr_services import OpusEnFrServices

opus_en_fr_router = APIRouter()


@opus_en_fr_router.post("/")
def translate(question: TranslationRequest) -> TranslationResponse:
    translation = OpusEnFrServices.translate(question.english_text)
    return {"french_translation": translation}