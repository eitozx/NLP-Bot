import discord
import textblob
from discord.ext import commands


def get_sentiment(text : str) -> str:
    # Use TextBlob for sentiment analysis
    blob = textblob.TextBlob(text)
    sentiment = blob.sentiment.polarity  # Value between -1 (negative) to 1 (positive)

    # Return sentiment category
    if sentiment > 0.1:
        return 'positive'
    elif sentiment < -0.1:
        return 'negative'
    else:
        return 'neutral'


class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message : discord.Message):
        if message.author.bot:
            return

        sentiment : str = get_sentiment(message.content)
        emoji_map = {
            "positive": "😊",
            "neutral": "😐",
            "negative": "😞"
        }
        await message.add_reaction(emoji_map[sentiment])

async def setup(bot):
    await bot.add_cog(Cog(bot))