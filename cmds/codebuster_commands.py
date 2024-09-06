import sys
sys.path.append("../")
from codebusters.codebuster import *
from discord.ext import commands
import math
from main import puzzles
from main import solved
from main import times
from main import profile
from main import hints
import time


@commands.command()
async def member(ctx):
    global profile
    
    if ctx.message.author.name not in profile:
        profile[ctx.message.author.name] = {
            "comp": [],
            "score": 0
        }

        await ctx.send(f"Welcome **{ctx.author.name}**! Try **!help** for the commands.")
    else:
        await ctx.send(f"You already have an account!\nCheck it with `!prof`")
    
    
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
async def new(ctx, diff: int):
    global puzzles
    global solved
    global profile
    
    username = f"{ctx.message.author.name}"
    
    if username in profile:
        
        if diff not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            await ctx.send("Enter a **difficulty** from 1-10! ❗️")
        else:
            if username not in puzzles:
                hints[username] = 0
                
                if diff != 10:
                    quote_range = get_quotes_of_diff(diff+1, diff+2)
                else:
                    quote_range = get_quotes_of_diff(diff+1, diff+5)
                
                for i in profile[username]['comp']:
                    if i[2] in quote_range:
                        quote_range.remove(i[2])
                
                if quote_range == []:
                    await ctx.send("You have already solved all the puzzles of that **difficulty**")
                else:
                    puzzles[username] = quote_to_code(random.choice(quote_range))
   
                    solved[username] = new_solve(puzzles[username])
                    times[username] = time.time()
                    
                    await ctx.send(disp(puzzles[username], solved[username], time.time() - times[username]))
            else:
                await ctx.send("You are already in a **puzzle**!\nCheck it with **!puzzle**")
    else:
        await ctx.send("Please **setup** an account!\nUse `!member`")


@commands.command()
async def puzzle(ctx):
    global puzzles
    global solved
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to create a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
        
@commands.command()
async def a(ctx, b: str):
    global puzzles
    a = "a"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))

@commands.command()
async def b(ctx, b: str):
    global puzzles
    a = "b"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))

@commands.command()
async def c(ctx, b: str):
    global puzzles
    a = "c"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))

@commands.command()
async def d(ctx, b: str):
    global puzzles
    a = "d"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def e(ctx, b: str):
    global puzzles
    a = "e"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def f(ctx, b: str):
    global puzzles
    a = "f"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def g(ctx, b: str):
    global puzzles
    a = "g"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def h(ctx, b: str):
    global puzzles
    a = "h"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def i(ctx, b: str):
    global puzzles
    a = "i"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def j(ctx, b: str):
    global puzzles
    a = "j"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def k(ctx, b: str):
    global puzzles
    a = "k"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def l(ctx, b: str):
    global puzzles
    a = "l"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def m(ctx, b: str):
    global puzzles
    a = "m"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def n(ctx, b: str):
    global puzzles
    a = "n"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def o(ctx, b: str):
    global puzzles
    a = "o"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def p(ctx, b: str):
    global puzzles
    a = "p"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def q(ctx, b: str):
    global puzzles
    a = "q"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def r(ctx, b: str):
    global puzzles
    a = "r"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def s(ctx, b: str):
    global puzzles
    a = "s"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def t(ctx, b: str):
    global puzzles
    a = "t"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def u(ctx, b: str):
    global puzzles
    a = "u"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def v(ctx, b: str):
    global puzzles
    a = "v"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def w(ctx, b: str):
    global puzzles
    a = "w"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def x(ctx, b: str):
    global puzzles
    a = "x"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def y(ctx, b: str):
    global puzzles
    a = "y"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
@commands.command()
async def z(ctx, b: str):
    global puzzles
    a = "z"
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username][0][a[0].lower()] = b[0].lower()
        solved[username] = update_solve(solved[username], puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))



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
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
        

