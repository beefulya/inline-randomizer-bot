import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from settings import token_bot
from panel.handlers import rtr

bot = Bot(token=token_bot, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def main():
  dp.include_router(rtr)
  await dp.start_polling(bot ,handle_signals=False)

if __name__ == '__main__':
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print("work is finished!")