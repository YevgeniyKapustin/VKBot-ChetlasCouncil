from loguru import logger
from vk_api.bot_longpoll import VkBotEventType

from src import config
from src.services import vk, commands
from src.services.schemas import Message
from src.utils.message import extract_msg_from_event


class Bot(object):
    def __init__(self):
        logger.add('.log')

    @logger.catch()
    def launch(self):
        while True:
            logger.info('launch...')
            if not config.DEBUG:
                try:
                    self.__run()
                except Exception as exception:
                    logger.critical(exception)
            else:
                self.__run()

    @staticmethod
    def __run():
        for event in vk.get_longpoll().listen():
            logger.debug(f'catch {event}')
            if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
                message: Message = extract_msg_from_event(event)
                if (
                        config.PEER_ID == message.peer_id and
                        message.text[0] == config.PREFIX
                ):
                    for command in commands:
                        ...
