from vk_api.bot_longpoll import VkBotMessageEvent

from src.services.schemas import Message


def extract_msg_from_event(event: VkBotMessageEvent) -> Message:
    """Возвращает объект Message создавая его из VkBotMessageEvent.

    Аргументы:
    event -- VkBotMessageEvent

    """
    message = Message.model_validate(event.object.message)
    message.text = message.text.lower()
    return message[1:]
