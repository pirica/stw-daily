"""
STW Daily Discord bot Copyright 2023 by the STW Daily team.
Please do not skid our hard work.
https://github.com/dippyshere/stw-daily

This file is the cog for the battle breakers daily reward command. claims battle breakers dailies

BATTLE BREAKERS!

WOAH-OH-OH, OOH-WOAH-OH OOH-WOAH-OH, OOH-WOAH-OH
Monsters from the sky, Want us all to die. Hiding underground, now they all must be found.
Break the crystals, set them free. Battle your way to victory.

BATTLE BREAKERS!

OH-WOAH-OH, OH-WOAH-OH
ctrl + shift + o what does that do :o
BATTLE BREAKERS!
:D"""

import asyncio
import orjson

import discord
import discord.ext.commands as ext
from discord import Option, OptionChoice

import stwutil as stw


# auth session for bb should we bother?
# eh ill try it later

class BattleBreakersDaily(ext.Cog):
    """
    Cog for the battle breaker daily command
    """

    def __init__(self, client):
        self.client = client
        self.emojis = client.config["emojis"]

    async def bbdaily_command(self, ctx):
        """
        The main function of the Battle Breakers Daily command

        Args:
            ctx: the context of the command

        Returns:
            None
        """
        desired_lang = await stw.I18n.get_desired_lang(self.client, ctx)
        embed = await stw.battle_breakers_deprecation(self.client, ctx, "util.battlebreakers.deprecation.embed.description2.bbdaily", desired_lang)
        return await stw.slash_send_embed(ctx, self.client, embed)

        # succ_colour = self.client.colours["success_green"]
        #
        # auth_info = await stw.get_or_create_auth_session(self.client, ctx, "bbdaily", authcode, auth_opt_out, True)
        # if not auth_info[0]:
        #     return
        #
        # final_embeds = []
        #
        # ainfo3 = ""
        # try:
        #     ainfo3 = auth_info[3]
        # except:
        #     pass
        #
        # # what is this black magic???????? I totally forgot what any of this is and how is there a third value to the auth_info??
        # # okay I discovered what it is, it's basically the "welcome whoever" embed that is edited
        # if ainfo3 != "logged_in_processing" and auth_info[2] != []:
        #     final_embeds = auth_info[2]
        #
        # # ok now we have the authcode information stuff, so it's time to attempt to claim daily on the road
        # request = await stw.profile_request(self.client, "daily", auth_info[1], game="bb")
        # json_response = orjson.loads(await request.read())
        #
        # # check for le error code
        # try:
        #     error_code = json_response["errorCode"]
        #     support_url = self.client.config["support_url"]
        #     acc_name = auth_info[1]["account_name"]
        #     # TODO: determine what happens here after 30th December 2022
        #     # Answer: WEX 504 gateway timeout
        #     embed = await stw.post_error_possibilities(ctx, self.client, "bbdaily", acc_name, error_code, support_url,
        #                                                response=json_response)
        #     final_embeds.append(embed)
        #     await stw.slash_edit_original(ctx, auth_info[0], final_embeds)
        # except KeyError:
        #     day = await asyncio.gather(asyncio.to_thread(stw.bb_day_query_check, json_response))
        #
        #     try:
        #         self.client.temp_auth[ctx.author.id]["bb_day"] = day[0]
        #     except KeyError:
        #         pass
        #
        #     if ctx.channel.id != 762864224334381077:
        #         dumb_useless_crap, name, emoji_text, description, amount = stw.get_bb_reward_data(self.client,
        #                                                                                           json_response,
        #                                                                                           pre_calc_day=day[0])
        #         # already claimed is handled in error since wex does that
        #
        #         # Initialise the claimed embed
        #         embed = discord.Embed(title=await stw.add_emoji_title(self.client, "Success", "checkmark"),
        #                               description="\u200b",
        #                               colour=succ_colour)
        #
        #         embed.add_field(name=f'{emoji_text} On day **{day[0]}**, you received:', value=f"```{amount} {name}```",
        #                         inline=True)
        #     else:
        #         embed = discord.Embed(title=await stw.add_emoji_title(self.client, "Success", "checkmark"),
        #                               description=f"\u200b\n<:Check:812201301843902474> "
        #                                           f"Successfully claimed daily reward"
        #                                           f"\n\u200b\n{self.emojis['check_mark']} **Please claim in "
        #                                           f"<#757768833946877992> for more detail** "
        #                                           f"\n\u200b",
        #                               colour=succ_colour)
        #     if ctx.channel.id != 762864224334381077:
        #         rewards = ''
        #         for i in range(1, 8):
        #             data = stw.get_bb_reward_data(self.client, pre_calc_day=day[0] + i)
        #             rewards += str(data[4]) + " " + str(data[1])
        #             if not (i + 1 == 8):
        #                 rewards += ', '
        #             else:
        #                 rewards += '.'
        #
        #         calendar = self.client.config["emojis"]["calendar"]
        #         embed.add_field(name=f'\u200b\n{calendar} Rewards for the next 7 days:', value=f'```{rewards}```\u200b',
        #                         inline=False)
        #     embed = await stw.set_thumbnail(self.client, embed, "check")
        #
        #     embed = await stw.add_requested_footer(ctx, embed)
        #     final_embeds.append(embed)
        #     await stw.slash_edit_original(ctx, auth_info[0], final_embeds)
        #     return

    # Battle Breakers is a new tactical role-playing game developed by Epic Games for mobile and PC.
    @ext.command(name='bbdaily',
                 aliases=['bbd', 'battlebreakersdaily', 'wex', 'bd', 'bb', 'bbbd', 'bbdd', 'bdb', 'gbd', 'hbd',
                          'nbd', 'bvd', 'bgd', 'bhd', 'bbs', 'bbe', 'bbf', 'bbc', 'vbbd', 'bvbd', 'gbbd',
                          'bgbd', 'hbbd', 'bhbd', 'nbbd', 'bnbd', 'bbvd', 'bbgd', 'bbhd', 'bbnd', 'bbsd', 'bbds',
                          'bbed', 'bbde', 'bbrd', 'bbdr', 'bbfd', 'bbdf', 'bbcd', 'bbdc', 'bbxd', 'bbdx', 'bdaily',
                          'bbaily', 'bbdily', 'bbdaly', 'bbdaiy', 'bbdail', 'bbbdaily', 'bbddaily', 'bbdaaily',
                          'bbdaiily', 'bbdailly', 'bbdailyy', 'bdbaily', 'bbadily', 'bbdialy', 'bbdaliy', 'bbdaiyl',
                          'vbdaily', 'gbdaily', 'hbdaily', 'nbdaily', 'bvdaily', 'bgdaily', 'bhdaily', 'bndaily',
                          'bbsaily', 'bbeaily', 'bbraily', 'bbfaily', 'bbcaily', 'bbxaily', 'bbdqily', 'bbdwily',
                          'bbdsily', 'bbdxily', 'bbdzily', 'bbdauly', 'bbda8ly', 'bbda9ly', 'bbdaoly', 'bbdally',
                          'bbdakly', 'bbdajly', 'bbdaiky', 'bbdaioy', 'bbdaipy', 'bbdailt', 'bbdail6', 'bbdail7',
                          'bbdailu', 'bbdailj', 'bbdailh', 'bbdailg', 'vbbdaily', 'bvbdaily', 'gbbdaily', 'bgbdaily',
                          'hbbdaily', 'bhbdaily', 'nbbdaily', 'bnbdaily', 'bbvdaily', 'bbgdaily', 'bbhdaily',
                          'bbndaily', 'bbsdaily', 'bbdsaily', 'bbedaily', 'bbdeaily', 'bbrdaily', 'bbdraily',
                          'bbfdaily', 'bbdfaily', 'bbcdaily', 'bbdcaily', 'bbxdaily', 'bbdxaily', 'bbdqaily',
                          'bbdaqily', 'bbdwaily', 'bbdawily', 'bbdasily', 'bbdaxily', 'bbdzaily', 'bbdazily',
                          'bbdauily', 'bbdaiuly', 'bbda8ily', 'bbdai8ly', 'bbda9ily', 'bbdai9ly', 'bbdaoily',
                          'bbdaioly', 'bbdalily', 'bbdakily', 'bbdaikly', 'bbdajily', 'bbdaijly', 'bbdailky',
                          'bbdailoy', 'bbdaiply', 'bbdailpy', 'bbdailty', 'bbdailyt', 'bbdail6y', 'bbdaily6',
                          'bbdail7y', 'bbdaily7', 'bbdailuy', 'bbdailyu', 'bbdailjy', 'bbdailyj', 'bbdailhy',
                          'bbdailyh', 'bbdailgy', 'bbdailyg', '/bbd', 'battlebreakers', '/battlebreakers', '/wex',
                          '/bd', '/bbdaily', 'বিডি প্রতিদিন', 'bb diàriament', 'bb denně', 'bb καθημερινά',
                          'bbdiariamente', 'દરરોજ', 'כל יום', 'bb zilnic', 'bb denne', 'ббдаили', 'bb kila siku',
                          'தினமும்', 'ప్రతిరోజు', 'bbgünlük', 'بی بی ڈیلی', 'bbdailn', 'bbdmily', 'dbbdaily', 'sbdaily',
                          'bbdailb', 'bbdawly', 'bbdagily', 'bbiaily', 'bbdailyi', 'bbdaivy', 'bbdapily', 'bbjaily',
                          'bbdbaily', 'bbdaigy', 'bbqdaily', 'bbdaeily', 'bbdagly', 'pbdaily', 'bebdaily', 'btbdaily',
                          'bbdtaily', 'bbdaiely', 'btdaily', 'bbdaijy', 'bbdaaly', 'bzbdaily', 'xbdaily', 'bbdailyr',
                          'bbdyaily', 'blbdaily', 'bsbdaily', 'bbldaily', 'bbdailf', 'bfbdaily', 'bbdatly', 'bldaily',
                          'bbdyily', 'bbdavly', 'bbdaigly', 'bbdayly', 'kbbdaily', 'bbdafly', 'bbtaily', 'jbbdaily',
                          'bbydaily', 'ebdaily', 'bbdacly', 'bbdailyz', 'bbdoily', 'bbdjily', 'rbdaily', 'ybdaily',
                          'ubdaily', 'bbdaisly', 'bbdrily', 'bbyaily', 'bbdaile', 'bbdaply', 'bbdazly', 'bbdailyo',
                          'bbdaisy', 'bbdainy', 'bbaaily', 'bbdailcy', 'bbdiily', 'bedaily', 'bbdailny', 'ybbdaily',
                          'brdaily', 'bbdkaily', 'bbdailz', 'tbdaily', 'bqdaily', 'bblaily', 'bbmaily', 'bbdaqly',
                          'bbdailyc', 'bbdailyn', 'bbdailm', 'bbdaizly', 'budaily', 'bidaily', 'bbdasly', 'bbdadly',
                          'bbdaixy', 'bbdoaily', 'bbzaily', 'bbdailw', 'bbdailyl', 'bbdaiby', 'bbdavily', 'bbdaicly',
                          'kbdaily', 'bbdpily', 'bbdaxly', 'bbdailxy', 'bbdaivly', 'bydaily', 'bbdailyk', 'xbbdaily',
                          'bwbdaily', 'bbdailr', 'bcdaily', 'fbdaily', 'bbdaiqy', 'bbdaill', 'zbdaily', 'bbdaialy',
                          'bbdailyf', 'bbdairly', 'bbdailyx', 'bmdaily', 'bbdaiyly', 'bbdably', 'bbdaidy', 'qbdaily',
                          'bbodaily', 'bbdailya', 'bbdailc', 'bbidaily', 'bbdailp', 'bbdaidly', 'bbdailyd', 'bbdaild',
                          'lbdaily', 'bbdvaily', 'bbdaibly', 'bbdiaily', 'bbdailo', 'bfdaily', 'bbdeily', 'bbdaiuy',
                          'bbdailyw', 'bbdlily', 'bbduily', 'bmbdaily', 'bbdaity', 'bbvaily', 'bboaily', 'bbdailym',
                          'bubdaily', 'bbdaixly', 'bbdnily', 'obdaily', 'lbbdaily', 'bjdaily', 'bbdailyb', 'ibdaily',
                          'bbtdaily', 'bxbdaily', 'bbdailyp', 'bbdhaily', 'bbdhily', 'cbbdaily', 'bxdaily', 'bzdaily',
                          'bbdaicy', 'bbdailv', 'bbdailey', 'bbdaili', 'bbnaily', 'bbdailwy', 'bbdaiwy', 'bbdaely',
                          'bbdvily', 'bbdails', 'bbduaily', 'bbdailvy', 'abbdaily', 'bbdlaily', 'bibdaily', 'ibbdaily',
                          'bsdaily', 'bbkaily', 'bbdailsy', 'bpbdaily', 'bbdailmy', 'cbdaily', 'babdaily', 'bybdaily',
                          'bbkdaily', 'bpdaily', 'bodaily', 'bbdpaily', 'bbdjaily', 'bbdaifly', 'bddaily', 'bbgaily',
                          'bbqaily', 'bbdatily', 'pbbdaily', 'bqbdaily', 'bbmdaily', 'bbdaiyy', 'mbbdaily', 'bbdayily',
                          'bbdtily', 'bbdkily', 'rbbdaily', 'bbdaila', 'bbdaify', 'bbdailx', 'bbdacily', 'bbwaily',
                          'bbwdaily', 'bbdanly', 'badaily', 'bbdnaily', 'bbdailfy', 'brbdaily', 'bbzdaily', 'fbbdaily',
                          'zbbdaily', 'mbdaily', 'bbdailby', 'bbdahly', 'bbudaily', 'bbdaiey', 'bbdanily', 'ebbdaily',
                          'dbdaily', 'bdbdaily', 'bbdarily', 'bbdfily', 'bbdamly', 'bbjdaily', 'bbdamily', 'bbdailq',
                          'bbdadily', 'sbbdaily', 'bbdailys', 'obbdaily', 'bbdailqy', 'bwdaily', 'ubbdaily', 'abdaily',
                          'bbdaihly', 'bbuaily', 'bbdahily', 'qbbdaily', 'bbpaily', 'jbdaily', 'bbadaily', 'bcbdaily',
                          'bbdaizy', 'bobdaily', 'bbdarly', 'wbbdaily', 'bbdailk', 'bkdaily', 'wbdaily', 'bbdaihy',
                          'bbdabily', 'bbpdaily', 'bbdailyq', 'bbhaily', 'bbdcily', 'bbdaildy', 'bkbdaily', 'bjbdaily',
                          'bbdaiwly', 'bbddily', 'bbdaiay', 'bbdailyv', 'bbbaily', 'bbdailry', 'bbdgaily', 'bbdgily',
                          'bbdaimy', 'bbdafily', 'bbdainly', 'bbdailzy', 'bbdmaily', 'bbdairy', 'bbdailiy', 'bbdailye',
                          'tbbdaily', 'bbdaimly', 'bbdaiiy', 'bbdailay', 'bbdaitly', 'bbdaiqly', 'bbdbily', 'bbda7ly',
                          'bbda&ly', 'bbda*ly', 'bbda(ly', 'bbdai;y', 'bbdai/y', 'bbdai.y', 'bbdai,y', 'bbdai?y',
                          'bbdai>y', 'bbdai<y', 'bbdail5', 'bbdail%', 'bbdail^', 'bbdail&', 'bbclvaim', 'bbclamim',
                          'bbclam', 'bclaim', 'bbclami', 'bbcalim', 'bbcaim', 'bbclaam', 'bbwclaim', 'bblaim',
                          'bbclaim', 'bbclaimw', 'bbclai', 'bbtlaim', 'bgclaim', 'bbcliam', 'blclaim', 'bbcsaim',
                          'bcblaim', 'bebclaim', 'bbclacim', 'bbelaim', 'bbclaium', 'nbclaim', 'bbculaim', 'bbjclaim',
                          'lbclaim', 'bbciaim', 'bbclim', 'bbclaimh', 'bbclnaim', 'bbkclaim', 'bbclgaim', 'bbdlaim',
                          'bbzlaim', 'bbcglaim', 'bblcaim', 'bbclaimg', 'bbclqim', 'bbclgim', 'bbclakm', 'bdbclaim',
                          'bbcladim', 'bbklaim', 'pbbclaim', 'bbcxaim', 'bgbclaim', 'bbclazim', 'bbclhaim', 'bhclaim',
                          'bbclazm', 'bbclaimr', 'bbczlaim', 'bbclaig', 'mbbclaim', 'bbclcim', 'bbtclaim', 'hbclaim',
                          'bbcelaim', 'bbcltim', 'bkclaim', 'zbbclaim', 'bbclaimv', 'bbclaix', 'bbcpaim', 'bbclait',
                          'bwbclaim', 'bbclaimz', 'bbilaim', 'bbcfaim', 'bbclqaim', 'bvbclaim', 'bbcuaim', 'bbcnaim',
                          'zbclaim', 'bbcoaim', 'bbclail', 'ubbclaim', 'buclaim', 'bbclaihm', 'btbclaim', 'bbmclaim',
                          'bbclahm', 'bbslaim', 'bcclaim', 'bbclalm', 'bubclaim', 'bsbclaim', 'bbclpim', 'bbcleaim',
                          'bbclaiv', 'bbccaim', 'bbclaiam', 'bxclaim', 'bbclrim', 'qbbclaim', 'babclaim', 'bzclaim',
                          'bbchlaim', 'rbclaim', 'bbuclaim', 'bbctlaim', 'bbckaim', 'bbyclaim', 'boclaim', 'bbclapm',
                          'bbcgaim', 'bwclaim', 'bbcllaim', 'bbclapim', 'gbclaim', 'bbnlaim', 'bbclaitm', 'bbclawm',
                          'bbclagim', 'bbbclaim', 'bbeclaim', 'bbclaia', 'bbclaigm', 'bbsclaim', 'bbclaimf', 'bbcleim',
                          'bbxclaim', 'bbcolaim', 'btclaim', 'bbclaiy', 'bbclyaim', 'obbclaim', 'vbbclaim', 'bobclaim',
                          'ubclaim', 'fbbclaim', 'bbclaik', 'bbclsaim', 'bbmlaim', 'bbcrlaim', 'bbcldaim', 'bbclaij',
                          'bbclxim', 'bbclaiu', 'bbcllim', 'bbclabim', 'bbclaivm', 'bbcljaim', 'bbiclaim', 'bhbclaim',
                          'kbclaim', 'bbclaibm', 'nbbclaim', 'jbclaim', 'bbclanim', 'bbclairm', 'bdclaim', 'bbcyaim',
                          'bbclwaim', 'bbfclaim', 'bbclaidm', 'ibbclaim', 'byclaim', 'bbclraim', 'bbclaimu', 'bbclaiim',
                          'bbclaiz', 'bbchaim', 'bbclaif', 'bnclaim', 'bbclfim', 'bbclzaim', 'bbclaifm', 'bbclaio',
                          'bbcwaim', 'bbcilaim', 'bbclajim', 'bcbclaim', 'bjbclaim', 'bbqclaim', 'bbclzim', 'bbcdaim',
                          'baclaim', 'bbclaiem', 'tbclaim', 'bbcaaim', 'bbclaem', 'bbclaxim', 'bbcclaim', 'bbclhim',
                          'bbclatm', 'bbclmaim', 'bbclaiom', 'bbcluaim', 'mbclaim', 'bbqlaim', 'bfclaim', 'sbbclaim',
                          'bbcldim', 'bbcladm', 'bbrclaim', 'bblclaim', 'bbclfaim', 'bbclbaim', 'bqbclaim', 'bbclasim',
                          'vbclaim', 'bbclaimo', 'bbclabm', 'sbclaim', 'bbclaima', 'bbclaib', 'bbhlaim', 'bbcylaim',
                          'bbcvlaim', 'bbclaimx', 'bbcplaim', 'bbcdlaim', 'bbcjaim', 'bbclmim', 'bbcflaim', 'bbcliim',
                          'bbclaipm', 'bjclaim', 'biclaim', 'bbclaii', 'bbclkim', 'bbclaimk', 'ybbclaim', 'bbclakim',
                          'bfbclaim', 'bbcxlaim', 'bpbclaim', 'bbclaimq', 'bbclaiqm', 'bbclaxm', 'bbclafim', 'bbclaic',
                          'bzbclaim', 'tbbclaim', 'bbgclaim', 'bbclaum', 'bbclaym', 'abclaim', 'bbclaimn', 'brbclaim',
                          'bbcmlaim', 'bbclarim', 'ebclaim', 'bbclahim', 'bbblaim', 'bbclavm', 'bbclain', 'obclaim',
                          'bbzclaim', 'bbclwim', 'bbcloaim', 'bpclaim', 'bbclaiml', 'beclaim', 'wbbclaim', 'bbllaim',
                          'bibclaim', 'bsclaim', 'bbcmaim', 'qbclaim', 'bkbclaim', 'bbclais', 'bbcnlaim', 'bbcltaim',
                          'bbclaizm', 'gbbclaim', 'bbclanm', 'bbclaikm', 'bbclawim', 'bbvlaim', 'bbdclaim', 'bbclaicm',
                          'dbclaim', 'bbaclaim', 'bbclsim', 'bbcjlaim', 'bbclaaim', 'hbbclaim', 'pbclaim', 'bbclaqim',
                          'bbclaih', 'bbalaim', 'bbclaimt', 'bbclyim', 'bbflaim', 'bboclaim', 'bbxlaim', 'brclaim',
                          'ebbclaim', 'bbclaimm', 'bbclcaim', 'lbbclaim', 'bbclbim', 'bbclaijm', 'fbclaim', 'bbclaims',
                          'bbclaeim', 'wbclaim', 'bbclaixm', 'bbylaim', 'bbnclaim', 'ibclaim', 'bbclailm', 'bbrlaim',
                          'bbclafm', 'bmbclaim', 'kbbclaim', 'bbclaimc', 'bbclaism', 'bbclnim', 'bbcblaim', 'bbclaiq',
                          'bbclpaim', 'bbclaip', 'xbclaim', 'bybclaim', 'bbclaqm', 'xbbclaim', 'dbbclaim', 'bbclaimy',
                          'blbclaim', 'bqclaim', 'bbclaid', 'bbcliaim', 'bbcljim', 'bbcloim', 'bbcqaim', 'bbclaoim',
                          'bbcwlaim', 'bbclair', 'bbclamm', 'bbglaim', 'bbclavim', 'bbclauim', 'bbcbaim', 'bbclaie',
                          'bmclaim', 'bbczaim', 'bnbclaim', 'bbcslaim', 'bbclaimj', 'bbjlaim', 'bbclaiym', 'bbclalim',
                          'bbclarm', 'bbclajm', 'bbclatim', 'bbcluim', 'bbclaimb', 'bbolaim', 'bbclacm', 'cbbclaim',
                          'bbctaim', 'bbclainm', 'bbclaiwm', 'bbclaom', 'bbclxaim', 'bbclaime', 'ybclaim', 'bbcqlaim',
                          'bbcklaim', 'bbclayim', 'bbclagm', 'abbclaim', 'bbclasm', 'bvclaim', 'bbclaiw', 'bbulaim',
                          'bbvclaim', 'bbclkaim', 'bbclaimp', 'bbcraim', 'bbclaimi', 'bbclvim', 'bbpclaim', 'bxbclaim',
                          'cbclaim', 'bbcvaim', 'bbhclaim', 'bbplaim', 'bbcalaim', 'bbwlaim', 'bbclaimd', 'jbbclaim',
                          'rbbclaim', 'bbceaim', 'bbc;aim', 'bbc/aim', 'bbc.aim', 'bbc,aim', 'bbc?aim', 'bbc>aim',
                          'bbc<aim', 'bbcla7m', 'bbcla8m', 'bbcla9m', 'bbcla&m', 'bbcla*m', 'bbcla(m', 'bbclai,',
                          'bbclai<', '/bbclaim'],
                 extras={'emoji': "T_MTX_Gem_Icon", "args": {
                     'generic.meta.args.authcode': ['generic.slash.token', True],
                     'generic.meta.args.optout': ['generic.meta.args.optout.description', True]},
                         "dev": True, "description_keys": ['bbdaily.meta.description.main1',
                                                           ['bbdaily.meta.description.list.item1', '`daily`']],
                         "name_key": "bbdaily.slash.name", "battle_broken": True},
                 brief="bbdaily.meta.brief",
                 description="{0}\n{1}")
    async def bbdaily(self, ctx):
        """
        This function is the entry point for the bbdaily command when called traditionally

        Args:
            ctx: the context of the command
        """

        await self.bbdaily_command(ctx)

    # @ext.slash_command(name='bbdaily', name_localizations=stw.I18n.construct_slash_dict("bbdaily.slash.name"),
    #                    description='Claim your Battle Breakers daily reward',
    #                    description_localizations=stw.I18n.construct_slash_dict("bbdaily.slash.description"),
    #                    guild_ids=stw.guild_ids)
    # async def slashbbdaily(self, ctx: discord.ApplicationContext,
    #                        token: Option(
    #                            description="Your Epic Games authcode. Required unless you have an active session.",
    #                            description_localizations=stw.I18n.construct_slash_dict(
    #                                "generic.slash.token"),
    #                            name_localizations=stw.I18n.construct_slash_dict("generic.meta.args.token"),
    #                            min_length=32) = "",
    #                        auth_opt_out: Option(default="False",
    #                                             description="Opt out of starting an authentication session",
    #                                             description_localizations=stw.I18n.construct_slash_dict(
    #                                                 "generic.slash.optout"),
    #                                             name_localizations=stw.I18n.construct_slash_dict(
    #                                                 "generic.meta.args.optout"),
    #                                             choices=[OptionChoice("Do not start an authentication session", "True",
    #                                                                   stw.I18n.construct_slash_dict(
    #                                                                       "generic.slash.optout.true")),
    #                                                      OptionChoice("Start an authentication session (Default)",
    #                                                                   "False",
    #                                                                   stw.I18n.construct_slash_dict(
    #                                                                       "generic.slash.optout.false"))]) = "False"):
    #     """
    #     This function is the entry point for the bbdaily command when called via slash
    #
    #     Args:
    #         ctx: The context of the slash command
    #         token: The authcode of the user
    #         auth_opt_out: Whether the user wants to opt out of starting an authentication session
    #     """
    #     await self.bbdaily_command(ctx)


def setup(client):
    """
    This function is called when the cog is loaded via load_extension

    Args:
        client: The bot client
    """
    client.add_cog(BattleBreakersDaily(client))
