import discord
from discord.ext import commands

class component(discord.ui.View):
  def __init__(self):
    super().__init__()
    
  def add_item(self, txt, color):
    self.add_item(button(txt, color))
  
class button(discord.ui.Button):
  def __init__(self, txt, color=None, custom_id=None, disabled=False):
    super().__init__(lavel=txt, style=color, custom_id=custom_id, disabled=disabled)
    
class interaction(commands.Cog):
  def __init__(self, bot):
    self.bot=bot
    
  @commands.Cog.listener
  async def on_interaction(self, com):
    self.bot.dispatch("button_click", com)
    
def setup(bot):
  bot.add_cog(interaction(bot))
