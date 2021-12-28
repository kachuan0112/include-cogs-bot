import os
from itertools import cycle
import discord
from discord.ext import commands , tasks
from config.config import NO_TOKEN_COMMAND

from config import config
from my_cogs.audiocontroller import AudioController
from my_cogs.settings import Settings
from my_cogs.utils import guild_to_audiocontroller, guild_to_settings

initial_extensions = ['my_cogs.commands.music',
                      'my_cogs.commands.general', 'my_cogs.plugins.button','my_cogs.commands.other']
bot = commands.Bot(command_prefix=config.BOT_PREFIX,
                   pm_help=True, case_insensitive=True)

bot.remove_command("help")

if __name__ == '__main__':

    config.ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
    config.COOKIE_PATH = config.ABSOLUTE_PATH + config.COOKIE_PATH

    if config.BOT_TOKEN == "":
        print(config.NO_TOKEN_COMMAND)
        exit

    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(e)


status = cycle(
    ['=help','=play','do you know im a music bot?','wanna get rick rolled?','hello','hola','knee how','こんにちは','konichiwa',':3',':)'])

@bot.event
async def on_ready():
    change_status.start()
    print(config.STARTUP_MESSAGE)

    for guild in bot.guilds:
        await register(guild)
        print("Joined {}".format(guild.name))

    print(config.STARTUP_COMPLETE_MESSAGE)

@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_guild_join(guild):
    print(guild.name)
    await register(guild)


async def register(guild):

    guild_to_settings[guild] = Settings(guild)
    guild_to_audiocontroller[guild] = AudioController(bot, guild)

    sett = guild_to_settings[guild]

    try:
        await guild.me.edit(nick=sett.get('default_nickname'))
    except:
        pass

    if config.GLOBAL_DISABLE_AUTOJOIN_VC == True:
        return

    vc_channels = guild.voice_channels

    if sett.get('vc_timeout') == False:
        if sett.get('start_voice_channel') == None:
            try:
                await guild_to_audiocontroller[guild].register_voice_channel(guild.voice_channels[0])
            except Exception as e:
                print(e)

        else:
            for vc in vc_channels:
                if vc.id == sett.get('start_voice_channel'):
                    try:
                        await guild_to_audiocontroller[guild].register_voice_channel(vc_channels[vc_channels.index(vc)])
                    except Exception as e:
                        print(e)


bot.run(config.BOT_TOKEN, bot=True, reconnect=True)
