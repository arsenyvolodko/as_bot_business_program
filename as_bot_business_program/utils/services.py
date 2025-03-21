from as_bot_business_program.models import ServiceModel
from as_bot_business_program.enums import *

_NAMES = list(ServiceNameEnum.__members__.values())
_COMMENTS = list(ServiceCommentEnum.__members__.values())
_CHATS = list(ServiceChatIdEnum.__members__.values())
_STATES = list(ServiceStateEnum.__members__.values())

SERVICE_MODELS = {}

for ind, name_enum in enumerate(_NAMES):
    model = ServiceModel(
        service_name=name_enum,
        comment=_COMMENTS[ind],
        chat_id=_CHATS[ind],
        state=_STATES[ind],
    )
    SERVICE_MODELS[name_enum.value] = model
