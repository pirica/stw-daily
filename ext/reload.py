"""
STW Daily Discord bot Copyright 2023 by the STW Daily team.
Please do not skid our hard work.
https://github.com/dippyshere/stw-daily

This file is the cog for the reload command. It is used to reload and load cogs for development.
"""

import discord
import discord.ext.commands as ext
import importlib

import stwutil as stw


class Reload(ext.Cog):
    """
    Reloads a cog.
    """

    def __init__(self, client):
        self.client = client

    async def reload_command(self, ctx, extension):
        """
        The main function for the reload command.

        Args:
            ctx: The context of the command.
            extension: The cog to reload.
        """
        try:
            user_document = await stw.get_user_document(ctx, self.client, ctx.author.id)
            currently_selected_profile_id = user_document["global"]["selected_profile"]
            keycard = user_document["profiles"][str(currently_selected_profile_id)]["settings"]["keycard"]
        except:
            keycard = "keycard"
        try:
            self.client.reload_extension(f"ext.{extension}")
            embed_colour = self.client.colours["auth_white"]
            embed = discord.Embed(title=await stw.add_emoji_title(self.client, "Reload cog", "experimental"),
                                  description=f'\u200b\nReloaded cog: {extension}\n\u200b',
                                  color=embed_colour)
        except Exception as e:
            embed_colour = self.client.colours["error_red"]
            embed = discord.Embed(title=await stw.add_emoji_title(self.client, "Reload cog", "experimental"),
                                  description=f'\u200b\nFailed to reload cog: {extension}\n\u200b',
                                  color=embed_colour)
            embed.add_field(name="Error:", value=f"```{e}```", inline=False)

        embed = await stw.set_thumbnail(self.client, embed, keycard)
        embed = await stw.add_requested_footer(ctx, embed, "en")

        await stw.slash_send_embed(ctx, self.client, embed)

    @ext.command(name='rlcg',
                 aliases=['rl', 'reload', '/rlcg'],
                 extras={'emoji': "experimental", "args": {'ext': 'The cog to reload'}, "dev": True},
                 brief="Reloads STW Daily extensions (cogs)",
                 description="Reload STW Daily extensions (cogs) to apply changes without restarting the bot\n"
                             "⦾ Please note that this command is for development purposes only"
                             " <:TBannersIconsBeakerLrealesrganx4:1028513516589682748>")
    async def rlcg(self, ctx, extension):
        """
        This function is the entry point for the reload command when called traditionally

        Args:
            ctx: The context of the command.
            extension: The cog to reload.
        """
        await self.reload_command(ctx, extension)

    async def load_command(self, ctx, extension):
        """
        The main function for the load command.

        Args:
            ctx: The context of the command.
            extension: The cog to load.
        """
        try:
            user_document = await stw.get_user_document(ctx, self.client, ctx.author.id)
            currently_selected_profile_id = user_document["global"]["selected_profile"]
            keycard = user_document["profiles"][str(currently_selected_profile_id)]["settings"]["keycard"]
        except:
            keycard = "keycard"
        try:
            self.client.load_extension(f"ext.{extension}")
            embed_colour = self.client.colours["auth_white"]
            embed = discord.Embed(title=await stw.add_emoji_title(self.client, "Load cog", "experimental"),
                                  description=f'\u200b\nLoaded cog: {extension}\n\u200b',
                                  color=embed_colour)
        except Exception as e:
            embed_colour = self.client.colours["error_red"]
            embed = discord.Embed(title=await stw.add_emoji_title(self.client, "Load cog", "experimental"),
                                  description=f'\u200b\nFailed to load cog: {extension}\n\u200b',
                                  color=embed_colour)
            embed.add_field(name="Error:", value=f"```{e}```", inline=False)

        embed = await stw.set_thumbnail(self.client, embed, keycard)
        embed = await stw.add_requested_footer(ctx, embed, "en")

        await stw.slash_send_embed(ctx, self.client, embed)

    @ext.command(name='lcg',
                 aliases=['lc', 'load', '/lcg'],
                 extras={'emoji': "experimental", "args": {'ext': 'The cog to load'}, "dev": True},
                 brief="Loads STW Daily extensions (cogs)",
                 description="Load STW Daily extensions (cogs) to apply changes without restarting the bot.\n"
                             "⦾ Please note that this command is for development purposes only"
                             " <:TBannersIconsBeakerLrealesrganx4:1028513516589682748>")
    async def lcg(self, ctx, extension):
        """
        This function is the entry point for the load command when called traditionally

        Args:
            ctx: The context of the command.
            extension: The cog to load.
        """
        await self.load_command(ctx, extension)

    async def nhen(self, ctx):
        """
        The main function for the nhen command.

        Args:
            ctx: The context of the command.

        Returns:
            None
        """
        description = "\u200b\n**Reloaded:**```asciidoc\n"
        try:
            user_document = await stw.get_user_document(ctx, self.client, ctx.author.id)
            currently_selected_profile_id = user_document["global"]["selected_profile"]
            keycard = user_document["profiles"][str(currently_selected_profile_id)]["settings"]["keycard"]
        except:
            keycard = "keycard"
        if len(self.client.watch_module.changed) == 0:
            description = "\u200b\n```No files were marked by STW Watch"

        for changed_item in self.client.watch_module.changed:
            try:
                self.client.reload_extension(changed_item)
                description += f"""== {changed_item}\n// Success\n\n"""
            except Exception as e:
                description += f"""Failed:: {changed_item}\n// {e}\n\n"""

        description += "```\u200b"
        embed_colour = self.client.colours["auth_white"]
        embed = discord.Embed(title=await stw.add_emoji_title(self.client, "STW WATCH", "look_normal"),
                              description=description,
                              color=embed_colour)

        embed = await stw.set_thumbnail(self.client, embed, keycard)
        embed = await stw.add_requested_footer(ctx, embed, "en")

        await stw.slash_send_embed(ctx, self.client, embed)
        self.client.watch_module.changed = set(())

    @ext.command(name='rlstwwatch',
                 aliases=['lsw', 'rsw', 'rlw', 'rls', 'rrlsw', 'rllsw', 'rlssw', 'rlsww', 'lrsw', 'rslw', 'rlws',
                          'elsw', '4lsw', '5lsw', 'tlsw', 'glsw', 'flsw', 'dlsw', 'rksw', 'rosw', 'rpsw', 'rlaw',
                          'rlww', 'rlew', 'rldw', 'rlxw', 'rlzw', 'rlsq', 'rls2', 'rls3', 'rlse', 'rlsd', 'rlss',
                          'rlsa', 'erlsw', 'relsw', '4rlsw', 'r4lsw', '5rlsw', 'r5lsw', 'trlsw', 'rtlsw', 'grlsw',
                          'rglsw', 'frlsw', 'rflsw', 'drlsw', 'rdlsw', 'rklsw', 'rlksw', 'rolsw', 'rlosw', 'rplsw',
                          'rlpsw', 'rlasw', 'rlsaw', 'rlwsw', 'rlesw', 'rlsew', 'rldsw', 'rlsdw', 'rlxsw', 'rlsxw',
                          'rlzsw', 'rlszw', 'rlsqw', 'rlswq', 'rls2w', 'rlsw2', 'rls3w', 'rlsw3', 'rlswe', 'rlswd',
                          'rlsws', 'rlswa', 'rlsw', '/rlsw'],
                 extras={'emoji': "experimental", "args": {}, "dev": True},
                 brief="Reloads extensions marked by STW Watch",
                 description="Reload STW Daily extensions (cogs) to apply changes without restarting the bot. "
                             "RLSW uses STW Watch™️ to automatically determine what files need to be reloaded."
                             "\n⦾ Please note that this command is for development purposes only"
                             " <:TBannersIconsBeakerLrealesrganx4:1028513516589682748>")
    async def rlsw(self, ctx):
        """
        This function is the entry point for the reload command when called traditionally

        Args:
            ctx: The context of the command.
        """
        await self.nhen(ctx)


def setup(client):
    """
    This function is called when the cog is loaded via load_extension

    Args:
        client: The bot client
    """
    client.add_cog(Reload(client))
