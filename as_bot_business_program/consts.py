from as_bot_business_program.utils.services import SERVICE_MODELS

START_TEXT = ("Этот бот позволяет при необходимости направить обращение в соответсвующий отдел поддержки.\n\n"
              "Для просмотра доступных отделов и их описания используйте команду /help.\n\n"
              "Чтобы направить обращение, выберите необходимый отдел среди клавиш на клавиатуре и следуйте инструкциям.")

CANCEL_CALLBACK = "CANCEL_CALLBACK"
STATUS_INFO = "Статус обращения: {}."

HELP_TEXT = ""
for key in SERVICE_MODELS:
    HELP_TEXT += f"<b>{key}</b>: {SERVICE_MODELS[key].comment.value}.\n\n"
HELP_TEXT += f"В случае технических неисправностей с ботом обращаться к @arseny_volodko"
