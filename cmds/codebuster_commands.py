import sys
sys.path.append("../")
from codebusters.codebuster import *
from discord.ext import commands
from main import puzzles

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


@commands.command()
async def new(ctx):
    global puzzles
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        puzzles[username] = quote_to_code(random.choice(quotes)['text'])
        await ctx.send(disp(puzzles[username]))
    else:
        await ctx.send("You are already in a **puzzle**!\nCheck it with **!puzzle**")
        

@commands.command()
async def puzzle(ctx):
    global puzzles
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to create a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        await ctx.send(disp(puzzle))
        
     
async def setup(bot):
    bot.add_command(freq)
    bot.add_command(word)
    bot.add_command(new)
    bot.add_command(puzzle)