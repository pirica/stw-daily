"""
STW Daily Discord bot Copyright 2022 by the STW Daily team.
Please do not skid our hard work.
https://github.com/dippyshere/stw-daily
"""
print("Starting STW Daily")

import orjson
import os
import aiohttp
import discord
import discord.ext.commands as ext
from discord.ext import tasks
from Crypto.Cipher import AES

import stwwatch as watch
import stwutil as stw

# Compatability layer for future versions of python 3.11+
try:
    import tomllib as toml
except ModuleNotFoundError:
    import tomli as toml

client = ext.AutoShardedBot(command_prefix=ext.when_mentioned, case_insensitive=True, intents=discord.Intents.default())


def load_config(config_path):
    """
    Loads the config file

    Args:
        config_path: The path to the config file

    Returns:
        dict: The config file as a dict
    """
    with open(config_path, "rb") as config_file:
        config = toml.load(config_file)
        config_file.close()

    return config


def main():
    """
    Main function
    """
    # Loading config file
    config_path = "config.toml"
    client.config = load_config(config_path)

    # simple way to parse the colours from config into usable colours;
    client.colours = {}
    for name, colour in client.config["colours"].items():
        client.colours[name] = discord.Colour.from_rgb(colour[0], colour[1], colour[2])

    client.temp_auth = {}
    client.remove_command('help')

    # list of extensions for stw daily to load in
    extensions = [
        "reward",
        "help",
        "auth",
        "daily",
        "info",
        "research",
        "serverext",
        "homebase",
        "vbucks",
        "reload",
        "profile.lavendar",  # hehe hiii
        "profile.devauth",
        "profile.sunday",
        "news",
        "battlebreakers.battlebreakers",  # why do you only call me when you're high
        "battlebreakers.bbreward",
        "power",
        "i18n-testing",
        "invite",
        "how2",
        "llamas",
        # "expeditions",
        "status",
        "profile_dumper",
        "daily_xp",
        "battlebreakers.bbdump"
    ]  # why no ext.bongodb :( doot doot doot doot

    for extension in extensions:
        print(client.load_extension(f"ext.{extension}"))

    set_client_modules(client)

    update_status.start()
    client.run(f"{os.environ['STW_DAILY_TOKEN']}")


def set_client_modules(client):
    """
    Sets the client modules

    Args:
        client: The client
    """
    client.watch_module = watch


async def create_http_session():
    """
    Creates an aiohttp session

    Returns:
        aiohttp.ClientSession: The aiohttp session
    """
    # headers={"User-Agent": "Fortnite/++Fortnite+Release-23.10-CL-23443094 Windows/10.0.25267.1.256.64bit"} idk
    return aiohttp.ClientSession(json_serialize=lambda x: orjson.dumps(x).decode())


# basic information for you <33
@client.event
async def on_ready():
    """
    Event for when the bot is ready
    """

    client.stw_session = await create_http_session()
    for command in client.commands:
        if command.name == "auth":
            client.auth_command = command
            break

    client.localisation = stw.reverse_dict_with_list_keys(client.config["valid_locales"])
    exec(bytes.fromhex("636C69656E742E616363657373203D205B62797465732E66726F6D68657828223334373037393436343934353339364435413644364336413631353734363733343934363541364336333644364336443631353735363642343934353532364336333437373837363635353733313643363236453531334422292C2054727565206966206F732E676574656E7628225245504C5F49442229206F72206F732E706174682E697364697228222F686F6D652F72756E6E6572222920656C73652046616C73652C205472756520696620636C69656E742E757365722E696420696E205B3735373737363939363431383731353635312C203735363032363035363732343537383337362C203735373739343134353634303338323530345D20656C73652046616C73652C2054727565206966206F732E676574656E7628225354575F4441494C595F544F4B454E222920656C73652046616C73652C2022225D"))
    exec(bytes.fromhex("636C69656E742E6163636573735B345D203D2066227B696E7428636C69656E742E6163636573735B315D29202B20337D7B696E7428636C69656E742E6163636573735B325D29202B20327D7B696E7428636C69656E742E6163636573735B335D29202B20317D22"))
    exec(bytes.fromhex("636C69656E742E6163636573735B305D203D2062797465732E66726F6D686578282233343730373934363439343533393644354136443643364136313537343637333439343635413643363336443643364436313537353636423439343535323643363334373738373636353537333136433632364535313344222920696620636C69656E742E6163636573735B325D20656C7365202862797465732E66726F6D686578282233343730333234443439343634453732363135373531363733383441324236423646353133443344222920696620636C69656E742E6163636573735B315D20656C7365202862797465732E66726F6D6865782822333437303332344434393436344537323631353735313637333834413242364236463531334433442229206966206E6F7420636C69656E742E6163636573735B335D20656C73652062797465732E66726F6D68657828223334373037393436343934353339364435413644364336413631353734363733343934363541364336333644364336443631353735363642343934353532364336333437373837363635353733313643363236453531334422292929"))
    client.command_name_dict, client.command_dict, client.command_name_list = stw.create_command_dict(client)
    print("Started STW Daily")

    try:
        await client.watch_module.watch_stw_extensions()
    except RuntimeError:
        pass


@client.event
async def on_message(message):
    """
    Event for when a message is sent.
    This works without message.content, and is currently used to: handle quote marks, auth by default

    Args:
        message: The message that was sent

    Returns:
        None
    """
    if '"' in message.content:
        message = stw.process_quotes_in_message(message)

    # pro watch me i am the real github copilot
    # make epic auth system thing
    try:
        if len(stw.extract_auth_code(message.content.split(" ")[1])) == 32:
            await client.auth_command.__call__(message, stw.extract_auth_code(message.content))
            return
    except IndexError:
        pass

    await client.process_commands(message)


# simple task which updates the status every 60 seconds to display time until next day/reset
@tasks.loop(seconds=60)
async def update_status():
    """
    Task to update the status of the bot
    """
    await client.wait_until_ready()
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening,
                                  name=f"@{client.user.name}  |  Reset in: \n{stw.time_until_end_of_day()}\n  |  In {len(client.guilds)} guilds"))


if __name__ == "__main__":
    main()
