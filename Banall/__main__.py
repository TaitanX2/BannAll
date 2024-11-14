import asyncio
import importlib

from pyrogram import idle
from pyrogram import filters, Client

from Banall import app, LOG, BOT_USERNAME
from Banall.modules import ALL_MODULES


async def anony_boot():
    try:
        await app.start()
    except Exception as ex:
        LOG.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("Banall.modules." + all_module)

    LOG.info(f"@{BOT_USERNAME} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOG.info("Stopping Banall Bot...")
