import settings
import random
import discord
from discord.ext import commands


logger = settings.logging.getLogger("bot")



def run():
    intents = discord.Intents.default()
    intents.message_content = True 
    
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
        await ctx.send("Hello! 👋🏼\nI'm the cryptogram bot here to help **codebusters** ✅\n\nHere are the **main** commands:\n    **!freq** [letter] displays the **frequency** of a letter\n    **!freq all** displays the all **frequency** of letters\n    **!word** [word] displays the **frequency** of a word")
        


    bot.run(settings.DISCORD_API_SECRET, root_logger=True)
    

if __name__ == "__main__":
    run()
