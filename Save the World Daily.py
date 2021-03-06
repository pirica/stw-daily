import asyncio
import datetime
import json
# noinspection PyUnresolvedReferences
import os
import time
import psutil

import discord
import requests
from discord.ext import commands

client = commands.AutoShardedBot(command_prefix='stw ', shard_count=1, case_insensetive=True)
client.remove_command('help')
uptime_start = datetime.datetime.utcnow()
daily_feedback = ""
r = ''


class endpoints:
    ac = "https://www.epicgames.com/id/logout?redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Fid%2Flogin%3FredirectUrl%3Dhttps%253A%252F%252Fwww.epicgames.com%252Fid%252Fapi%252Fredirect%253FclientId%253Dec684b8c687f479fadea3cb2ad83f5c6%2526responseType%253Dcode"
    token = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"
    reward = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{0}/client/ClaimLoginReward?profileId=campaign"


# noinspection PyUnboundLocalVariable,PyShadowingNames
def getToken(authCode: str):
    h = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ="
    }
    d = {
        "grant_type": "authorization_code",
        "code": authCode
    }
    r = requests.post(endpoints.token, headers=h, data=d)
    # print(r.text)
    r = json.loads(r.text)
    if "access_token" in r:
        access_token = r["access_token"]
        account_id = r["account_id"]
        print(f"access_token: {access_token}\naccount_id: {account_id}\nexpires_at: {r['expires_at']}")
        return access_token, account_id
    else:
        if "errorCode" in r:
            print(r)
            print(f"[ERROR] {r['errorCode']}")
            err = r['errorCode']
            reason = r['errorMessage']
        else:
            print("[ERROR] Unknown error")
        return False, err, reason


def get_bot_uptime():
    now = datetime.datetime.utcnow()
    delta = now - uptime_start
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    fmt = ''
    if days == 1:
        fmt += '{d} day, '
    else:
        if days:
            fmt += '{d} days, '
    if hours == 1:
        fmt += '{h} hour, '
    else:
        if hours:
            fmt += '{h} hours, '
    if minutes == 1:
        fmt += '{m} minute, '
    else:
        if minutes:
            fmt += '{m} minutes, '
    if seconds == 1:
        fmt += '{s} second'
    else:
        fmt += '{s} seconds'
    # if days:
    #    fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
    # else:
    #    fmt = '{h} hours, {m} minutes, and {s} seconds'
    return fmt.format(d=days, h=hours, m=minutes, s=seconds)


@client.event
async def on_ready():
    print('Client open')
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name=f"stw help in {len(client.guilds)} severs"))


# noinspection PyBroadException
@client.command()
async def info(message):
    try:
        osgetlogin = os.getlogin()
    except:
        osgetlogin = 'Not Available'
    embed = discord.Embed(title='Information', description='Statistics:', colour=discord.Colour.red())
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/695117839383920641/759372935676559400/Asset_4.14x.png')
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    embed.add_field(name='Host statistics:', value=f'os.name: {os.name}\nos.cpu_count: {os.cpu_count()}\n'
                                                   f'os.getcwd: {os.getcwd()}\nos.getlogin: {osgetlogin}\n'
                                                   f'CPU usage: {psutil.cpu_percent()}%\nCPU Freq: {int(psutil.cpu_freq().current)}mhz\nRAM Usage:\nTotal: '
                                                   f'{psutil.virtual_memory().total // 1000000}mb\nUsed: '
                                                   f'{psutil.virtual_memory().used // 1000000}mb\nFree: '
                                                   f'{psutil.virtual_memory().free // 1000000}mb\nUtilisation: '
                                                   f'{psutil.virtual_memory().percent}%')
    embed.set_footer(text=f"\nRequested by: {message.author.name} • "
                          f"{time.strftime('%H:%M')} {datetime.date.today().strftime('%d/%m/%Y')}"
                     , icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)


@client.command()
async def temp(message):
    try:
        psutilsensors_temperatures = psutil.sensors_temperatures()
    except:
        psutilsensors_temperatures = 'Not available'
    await message.channel.send(psutilsensors_temperatures)


