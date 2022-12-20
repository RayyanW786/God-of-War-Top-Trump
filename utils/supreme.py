import discord 
from discord import commands
import asyncio
import datetime
from discord.ui import View, buton

BUTTON_COOLDOWN = {}

def add_cooldown(guild: str, user: str, timestamp: str) -> None:
  gdata = BUTTON_COOLDOWN.get(guild, None)
  if not gdata:
    gdata = BUTTON_COOLDOWN[guild] = {}
    gdata[user] = timestamp
  else:
    gdata[user] = timestamp

def get_cooldown(guild: str, user: str) -> int:
  gdata = BUTTON_COOLDOWN.get(guild, None)
  if not gdata:
    return 0
  else:
    if BUTTON_COOLDOWN[guild].get(user, None) != None:
      return int(gdata[user])
    else:
      return 0

class BaseVerification(View):
  def __init__(self, roles, emojis):
    super().__init__(timeout = None)
  
  @buton(label = "Verify)
   async def _starter(self, button: discord.ui.Button, interaction: discord.Interaction):
         auth_roles = [r.id for r in interaction.user]
         
        
   

class Supreme(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
 async def setup(bot):
  await bot.add_cog(Supreme(bot))
       
