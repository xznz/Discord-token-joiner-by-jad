from discord.ext.commands.core import command
import requests
import time
import asyncio
import discord
from discord.ext import commands
import random

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!")
bot.remove_command('help')

color = FFD700 

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name=f"Made by Jad with peace"))



@bot.command()
async def help(ctx):
    embed = discord.Embed(title='Help', description='!help\n!join [link]\n\n !stock\n!raid [link] [channel-id] [message]',color=color)
    await ctx.send(embed=embed)


balls = open('proxies.txt','r')
balls2 = balls.readlines()
proxies = {
  "http": random.choice(balls2)
}

@bot.command()
async def join(ctx, serverlink):
        s = serverlink.split('/')
        embed = discord.Embed(title='Joining Server', description=f'Joining {s[3]} with 1 tokens! Tokens can sometimes be locked on join!', color=color)
        await ctx.send(embed=embed)
        await asyncio.sleep(2)
        r = open('tokens.txt', 'r')
        r2 = r.readlines()
        headers = {
        "Authorization": random.choice(r2),
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
        }
        await asyncio.sleep(2)
        r = requests.post(f'https://discord.com/api/v9/invites/{s[3]}', headers=headers,proxies=proxies)
        print(r.text)
        if r.status_code == 403:
          embed = discord.Embed(title='Account Locked', description='This account is email/phone locked!')
          await ctx.send(embed=embed)


@bot.command()
async def stock(ctx):
    f = open('tokens.txt', 'r')
    f2 = f.readlines()
    embed = discord.Embed(title='Stock', description=f'Current tokens: {len(f2)}',color=color)
    await ctx.send(embed=embed)


@bot.command()
async def raid(ctx, link, channel, message):
    r = open('tokens.txt')
    r2 = r.readlines()
    a2 = link.split('/')
    embed = discord.Embed(
      title='Raiding Server!',
      description=f'Raiding {a2[3]} with 1 token!',
      color=color
    )
    await ctx.send(embed=embed)
    headers = {
      'authorization': random.choice(r2),
      }
    r = requests.post(f'https://discord.com/api/v9/invites/{a2[3]}', headers=headers)
    await asyncio.sleep(15)
    data2 = {
        "content": message
    }
    r2 = requests.post(f'https://discord.com/api/v9/channels/{channel}/messages',data=data2,headers=headers)
    print(r2.text)



bot.run('Discord bot token here')