@commands.command()
async def reset(ctx):
    global puzzles
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
        solved[username] = new_solve(puzzle)
        
        await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
        

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
            hints[username] += 1
            chosen_letter = None
            while chosen_letter == None:
                chosen_letter = random.choice([i for i in ALPHABET])
                if solved[username][0][chosen_letter] == puzzle[1][chosen_letter] or chosen_letter not in puzzle[0]:
                    chosen_letter = None

            solved[username][0][chosen_letter] = puzzle[1][chosen_letter]
            solved[username] = update_solve(solved[username], puzzle)
            
            await ctx.send(disp(puzzle, solved[username], time.time() - times[username]))
        
        
@commands.command()
async def done(ctx):
    global puzzles
    global profile
    global times
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
    
        if check_win(puzzle, solved[username]):
            profile[username]['comp'].append(puzzles[username])
            score_gain  = int((puzzles[username][2]['difficulty'] * 1000) / ((time.time() - times[username]) ** (1/3)) + hints[username])
            profile[username]['score'] += score_gain
            
            puzzles.pop(username)
            await ctx.send(f"You solved the **puzzle**! ✅\n\nIt took you **{round(time.time() - times[username], 2)}** seconds ⏰\nThis earns you **{score_gain}** points 🪙!")
            
        else:
            await ctx.send("That's an **inncorrect** answer ❗️")

@commands.command()
async def prof(ctx, who="NONE"):
    global profile
    
    if who == "NONE":
        who = ctx.message.author.name
        
    if who in profile:
        txt = ""
        txt += f"User: **{who}**\n"
        txt += f"Points: **{profile[who]['score']}** 🪙"
        await ctx.send(txt)
    else:
        await ctx.send(f"**{who}** has not set up an account❗️")


@commands.command()
async def lead(ctx):
    global profile
    
    if profile != {}:
        rankings = {}
        
        
        for i in profile:
            rankings[i] = profile[i]['score']

        rankings = sorted(rankings.items(), key=lambda x: -x[1])
        

        txt = "Leaderboard ⭐️\n"
        for i in range(0, 10):
            if i < len(rankings):
                bonus = ""
                if i == 0:
                    bonus = "🥇"
                elif i == 1:
                    bonus = "🥈"
                elif i == 2:
                    bonus = "🥉"
                    
                txt += f"`[`**`{i+1}`**`] {rankings[i][0]}        `**`{rankings[i][1]}`**` " + bonus + "`\n"
                
        await ctx.send(txt)
    else:
        await ctx.send("No rankings yet")


@commands.command()
async def end(ctx):
    global puzzles
    global profile
    
    username = f"{ctx.message.author.name}"
    
    if username not in puzzles:
        await ctx.send("You need to have a **puzzle** first!\nUse **!new**")
    else:
        puzzle = puzzles[username]
    
        solved[username][0] = puzzle[1]
        solved[username] = update_solve(solved[username], puzzle)

        profile[username]['comp'].append(puzzles[username])        
        puzzles.pop(username)

        
        await ctx.send(f"You ended the puzzle here's the **answer**:\n`{solved[username][1].upper()}`")

            
async def setup(bot):
    bot.add_command(freq)
    bot.add_command(word)
    bot.add_command(new)
    bot.add_command(puzzle)
    bot.add_command(undo)
    bot.add_command(reset)
    bot.add_command(hint)
    bot.add_command(end)
    bot.add_command(done)
    bot.add_command(member)
    bot.add_command(prof)
    bot.add_command(lead)
    
    bot.add_command(a)
    bot.add_command(b)
    bot.add_command(c)
    bot.add_command(d)
    bot.add_command(e)
    bot.add_command(f)
    bot.add_command(g)
    bot.add_command(h)
    bot.add_command(i)
    bot.add_command(j)
    bot.add_command(k)
    bot.add_command(l)
    bot.add_command(m)
    bot.add_command(n)
    bot.add_command(o)
    bot.add_command(p)
    bot.add_command(q)
    bot.add_command(r)
    bot.add_command(s)
    bot.add_command(t)
    bot.add_command(u)
    bot.add_command(v)
    bot.add_command(w)
    bot.add_command(x)
    bot.add_command(y)
    bot.add_command(z)
