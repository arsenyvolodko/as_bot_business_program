from pydantic import BaseModel

from as_bot_business_program.enums import *


class ServiceModel(BaseModel):
    service_name: ServiceNameEnum
    comment: ServiceCommentEnum
    chat_id: int
    state: ServiceStateEnum
