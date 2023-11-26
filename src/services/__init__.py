from src.services.commands import Commands
from src.services.vk import Connection


vk: Connection = Connection()
api = vk.get_bot_api()
commands: Commands = Commands()
