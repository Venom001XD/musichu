import sys

from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
       userbot  = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING5),
            no_updates=True,
        )

async def start(self):
    LOGGER(__name__).info(f"Gettings Assistants Info...")
    if config.STRING1:
        await userbot.start()
        try:
            await userbot.join_chat("kakashi_bots_support")
            await userbot.join_chat("kakashi_bots_updates")
        except:
            pass
        assistants.append(1)
        get_me = await userbot.get_me()
        userbot.username = get_me.username
        userbot.id = get_me.id
        assistantids.append(get_me.id)
        if get_me.last_name:
            userbot.name = (
                get_me.first_name + " " + get_me.last_name
            )
        else:
            userbot.name = get_me.first_name
        LOGGER(__name__).info(
            f"Assistant Started as {self.one.name}"
        )
        try:
            await userbot.send_message(
                config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴏɴᴇ sᴛᴀʀᴛᴇᴅ :**\n\n✨ ɪᴅ : `{userbot.id}`\n❄ ɴᴀᴍᴇ : {userbot.name}\n💫 ᴜsᴇʀɴᴀᴍᴇ : @{userbot.username}"
            )
        except:
            LOGGER(__name__).error(
                f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
            )
            sys.exit()
userbot.start()        
