
import sys
sys.path.append("../")
from codebusters.codebuster import *
from discord.ext import commands


@commands.command()
async def freq(ctx, letter):
    if letter == 'all':
        text = ""
        for i in LETTER_FREQ:
            text += f"**{i}** - **{round(LETTER_FREQ[i.upper()]*100, 3)}%**\n"
        await ctx.send(text)
    else:
        await ctx.send(f"The frequency of **{letter[0]}** is **{round(LETTER_FREQ[letter[0].upper()], 3)*100}%**")


@commands.command()
async def word(ctx, word):
    await ctx.send(f"The frequency of **{word}** is **{word_frequency(word, 'en')*100}%**")


async def setup(bot):
    bot.add_command(freq)
    bot.add_command(word)