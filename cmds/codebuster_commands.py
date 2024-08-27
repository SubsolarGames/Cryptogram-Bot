import sys
sys.path.append("../")
from codebusters.codebuster import *
from discord.ext import commands
from main import puzzles
from main import solved


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
    global solved
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        puzzles[username] = quote_to_code(random.choice(quotes)['text'])
        solved[username] = new_solve(puzzles[username])
        await ctx.send(disp(puzzles[username], solved[username]))
    else:
        await ctx.send("You are already in a **puzzle**!\nCheck it with **!puzzle**")
        

@commands.command()
async def puzzle(ctx):
    global puzzles
    global solved
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to create a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        await ctx.send(disp(puzzle, solved[username]))
        

@commands.command()
async def solve(ctx, a: str, b: str):
    global puzzles
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username]))
        

@commands.command()
async def undo(ctx, letter: str):
    global puzzles
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][letter[0].lower()] = "_"
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username]))
        

@commands.command()
async def reset(ctx):
    global puzzles
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username] = new_solve(puzzle)
        
        await ctx.send(disp(puzzle, solved[username]))
        

@commands.command()
async def hint(ctx):
    global puzzles
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]

        if check_win(puzzle, solved[username]):
            await ctx.send("There are no more hints")
        else:
            chosen_letter = None
            while chosen_letter == None:
                chosen_letter = random.choice([i for i in ALPHABET])
                if solved[username][0][chosen_letter] == puzzle[1][chosen_letter] or chosen_letter not in puzzle[0]:
                    chosen_letter = None

            solved[username][0][chosen_letter] = puzzle[1][chosen_letter]
            solved[username] = update_solve(solved[username], puzzle)
            
            await ctx.send(disp(puzzle, solved[username]))
        
        
@commands.command()
async def done(ctx):
    global puzzles
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
    
        if check_win(puzzle, solved[username]):
            puzzles.pop(username)
            await ctx.send("You solved the **puzzle**! ✅")
        else:
            await ctx.send("That's an **inncorrect** answer ❗️")


@commands.command()
async def end(ctx):
    global puzzles
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
    
        solved[username][0] = puzzle[1]
        solved[username] = update_solve(solved[username], puzzle)
        
        puzzles.pop(username)
        
        await ctx.send(f"You ended the puzzle here's the **answer**:\n`{solved[username][1].upper()}`")

            
async def setup(bot):
    bot.add_command(freq)
    bot.add_command(word)
    bot.add_command(new)
    bot.add_command(puzzle)
    bot.add_command(solve)
    bot.add_command(undo)
    bot.add_command(reset)
    bot.add_command(hint)
    bot.add_command(end)
    bot.add_command(done)