import sys

from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
       self.one  = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING1),
            no_updates=True,
        )
        
async def start(self):
    LOGGER(__name__).info(f"Gettings Assistants Info...")
    if config.STRING1:
        await self.one.start()
        try:
            await self.one.join_chat("kakashi_bots_support")
            await self.one.join_chat("kakashi_bots_updates")
        except:
            pass
        assistants.append(1)
        get_me = await self.one.get_me()
        self.one.username = get_me.username
        self.one.id = get_me.id
        assistantids.append(get_me.id)
        if get_me.last_name:
            self.one.name = (
                get_me.first_name + " " + get_me.last_name
            )
        else:
            self.one.name = get_me.first_name
        LOGGER(__name__).info(
            f"Assistant Started as {self.one.name}"
        )
        try:
            await self.one.send_message(
                config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴏɴᴇ sᴛᴀʀᴛᴇᴅ :**\n\n✨ ɪᴅ : `{self.one.id}`\n❄ ɴᴀᴍᴇ : {self.one.name}\n💫 ᴜsᴇʀɴᴀᴍᴇ : @{self.one.username}"
            )
        except:
            LOGGER(__name__).error(
                f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
            )
            sys.exit()
        
