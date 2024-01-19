import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command(name='ban', pass_context=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(
        title='User Banned',
        description=f'{member.mention} has been banned by {ctx.author.mention}',
        color=discord.Color.red()
    )
    embed.add_field(name='Reason', value=reason, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='kick', pass_context=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(
        title='User Kicked',
        description=f'{member.mention} has been kicked by {ctx.author.mention}',
        color=discord.Color.orange()
    )
    embed.add_field(name='Reason', value=reason, inline=False)
    await ctx.send(embed=embed)


bot.run('YOUR_BOT_TOKEN')