# noinspection PyShadowingBuiltins
@client.command()
async def help(message):
    embed = discord.Embed(title='Help', description='Commands:', colour=discord.Colour.red())
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/448073494660644884/757803329027047444/Asset_2.24x.1.png')
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    embed.add_field(name='stw daily [AUTH TOKEN]',
                    value="Collect your daily reward without even opening the game\nDefeats the whole point of the "
                          "system but who cares?\n**Requires: Auth Token**\n[You can get an auth token by following this "
                          "link](https://tinyurl.com/epicauthcode)\nThen just simply copy your code from the response "
                          "and append to your command.\n'https://accounts.epicgames.com/fnauth?code=CODE'",
                    inline=False)
    embed.add_field(name='stw instruction', value='More detailed instructions for using the bot', inline=False)
    embed.add_field(name='stw uptime', value='**[DEVELOPER]**\nSends how long the bot has been running for.')
    embed.add_field(name='stw emoji', value='**[DEVELOPER]**\nSends the loading emoji')
    embed.add_field(name='stw ping',
                    value='**[DEVELOPER]**\nSends the websocket latency and actual latency, as well as uptime.')
    embed.add_field(name='stw info', value='**[DEVELOPER]**\nReturns information about the bot')
    embed.set_footer(text=f"\nRequested by: {message.author.name} • "
                          f"{time.strftime('%H:%M')} {datetime.date.today().strftime('%d/%m/%Y')}"
                     , icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)


@client.command()
async def uptime(message):
    """Tells you how long the bot has been up for."""
    await message.send('Uptime: **{}**'.format(get_bot_uptime()))


@client.command()
async def instruction(message):
    embed = discord.Embed(title='How to use "STW Daily"', color=discord.Color.blurple())
    embed.set_footer(text='This bot was made by Dippy is not here', icon_url=message.author.avatar_url)
    embed.add_field(name='Welcome',
                    value='I will collect your daily rewards for you, without the need to launch the game.\n\n'
                          'To get started, [Visit this link](https://tinyurl.com/epicauthcode), and copy **only** the '
                          'authorisation code that it gives you.\n\nFor example,\n```js'
                          '\n{"redirectUrl":"https://accounts.epicgames.com/fnauth?code=a51c1f4d35b14'
                          '57c8e34a1f6026faa35","sid":null}\n```\nwill become\n```\n'
                          'a51c1f4d35b1457c8e34a1f6026faa35\n```\n\nThen, just simply copy paste that into '
                          'your command, like so:\n``stw daily a51c1f4d35b1457c8e34a1f6026faa35``\n:bulb: '
                          'Pro tip: In most browsers, double click on or below the code and it should '
                          'highlight just the code\n\nIf there is any error, please do not hesitate to ask '
                          '<@!349076896266452994> and I will try to resolve the issue.\n\n```cs\n# WARNING\n'
                          '"Your Authorisation code can potentially be used maliciously. '
                          'It is only temporary and will expire after use, however that does not mean you '
                          'shouldn\'t be careful who you give it to."\n```\n```css\n# NOT AFFILIATED'
                          ' WITH EPIC GAMES\n```')
    await message.channel.send(embed=embed)


# noinspection SpellCheckingInspection,PyShadowingNames
@client.command(pass_context=True)
async def ping(message):
    websocket_ping = '{0}'.format(int(client.latency * 100)) + ' ms'
    before = time.monotonic()
    # msg = await message.send("Pong!")
    # await msg.edit(content=f"Pong!  `{int(ping)}ms`")
    # await message.channel.send(f'websocket latency: {client.latency*100}ms')
    # await message.send('websocket: {0}'.format(int(client.latency * 100)) + ' ms')
    embed = discord.Embed(title='Latency', color=discord.Color.blurple())
    embed.set_footer(text=f"\nRequested by: {message.author.name} • "
                          f"{time.strftime('%H:%M')} {datetime.date.today().strftime('%d/%m/%Y')}"
                     , icon_url=message.author.avatar_url)
    embed.add_field(name='Websocket :electric_plug:', value=websocket_ping, inline=True)
    embed.add_field(name='Actual :microphone:',
                    value='<a:loadin:759293511475527760>', inline=True)
    embed.add_field(name='Uptime :alarm_clock:', value=f'{get_bot_uptime()}', inline=True)
    embed2 = discord.Embed(title='Latency', color=discord.Color.blurple())
    embed2.set_footer(text=f"\nRequested by: {message.author.name} • "
                           f"{time.strftime('%H:%M')} {datetime.date.today().strftime('%d/%m/%Y')}"
                      , icon_url=message.author.avatar_url)
    embed2.add_field(name='Websocket :electric_plug:', value=websocket_ping, inline=True)
    msg = await message.channel.send(embed=embed)
    ping = (time.monotonic() - before) * 1000
    embed2.add_field(name='Actual :microphone:',
                     value=f'{int(ping)}ms', inline=True)
    await asyncio.sleep(4)
    embed2.add_field(name='Uptime :alarm_clock:', value=f'{get_bot_uptime()}', inline=True)
    await msg.edit(embed=embed2)


@client.command()
async def emoji(message):
    # await message.channel.send('<a:loading:759292972784418800>')
    # await message.channel.send(f'<a:god:424520269315440650>')
    await message.channel.send('<a:loadin:759293511475527760>')


