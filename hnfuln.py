#!/usr/bin/env python3

import sys
import discord

client = discord.Client()
count  = {}

async def update(g, n):
    print(f'>> updating {g}')
    count[g] = n
    try: await g.edit(name=f'h{n}ful{n}')
    except Exception as e:
        print(f'!>> error updating servername. check permissions. err: {e}')
        return
    print(f'+>> successfully updated {g}')


async def updateall():
    print('>> updating all guilds')
    for g in client.guilds:
        n = len(g.members)
        if not g in count or count[g] != n:
            await update(g, n)


@client.event
async def on_guild_join(guild):
    print(f'>> joined {guild}')
    await updateall()


@client.event
async def on_ready():
    print('>> client ready')
    await updateall()


@client.event
async def on_member_remove(member):
    print(f'>> {member} left')
    await updateall()


@client.event
async def on_member_join(member):
    print(f'>> {member} joined')
    await updateall()


if len(sys.argv) != 2: sys.exit('usage: python hnfuln.py <discord bot token>')
else: client.run(sys.argv[1])
