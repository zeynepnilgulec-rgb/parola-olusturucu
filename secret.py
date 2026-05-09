import discord
import typing
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix='$',
    intents=intents,
    description='Nothing to see here!'
)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.group(hidden=True)
async def secret(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Shh!', delete_after=5)


def create_overwrites(ctx, *objects):
    overwrites = {
        obj: discord.PermissionOverwrite(view_channel=True)
        for obj in objects
    }

    overwrites[ctx.guild.default_role] = discord.PermissionOverwrite(
        view_channel=False
    )

    overwrites[ctx.guild.me] = discord.PermissionOverwrite(
        view_channel=True
    )

    return overwrites


@secret.command()
@commands.guild_only()
async def text(ctx, name: str, *objects: typing.Union[discord.Role, discord.Member]):

    overwrites = create_overwrites(ctx, *objects)

    await ctx.guild.create_text_channel(
        name=name,
        overwrites=overwrites,
        topic='Top secret text channel.',
        reason='Very secret business.'
    )


@secret.command()
@commands.guild_only()
async def voice(ctx, name: str, *objects: typing.Union[discord.Role, discord.Member]):

    overwrites = create_overwrites(ctx, *objects)

    await ctx.guild.create_voice_channel(
        name=name,
        overwrites=overwrites,
        reason='Very secret business.'
    )


@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}!')


@bot.command()
async def nasilsin(ctx):
    await ctx.send("Iyiyim, sen nasilsin?")


@bot.command()
async def bende_iyiym(ctx):
    await ctx.send("Harika, nasil yardimci olabilirim?")


@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(
        f'{member.name} joined {discord.utils.format_dt(member.joined_at)}'
    )


@bot.command()
async def heh(ctx, count_heh: int = 5):
    await ctx.send("he" * count_heh)



bot.run()
