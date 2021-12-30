from discord.ext import commands
import requests
import json
import re
import os

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

bot = commands.Bot(command_prefix="!pql-ladder ")

def api_call():
    response = requests.get("http://api:42069")
    dict_response = json.loads(response.content)
    return dict_response["players"]

def clean_name(nick):
    return re.sub(r"[\^][0-9]","", nick)

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))

@bot.command()
async def rank(ctx, arg):

    if arg.isdigit() == True:
        players = api_call()
        clean_nick = clean_name(players[int(arg)-1]["nickname"])
        rating = players[int(arg)-1]["rating"]
        await ctx.channel.send(clean_nick + " is at rank " + arg + " with " + str(rating) + " rating")

    return

@bot.command()
async def top(ctx, arg):

    if arg.isdigit() == True:
        if int(arg) <= 5:
            players = api_call()
            top_players = []
            for i in range(int(arg)):
                top_players.append(players[i])

            nicknames = [player['nickname'] for player in top_players]
            clean_nicks = []
            for nick in nicknames:
                clean_nicks.append(clean_name(nick))
            ratings = [player['rating'] for player in top_players]

            output = ""
            for j in range(len(top_players)):
                output = output + "Rank " + str(j+1) + " - " + clean_nicks[j] + " - Rating " + str(ratings[j]) + "\n"

            await ctx.channel.send(output)
        else:
            await ctx.channel.send("chill, max 5 pls")

    return

@bot.command()
async def steamid(ctx, arg):
    if arg.isdigit() == True:
        response = requests.get("http://api:42069/" + str(arg))
        dict_response = json.loads(response.content)
        await ctx.channel.send(clean_name(dict_response["nickname"]) + " with " + str(dict_response["rating"]) + " rating")

    return

@bot.command(name="2k")
async def two_k(ctx):
    players = api_call()
    two_k_players = list(filter(lambda d: d['rating'] >= 2000, players))
    nicknames = [player['nickname'] for player in two_k_players]
    clean_nicks = []
    for nick in nicknames:
        clean_nicks.append(clean_name(nick))
    nicks_string = ', '.join(clean_nicks)
    await ctx.channel.send("Players rated 2000 or above:\n" + nicks_string)

    return

bot.run(DISCORD_TOKEN)