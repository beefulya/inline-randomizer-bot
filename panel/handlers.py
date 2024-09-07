import random
from secrets import token_hex
from aiogram import Router
from aiogram.types import Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from aiogram.filters import CommandStart

rtr = Router()

# command -> /start
@rtr.message(CommandStart)
async def start(message: Message) -> None:
  await message.answer(f"<b>хайп</b>")

# рандом шняга короче ))))
@rtr.inline_query()
async def iq(iquery: InlineQuery):
  rand_id = token_hex(12)
  await iquery.answer([
    InlineQueryResultArticle(id=rand_id,
                            title="На сколько процентов у тебя будет сегодня хорошое настроение",
                            description=("нажми на этот блок чтобы узнать!"),
                            input_message_content=InputTextMessageContent(message_text=(f"Моё настроение сегодня на <tg-spoiler>{random.randrange(0, 100)}%</tg-spoiler>")))
], cache_time=1, is_personal=False)