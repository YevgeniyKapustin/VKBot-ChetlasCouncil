from src import config
from src.services import vk


class Poll(object):
    __slots__ = ('__question',)

    def __init__(self, question: str):
        self.__question: str = question

    def create(self):
        poll = vk.get_admin_api().polls.create(
            question=self.__question,
            add_answers='["✔️ Да", "❌ Нет"]',
            is_anonymous=1,
            end_date=1701082800,
            owner_id=-config.CHAT_ID,
            message='Новый опрос!'
        )
        vk.get_bot_api().messages.send(
            chat_id=config.CHAT_ID,
            attachment=f'poll{poll["owner_id"]}_{poll["id"]}',
            random_id=0
        )
