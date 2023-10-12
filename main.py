import discord
from discord import app_commands
import os
import logging

from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
from itertools import islice
from math import ceil

from instaloader import Instaloader, Profile

load_dotenv()

MY_GUILD = discord.Object(id=823586247989526568)  # TTM Server ID

# Logging
if not os.path.exists('logs'):
    os.makedirs('logs')
handler = logging.FileHandler(filename='logs/scarecrow-' + datetime.today().strftime('%Y%m%d-%H%M%S') + '.log',
                              encoding='utf-8',
                              mode='w')
profileUsername = 'thetinmen'
L = Instaloader()

profile = Profile.from_username(L.context, profileUsername)


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)


def get_target_channel():
    if os.path.exists('channel.txt'):
        f = open("channel.txt", "r")
        channel = client.get_channel(int(f.read()))
        f.close()
        return channel
    else:
        return None


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')


# @client.tree.command()
# async def setchannel(interaction: discord.Interaction, channel: discord.TextChannel):
#     """Set the channel where post announcements should be made."""
#     f = open("channel.txt", "w")
#     f.write(str(channel.id))
#     f.close()
#     await interaction.response.send_message(f'Announcement channel set to {channel.mention}')
#
#
# @client.tree.command()
# async def getchannel(interaction: discord.Interaction):
#     """Get the current announcement channel."""
#
#     if os.path.exists('channel.txt'):
#         channel = get_target_channel()
#         await interaction.response.send_message(f'Current announcement channel: {channel.mention}.')
#
#     else:
#         await interaction.response.send_message('No announcement channel set.')



@client.tree.command()
async def post(interaction: discord.Interaction, attachment: discord.Attachment, url: str, title: str,
               reel: bool = False, description: str = '', channel: discord.TextChannel = None):
    """Sends a message announcing the last post published."""
    await interaction.response.defer()
    if channel is None:
        channel = get_target_channel()

    if channel:
        print('Creating embed...')
        embed = discord.Embed(title=title, description=description, url=url, color=0xfd4e0e)
        embed.set_author(name="New reel by TheTinMen" if reel else "New post by TheTinMen")
        embed.set_image(url=attachment.url)
        embed.set_footer(text="Scarecrow")
        print('Sending embed...', channel.name)

        try:
            await channel.send(embed=embed)
        except:
            print('An error occured.')
        print('Sending confirmation message...')
        await interaction.followup.send(f'Message sent to {channel.mention}.')

    else:
        await interaction.followup.send(f'No announcement channel set.')


@client.tree.command()
async def ping(interaction: discord.Interaction):

    await interaction.response.defer()
    print(interaction.user.roles)
    await interaction.followup.send(f'Pong! {round(client.latency*1000, 2)}ms')



client.run(os.getenv('TOKEN'), log_handler=handler)
