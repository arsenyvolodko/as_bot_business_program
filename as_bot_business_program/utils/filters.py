from aiogram import types

from as_bot_business_program.utils.services import SERVICE_MODELS


async def text_in_service_models(message: types.Message) -> bool:
    return message.text in SERVICE_MODELS
