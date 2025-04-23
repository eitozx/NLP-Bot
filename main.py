import os
import asyncio
import discord
import jishaku # noqa
from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(
            intents=intents,
            help_command=None,
            case_insensitive=True,
            strip_after_prefix=True,
            command_prefix=commands.when_mentioned_or("."),  # noqa
        )

async def main():
    bot = Bot()
    bot.remove_command('help')

    await bot.load_extension(f"extensions.nlp")
    await bot.load_extension("jishaku")
    print(f'Loaded Extensions: {len(bot.extensions)}')
    await bot.start(os.getenv("BOT_TOKEN"))


if __name__ == "__main__":
    asyncio.run(main())