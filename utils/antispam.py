import time
import sched
import discord
import asyncio
from discord.ext import commands

startTime = None
spamControl = {}
spamTimer = 16
spamMessageLimit = 6

def setStartTime():
    global startTime
    startTime = time.time()


def setSpamTimer(seconds: int):
    global spamTimer
    spamTimer = seconds


def setSpamMessageLimit(messageCount: int):
    global spamMessageLimit
    spamMessageLimit = messageCount

async def addSpamCounter(user: discord.Member, bott: commands.Bot):
    global spamControl
    global spamMessageLimit

    server = user.guild

    if user not in spamControl:
        spamControl[user] = 1
    else:
        spamControl[user] += 1
       
    if spamControl[user] == spamMessageLimit:
        print("fuck")
        role = discord.utils.get(server.roles, name="Muted")
        await user.add_roles(role)
            #return

        mutedRole = None
        for role in server.roles:
            if role.name == "Muted":
                mutedRole = role
                break
#
        if mutedRole is not None:
            await bott.add_roles(user, role)
        else:
            return
            #await bot.send_message(channel, "Unable to mute user, make sure the **Muted** role exists")


async def reduceSpamCounter(user: discord.Member, bott: commands.Bot):
    global spamControl
    global spamTimer
    global spamMessageLimit

    await asyncio.sleep(spamTimer)
    server = user.guild
    
    if user in spamControl:
        spamControl[user] -= 1
        
    if spamControl[user] == (spamMessageLimit-1):
        print("fuck")
        role = discord.utils.get(server.roles, name="Muted")
        await user.remove_roles(role)



        mutedRole = None
        for role in user.roles:
            if role.name == "Muted":
                mutedRole = role
                break
            
        if mutedRole is not None:
            await bott.remove_roles(user, role)