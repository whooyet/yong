import discord, os
from distutils.sysconfig import PREFIX
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

Client = discord.Client()
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')


@client.command(name='구인')
async def aa(ctx, arg, *arg2):
    voice_channel = ctx.author.voice

    if voice_channel is None:
        await ctx.channel.send("먼저 음성 채널에 들어가주세요.")
    else:
        aa = ctx.author.voice.channel
        #invite = await aa.create_invite(unique=False, max_uses=100)

        parameter = ' '.join(arg2)
        members = ctx.author.voice.channel.members

        embed=discord.Embed(title=f"{arg}", description=f"{ctx.author.mention} 님이 구인중")
        embed.add_field(name="채널명", value=f"{aa.mention}", inline=True)
        embed.add_field(name="맴버", value=f"{len(members)}명", inline=True)
        embed.set_footer(text=f"{parameter}")

        await ctx.message.delete()
        await ctx.send(embed=embed)
        #await embed.add_reaction('👍')

@aa.error
async def aa_error(ctx, error):
    print(error)
    await ctx.send(f"!구인 할말 추가할말")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