# noinspection PyUnboundLocalVariable,PyUnusedLocal,PyBroadException
@client.command()
async def daily(message, token=''):
    msg = await message.channel.send(embed=discord.Embed(title='Processing', colour=discord.Color.blurple()))
    global daily_feedback, r
    daily_feedback = ""
    r = ''
    # token = str(message.message.content)[10:]
    if str(message.message.content)[9:] == "":
        await msg.edit(
            embed=discord.Embed(title="Specify Auth Token. [You can get yours here](https://tinyurl.com/epicauthcode)"))
    elif len(token) != 32:
        await msg.edit(embed=discord.Embed(title='Please provide a valid token'))
    else:
        await msg.edit(embed=discord.Embed(title=f"Using Auth token: {token}"))
        gtResult = getToken(token)
        if not gtResult[0]:
            # print(str(gtResult))
            embed = discord.Embed(
                title='We hit a roadblock',
                description='Failed to lock profile.',
                colour=0xf63a32
            )
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/448073494660644884/758129079064068096/Asset_4.14x2.png')
            embed.add_field(name="Reason provided by the server:",
                            value=f"{gtResult[1]}",
                            inline=False)
            embed.add_field(name="Description provided by the server:",
                            value=f"{gtResult[2]}",
                            inline=False)
        else:
            h = {
                "Authorization": f"bearer {gtResult[0]}",
                "Content-Type": "application/json"
            }
            r = requests.post(endpoints.reward.format(gtResult[1]), headers=h, data="{}")
            await msg.edit(embed=discord.Embed(title='Claimed your daily.'))
        try:
            if str(r.text).find('{"errorCode":"') == '-1':
                embed = discord.Embed(
                    title='We hit a roadblock',
                    description='Failed to lock profile.',
                    colour=0xf63a32
                )
                embed.set_thumbnail(
                    url='https://cdn2.iconfinder.com/data/icons/mix-color-5/100/Mix_color_5__info-512.png')
                embed.add_field(name="Reason provided by the server:",
                                value=str(r.text).split('{"errorCode":"', 1)[1].split('","errorMessage":"', 1)[0],
                                inline=False)
                embed.add_field(name="Description provided by the server:",
                                value=str(r.text).split('","errorMessage":"', 1)[1].split('","messageVars"', 1)[0],
                                inline=False)
            else:
                try:
                    # print(str(str(r.text).split("notifications", 1)[1][2:].split('],"profile', 1)[0]))
                    daily_feedback = str(r.text).split("notifications", 1)[1][4:].split('],"profile', 1)[0]
                    day = str(daily_feedback).split('"daysLoggedIn":', 1)[1].split(',"items":[', 1)[0]
                    try:
                        await message.channel.send(f'Debugging info because sometimes it breaks:\n{daily_feedback}')
                        item = str(daily_feedback).split('[{"itemType":"', 1)[1].split('","itemGuid"', 1)[0]
                        amount = str(daily_feedback).split('"quantity":', 1)[1].split("}]}", 1)[0]
                        embed = discord.Embed(title='Success',
                                              colour=0x00c113)
                        embed.set_thumbnail(
                            url='https://cdn.discordapp.com/attachments/448073494660644884/757803334198624336/Asset_2.1.14x2.png')
                        embed.add_field(name=f'On day **{day}**, you received:', value=f"**{amount}** **{item}**",
                                        inline=False)
                        # print(item)
                        # print(amount)
                    except Exception as e:
                        await message.channel.send(f'Debugging info because sometimes it breaks:\n{e}')
                        embed = discord.Embed(title='Hmm',
                                              colour=0xeeaf00)
                        embed.set_thumbnail(
                            url='https://cdn.discordapp.com/attachments/448073494660644884/757803329299415163/Asset_1.14x2.png')
                        embed.add_field(name='It appears that you have **already claimed** todays reward.',
                                        value=f"You are on day **{day}**", inline=False)
                except:
                    embed = discord.Embed(
                        title='We hit a roadblock',
                        description='Failed to lock profile.',
                        colour=0xf63a32
                    )
                    embed.set_thumbnail(
                        url='https://cdn.discordapp.com/attachments/448073494660644884/758129079064068096/Asset_4.14x2.png')
                    embed.add_field(name="Reason provided by the server:", value=f"{gtResult[1]}", inline=False)
                    embed.add_field(name="Description provided by the server:", value=f"{gtResult[1]}", inline=False)
        except:
            pass
        # embed.set_author(name=str(message.message.content)[9:],
        #                 icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/3/31'
        #                          '/Epic_Games_logo.svg/1200px-Epic_Games_logo.svg.png')
        embed.set_footer(text=f"\nRequested by: {message.author.name} • "
                              f"{time.strftime('%H:%M')} {datetime.date.today().strftime('%d/%m/%Y')}"
                         , icon_url=message.author.avatar_url)
        # await message.channel.send(embed=embed)
        await msg.edit(embed=embed)


# noinspection SpellCheckingInspection
client.run('token')
