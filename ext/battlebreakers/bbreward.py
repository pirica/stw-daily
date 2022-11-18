import discord
import discord.ext.commands as ext
from discord import Option
from discord.commands import (  # Importing the decorator that makes slash commands.
    slash_command,
)

import stwutil as stw


# cog for the reward command.
class BBReward(ext.Cog):

    def __init__(self, client):
        self.client = client

    async def bbreward_command(self, ctx, day, limit=7, slash=False):

        try:
            temp_auth = self.client.temp_auth[ctx.author.id]
            if day == 'hi readers of the bot':
                daye = temp_auth["bb_day"]
                if daye is not None:
                    day = daye
        except:
            pass

        embed_colour = self.client.colours["reward_magenta"]
        err_colour = self.client.colours["error_red"]
        if day == 'hi readers of the bot':

            embed = discord.Embed(colour=err_colour,
                                  title=await stw.add_emoji_title(self.client, "Missing Day", "error"),
                                  description="```Please specify the day (number) of which you would like to see```")
            embed = await stw.add_requested_footer(ctx, embed)
            embed = await stw.set_thumbnail(self.client, embed, "error")
            await stw.slash_send_embed(ctx, slash, embed)

        else:
            try:
                day = int(day)
                limit = int(limit)

                if limit < 1:
                    limit = 7

            except:
                embed = discord.Embed(colour=err_colour,
                                      title=await stw.add_emoji_title(self.client, "Non Numeric Day or Limit", "error"),
                                      description="```The inputted day or limit must be a valid integer, please try again```")
                embed = await stw.add_requested_footer(ctx, embed)
                embed = await stw.set_thumbnail(self.client, embed, "error")
                await stw.slash_send_embed(ctx, slash, embed)
                return

            if int(limit) > 100:
                embed = discord.Embed(colour=err_colour,
                                      title=await stw.add_emoji_title(self.client, "Too Long", "error"),
                                      description="```You attempted to retrieve too many days after! Try a lower value```")
                embed = await stw.add_requested_footer(ctx, embed)
                embed = await stw.set_thumbnail(self.client, embed, "error")
                await stw.slash_send_embed(ctx, slash, embed)
                return

            embed = discord.Embed(title=await stw.add_emoji_title(self.client, "Reward", "Shared2"),
                                  description=f'\u200b\nDisplaying rewards for day **{day}** and **{limit}** days after\n\u200b',
                                  color=embed_colour)

            try:
                # day, name, emoji_text, description, quantity
                reward = stw.get_bb_reward_data(self.client, pre_calc_day=day)
            except:
                embed = discord.Embed(colour=err_colour,
                                      title=await stw.add_emoji_title(self.client, "Invalid Day", "error"),
                                      description="```Please retry with a valid integer.```")
                embed = await stw.add_requested_footer(ctx, embed)
                embed = await stw.set_thumbnail(self.client, embed, "error")
                await stw.slash_send_embed(ctx, slash, embed)
                return

            embed.add_field(name=f'**{reward[2]} Item: **', value=f'```{reward[4]} {reward[1]}```\u200b')
            for row in stw.LoginRewards[0]['Rows']:
                if 'MtxGiveaway' in stw.LoginRewards[0]['Rows'][row]['ItemDefinition']['AssetPathName']:
                    if int(day) % 1800 < int(row):
                        if int(row) - int(day) % 1800 == 1:
                            day_string = "day."
                        else:
                            day_string = "days."
                        embed.add_field(
                            name=f'**{self.client.config["emojis"]["T_MTX_Gem_Icon"]} Next Gem reward in: **',
                            value=f'```{int(row) - int(day) % 1800} {day_string}```\u200b', inline=False)
                        break

            rewards = ''
            for i in range(1, limit + 1):
                data = stw.get_bb_reward_data(self.client, pre_calc_day=day + i)
                rewards += str(data[4]) + " " + str(data[1])
                if not (i + 1 == limit + 1):
                    rewards += ', '
                else:
                    rewards += '.'
            if limit == 1:
                reward = stw.get_bb_reward_data(self.client, pre_calc_day=day + 1)

                embed.add_field(name=f'**{reward[2]} Tomorrow\'s reward:**',
                                value=f'```{reward[4]} {reward[1]}```\u200b',
                                inline=False)
            else:
                embed.add_field(
                    name=f'{self.client.config["emojis"]["calendar"]} Rewards for the next **{limit}** days:',
                    value=f'```{rewards}```\u200b', inline=False)

            embed = await stw.set_thumbnail(self.client, embed, "Shared2")
            embed = await stw.add_requested_footer(ctx, embed)

            try:
                await stw.slash_send_embed(ctx, slash, embed)
            except discord.errors.HTTPException:
                embed = discord.Embed(colour=err_colour,
                                      title=await stw.add_emoji_title(self.client, "Too Long", "error"),
                                      description="```You attempted to retrieve too many days after! Try a lower value```")
                embed = await stw.add_requested_footer(ctx, embed)
                embed = await stw.set_thumbnail(self.client, embed, "error")
                await stw.slash_send_embed(ctx, slash, embed)

    @ext.command(name='bbreward',
                 aliases=['bbr', 'bbrwrd', 'battlebreakersreward', 'breward', 'bbeward', 'bbrward', 'bbreard',
                          'bbrewrd', 'bbrewad', 'bbrewar', 'bbbreward', 'bbrreward', 'bbreeward', 'bbrewward',
                          'bbrewaard', 'bbrewarrd', 'bbrewardd', 'brbeward', 'bberward', 'bbrweard', 'bbreawrd',
                          'bbrewrad', 'bbrewadr', 'vbreward', 'gbreward', 'hbreward', 'nbreward', 'bvreward',
                          'bgreward', 'bhreward', 'bnreward', 'bbeeward', 'bb4eward', 'bb5eward', 'bbteward',
                          'bbgeward', 'bbfeward', 'bbdeward', 'bbrwward', 'bbr3ward', 'bbr4ward', 'bbrrward',
                          'bbrfward', 'bbrdward', 'bbrsward', 'bbreqard', 'bbre2ard', 'bbre3ard', 'bbreeard',
                          'bbredard', 'bbresard', 'bbreaard', 'bbrewqrd', 'bbrewwrd', 'bbrewsrd', 'bbrewxrd',
                          'bbrewzrd', 'bbrewaed', 'bbrewa4d', 'bbrewa5d', 'bbrewatd', 'bbrewagd', 'bbrewafd',
                          'bbrewadd', 'bbrewars', 'bbreware', 'bbrewarr', 'bbrewarf', 'bbrewarc', 'bbrewarx',
                          'vbbreward', 'bvbreward', 'gbbreward', 'bgbreward', 'hbbreward', 'bhbreward', 'nbbreward',
                          'bnbreward', 'bbvreward', 'bbgreward', 'bbhreward', 'bbnreward', 'bbereward', 'bb4reward',
                          'bbr4eward', 'bb5reward', 'bbr5eward', 'bbtreward', 'bbrteward', 'bbrgeward', 'bbfreward',
                          'bbrfeward', 'bbdreward', 'bbrdeward', 'bbrweward', 'bbr3eward', 'bbre3ward', 'bbre4ward',
                          'bbrerward', 'bbrefward', 'bbredward', 'bbrseward', 'bbresward', 'bbreqward', 'bbrewqard',
                          'bbre2ward', 'bbrew2ard', 'bbrew3ard', 'bbreweard', 'bbrewdard', 'bbrewsard', 'bbreaward',
                          'bbrewaqrd', 'bbrewawrd', 'bbrewasrd', 'bbrewxard', 'bbrewaxrd', 'bbrewzard', 'bbrewazrd',
                          'bbrewaerd', 'bbrewared', 'bbrewa4rd', 'bbrewar4d', 'bbrewa5rd', 'bbrewar5d', 'bbrewatrd',
                          'bbrewartd', 'bbrewagrd', 'bbrewargd', 'bbrewafrd', 'bbrewarfd', 'bbrewadrd', 'bbrewarsd',
                          'bbrewards', 'bbrewarde', 'bbrewardr', 'bbrewardf', 'bbrewarcd', 'bbrewardc', 'bbrewarxd',
                          'bbrewardx', 'brwrd', 'bbwrd', 'bbrrd', 'bbrwd', 'bbrwr', 'bbbrwrd', 'bbrrwrd', 'bbrwwrd',
                          'bbrwrrd', 'bbrwrdd', 'brbwrd', 'bbwrrd', 'bbrrwd', 'bbrwdr', 'vbrwrd', 'gbrwrd', 'hbrwrd',
                          'nbrwrd', 'bvrwrd', 'bgrwrd', 'bhrwrd', 'bnrwrd', 'bbewrd', 'bb4wrd', 'bb5wrd', 'bbtwrd',
                          'bbgwrd', 'bbfwrd', 'bbdwrd', 'bbrqrd', 'bbr2rd', 'bbr3rd', 'bbrerd', 'bbrdrd', 'bbrsrd',
                          'bbrard', 'bbrwed', 'bbrw4d', 'bbrw5d', 'bbrwtd', 'bbrwgd', 'bbrwfd', 'bbrwdd', 'bbrwrs',
                          'bbrwre', 'bbrwrr', 'bbrwrf', 'bbrwrc', 'bbrwrx', 'vbbrwrd', 'bvbrwrd', 'gbbrwrd', 'bgbrwrd',
                          'hbbrwrd', 'bhbrwrd', 'nbbrwrd', 'bnbrwrd', 'bbvrwrd', 'bbgrwrd', 'bbhrwrd', 'bbnrwrd',
                          'bberwrd', 'bb4rwrd', 'bbr4wrd', 'bb5rwrd', 'bbr5wrd', 'bbtrwrd', 'bbrtwrd', 'bbrgwrd',
                          'bbfrwrd', 'bbrfwrd', 'bbdrwrd', 'bbrdwrd', 'bbrqwrd', 'bbrwqrd', 'bbr2wrd', 'bbrw2rd',
                          'bbr3wrd', 'bbrw3rd', 'bbrwerd', 'bbrwdrd', 'bbrswrd', 'bbrwsrd', 'bbrawrd', 'bbrwred',
                          'bbrw4rd', 'bbrwr4d', 'bbrw5rd', 'bbrwr5d', 'bbrwtrd', 'bbrwrtd', 'bbrwgrd', 'bbrwrgd',
                          'bbrwfrd', 'bbrwrfd', 'bbrwrsd', 'bbrwrds', 'bbrwrde', 'bbrwrdr', 'bbrwrdf', 'bbrwrcd',
                          'bbrwrdc', 'bbrwrxd', 'bbrwrdx', '/bbr', '/bbrwrd', '/bbreward', '/battlebreakersrewards',
                          'battlebreakersrewards', 'bbitem', '/bbitem'],
                 extras={'emoji': "Shared2", "args": {'day': 'The day to get the rewards of. Not required if you '
                                                             'are authenticated',
                                                      'limit': 'The number of upcoming days to see (Optional)'},
                         "dev": False},
                 brief="View info about a specific day\'s reward, and the rewards that follow in Battle Breakers",
                 description="This command lets you view the rewards of any specific day, and any number of rewards "
                             "that follow. This command is for Battle Breakers rewards.")
    async def bbreward(self, ctx, day='hi readers of the bot', limit='7'):
        await self.bbreward_command(ctx, day, int(limit))

    @slash_command(name='bbreward',
                   description='View info about a specific day\'s reward, and the rewards that follow in Battle Breakers',
                   guild_ids=stw.guild_ids)
    async def bbslashreward(self, ctx: discord.ApplicationContext,
                            day: Option(int,
                                        "The day to get the rewards of. Not required if you are authenticated") = 'hi readers of the bot',
                            limit: Option(int, "The number of upcoming days to see") = 7):
        await self.bbreward_command(ctx, day, limit, True)


def setup(client):
    client.add_cog(BBReward(client))
