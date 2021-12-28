import discord
import asyncio
from discord import embeds
from discord import mentions
from discord.ext import commands
import datetime
import time
from datetime import datetime


class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='botstop', aliases=['bstop'])
    @commands.is_owner()
    async def botstop(self, ctx):
        print('好的wor')
        my_embed=(discord.Embed(title="[**Annoucment**]",description=f"\nBot will be stop and maintains in a few Minutes/Hours/Days depents of the issue."
                                                                            f'\nThanks for your understanding.'
                                                                            f"\nBot already stop working don't use commands until next annoucment."
                                                                            ,color=discord.Color.blurple())
        .add_field(name="Sincerely,",value="<@696599329011400775>" , inline=False)
        .set_footer(text="Thank you!",icon_url="https://cdn.discordapp.com/emojis/889708693925531658.png?size=96")
        
        )
        await ctx.send(embed=my_embed)
        await self.bot.logout()
        return

    @commands.command(name="bstart")
    async def bstart(self , ctx):
        embed=(discord.Embed(title="[**Annoucment**]" , description= f"\nHello Guys"
                                                                    f"\nThe Bot Have been Successfull finish for 80% of devoloped."
                                                                    f"\nThe Bot can be use for now. Eventhough some commands still unworkable, but it will be fixed after some days"
                                                                    f"\nPlease notice that there are still some bug in it, so if you found it please ask <@696599329011400775> for a help."
                                                                    f"\nthats all for now, enjoy." , color=discord.Color.blurple())
        .add_field(name="Sincerely,",value="<@696599329011400775>" , inline=False)
        .set_footer(text="Thank you!",icon_url="https://cdn.discordapp.com/emojis/923844782101495818.png?size=96")

        )

        await ctx.send(embed=embed)

    @commands.command(name="help" , description="See what command you can use")
    async def help(self , ctx):
        embed=(discord.Embed(title="**BOT COMMANDS**" , description="**See All Commands in here**" , color=discord.Color.blurple())
        .add_field(name='**Music Commands ! **', value="`play` , `=music (do this commands for more imformation)`",inline=False)
        .add_field(name="**Other fun commands !** " , value="`ping` , `lmao` , `lmfao` , `流感黄豆`" , inline=False)
        .add_field(name="**Other Commands ! **" , value="`help` , `invite` , `reset`" , inline=False)
        .add_field(name="Admin commands(remember give Bot also an Administrator)" , value="`mute` , `unmute` , `warn` ,~~`setprefix`~~ (current not usable) , `setting`", inline=False)
        .set_footer(text="=help will show this commands. ",icon_url="https://cdn.discordapp.com/emojis/800566172600893450.gif?size=96")
        )
        await ctx.send(embed=embed) 

    @commands.command(name="music")
    async def music(self , ctx):
        embed = discord.Embed(title="**Music Commands**" , description="refer this commands below." , color=discord.Color.blurple())
        embed.add_field(name="play <url>/<songs name>" , value="For Join The Voice Call And Play Music." , inline=False)
        embed.add_field(name="loop" , value="For Loop The Music." , inline=False)
        embed.add_field(name="leave/disconnect" , value="For Leave The Channel And Stop Music." , inline=False)
        embed.add_field(name="join/connect" , value="connect to voice chat." , inline=False)
        embed.add_field(name="volume/vol" , value="For Set Bot Volume." , inline=False)
        embed.add_field(name="stop" , value="For Stop All Songs And Clear The List." , inline=False)
        embed.add_field(name="skip/forceskip" , value="For Skip To The Next Songs." , inline=False)
        embed.add_field(name="clear" , value="clear queue" , inline=False)
        embed.add_field(name="history" , value="Check song have played." , inline=False)
        embed.add_field(name="shuffle" , value="For Change Queue Place." , inline=False)
        embed.add_field(name="queue" , value="For check the song in queue." , inline=False)
        embed.add_field(name="prev" , value="For go back one song" , inline=False)
        embed.add_field(name="pause/resume" , value="For Pause and Resume songs." , inline=False)
        embed.add_field(name="songinfo/now" , value="For check songs" , inline=False)
        embed.add_field(name="Error You Will Have" , value=f"\n→If play a songs didn't join and play/no sound/didn't send embed please simply do `=reset`."  f"\n→Bot Will Be Leave In Two Hours If Nothing Have Been Play In That Moment." , inline=False)
        embed.set_footer(text="This Bot Is Program By Python" , icon_url="https://cdn.discordapp.com/emojis/889708830827626578.png?size=96")
        embed.timestamp=datetime.utcnow()
        

        await ctx.send(embed=embed)

    @commands.command(name="lmao")
    async def lmao(self , ctx):
        my_embed=(discord.Embed(title="Lmao" , color=discord.Color.blurple())
    )

        await ctx.send(embed=my_embed)


    @commands.command(name="lmfao")
    async def lmfao(self , ctx):
        my_embed=(discord.Embed(title="Lmfao" , color=discord.Color.blurple())
    )

        await ctx.send(embed=my_embed)

    @commands.command(description="Unmutes a specified user.")
    async def unmute(self , ctx, member: discord.Member=None):
        if not member:
            await ctx.send("You must mention a member to unmute!")

        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mutedRole)
        await member.send(f" you have unmuted from: - {ctx.guild.name}")
        embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.blurple())
        await ctx.send(embed=embed)


    @commands.command()
    async def mute(self , ctx, member: discord.Member=None, time=None, *, reason=None):
        if not member:
            await ctx.send("You must mention a member, time and reason(or no) to mute!")
        elif not time:
            await ctx.send("You must mention a time!")
        else:
            if not reason:
                reason="No reason given"
            try:
                seconds = int(time[:-1]) 
                duration = time[-1] 
                if duration == "s":
                    seconds = seconds * 1
                elif duration == "m":
                    seconds = seconds * 60
                elif duration == "h":
                    seconds = seconds * 60 * 60
                elif duration == "d":
                    seconds = seconds * 86400
                else:
                    await ctx.send("Invalid duration input")
                    return
            except Exception as e:
                print(e)
                await ctx.send("Invalid time input")
                return
            guild = ctx.guild
            mutedRole = discord.utils.get(guild.roles, name="Muted")
            if not mutedRole:
                mutedRole = await guild.create_role(name="Muted")
                for channel in guild.channels:
                    await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
            await member.add_roles(mutedRole, reason=reason)

            muted_embed = discord.Embed(title="Muted", description=f"{member.mention} Was muted" , color=discord.Color.blurple())
            muted_embed.add_field(name="Reason:" , value=reason)
            muted_embed.add_field(name="Duration:" , value=time)
            await ctx.send(embed=muted_embed)
            await member.send(f"You Have Been Muted From: {guild.name} reason: {reason} time: {time}")
            await member.send("https://cdn.discordapp.com/attachments/880086279021297664/915230250978394122/ba29496e40b03d78.jpg")
            await asyncio.sleep(seconds)

            await member.remove_roles(mutedRole)
            
            unmute_embed = discord.Embed(title="Mute Over", description=f"{member.mention} muted is over" , color=discord.Color.blurple())
            await ctx.send(embed=unmute_embed)

    ##################################################

    @commands.command()
    async def warn(self , ctx, member: discord.Member, *, reason=None):
        if not member:
            await ctx.send("You need to mentiona member =warn `@member`.")

            embed = discord.Embed(title="You have been warn" , description=f"{member.mention} was warned " , color=discord.Color.blurple())
            embed.add_field(name="reason:" , value=reason , inline=False)
            await ctx.send(embed=embed)
            await ctx.send("https://cdn.discordapp.com/attachments/880086279021297664/915230250978394122/ba29496e40b03d78.jpg")
            await member.send(f"You have been warn reason: {reason}")
            await member.send("https://cdn.discordapp.com/attachments/880086279021297664/915230250978394122/ba29496e40b03d78.jpg")


    @commands.command(name="流汗黄豆")
    async def 流汗黄豆(self , ctx , member: discord.Member , * , reason=":sweat_smile: :sweat_smile: :sweat_smile: "):
        if not member:
            await ctx.send("你会不会哦 , =流汗黄豆 @人 懂？")
            await ctx.send(":sweat_smile: :sweat_smile: :sweat_smile:")

            embed = discord.Embed(title="You have benn 流汗黄豆警告" , descriptionf=f"{member.mention} was :sweat_smile: " , color=discord.Color.blurple())
            await ctx.send(embed=embed)
            await ctx.send(":sweat_smile: :sweat_smile: :sweat_smile: ")
            await member.send(embed=embed)
            await member.send(":sweat_smile: :sweat_smile: :sweat_smile: ")




def setup(bot):
    bot.add_cog(Other(bot))