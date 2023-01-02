#ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ɪɴ ᴀɴʏ ᴇʀʀᴏʀs ᴛʜᴀɴ ᴘʟᴢ ᴄᴏɴᴛᴀᴄᴛ @SIXTH_H0KAGE
#sᴜᴘᴘᴏʀᴛ :- @kakashi_bots_support
#ᴜᴘᴅᴀᴛᴇs :- @kakashi_bots_updates
#ɴᴇᴛᴡᴏʀᴋ :- @Otaku_Binge

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
from VIVI.core.userbot import Userbot
import config
from config import *
from VIVI import LOGGER, app, userbot
from VIVI.core.call import VIV
from VIVI.plugins import ALL_MODULES
from VIVI.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("VIVI").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("VIVI").warning(
            "Spotify Client Id & Secret not added, padh le bc abhi bhi time h ya fir gamd dede @SIXTH_H0KAGE ladki ho tabhi dena mai gay nhi ."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("VIVI.plugins" + all_module)
    LOGGER("VIVI.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await VIV.start()
    try:
        await VIV.stream_call(
            "https://telegra.ph/file/1fb934326ef84ffd7f322.jpg"
        )
    except NoActiveGroupCall:
        LOGGER("VIVI").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await VIV.decorators()
    LOGGER("VIVI").info("Music Bot Started Successfully, ENJOY PEEPS")
    await idle()
    try:
        await userbot.send_message(
            config.LOG_GROUP_ID,
            f"Started",
        )
    except Exception as e:
        print(
            "ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇᴅ ᴀs ᴀᴅᴍɪɴ!"
        )
        LOGGER.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
        return
    try:
        await userbot.join_chat("AbishnoiMF")
        await userbot.join_chat("Abishnoi_bots")
    except:
        pass
    await run()
    


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("VIVI").info("Stopping Music Bot")
