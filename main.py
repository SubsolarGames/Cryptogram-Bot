import settings
import random
import math
import discord
from discord.ext import commands
from codebusters.codebuster import *


logger = settings.logging.getLogger("bot")
puzzles = {}
solved = {}


def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.presences = True
    
    bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
    
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        
        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file.name != "__init__.py":
                await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")
    
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("There was an **error** [❗️]\nPlease check **!help** for more info")
            
    
    @bot.command()
    async def help(ctx):
        commands = ["!freq [letter]|displays the `**`frequency`**` of a letter", "!freq all|displays the all `**`frequency`**` of letters", "!word [word]|displays the `**`frequency`**` of a word"]
        puzzle_commands = [ "!new|creates a new `**`puzzle`**`", "!puzzle|displays current `**`puzzle`**`", "!solve [letter] [letter]|changes the `**`cypher letter`**` into the `**`real letter`**`", "!undo [letter]|reverts the `**`cypher letter`**` to a blank"]
        txt = "Hello! 👋🏼\nI'm the cryptogram bot here to help **codebusters** ✅\n\nHere are the **main** commands:`\n"
        
        most = 0
        for o in [commands, puzzle_commands]:
            for i in o:
                l = i.split("|")
                len_of = len(l[0])
                if len_of > most:
                    most = len_of
  
                 
        for i in commands:
            l = i.split("|")
            spacing = (most+8) - len(l[0])
            to_space = lambda x: "".join([" " for k in range(x)])
            
            txt += "`**`" + l[0] + "`**`" + to_space(spacing) + l[1] + '\n'
        
   
                
        txt += "`\nHere are the **puzzle** commands:`\n"
        for i in puzzle_commands:
            l = i.split("|")
            spacing = (most+8) - len(l[0])
            to_space = lambda x: "".join([" " for k in range(x)])
            
            txt += "`**`" + l[0] + "`**`" + to_space(spacing) + l[1] + '\n'
            
        await ctx.send(txt)


    bot.run(settings.DISCORD_API_SECRET, root_logger=True)
    

if __name__ == "__main__":
    run()
