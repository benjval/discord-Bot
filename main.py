import random
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='<', intents= intents)

# @client.event
# async def on_ready():
#     print("We have logged inn as {0.user}".format(client))
    
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content.startswith("hi"):
#         print("funciona")
#         await message.channel.send("hello")

@bot.command(name="hi")
async def hi(ctx):
    print("llega la señal")
    if not ctx.message.author.voice:
        await ctx.send("{} Conectate a voz y quisas te salude".format(ctx.message.author.name))
        return
    else:
        channel= ctx.message.author.voice.channel
        await ctx.send("{} Hola espero que estes bien en {}".format(ctx.message.author.name, channel))
        return

@bot.command(name="d")
async def d(ctx, dados):
    #Separamos para saber si se tiro bien 
    dice_list= dados.split("d")
    if len(dice_list)<2 or len(dice_list)>2:
        await ctx.send("{} El comando que uso, esta mal escrito un ejemplo de uso es:\n <d 1d100".format(ctx.message.author.name))
    else:
        #Guardamos la cantidad de dados 
        quantity, numbers =dice_list[0], dice_list[1]
        #Vemos si es valida la cantidad de dados 
        if not quantity.isnumeric():
            await ctx.send("{} La cantidad de dados debe ser un numero".format(ctx.message.author.name))
        else:
            dice_numbers=numbers.split("+")
            results=[]
            if len(dice_numbers)==1:
                for i in range(int(quantity)):
                    results.append(random.randint(1,int(dice_numbers[0])))
            elif len(dice_numbers)==2:
                for i in range(int(quantity)):
                    results.append(random.randint(1,int(dice_numbers[0]))+int(dice_numbers[1]))
            else:
                await ctx.send("{} Se le puede sumar a lo mas un numero a la tirada de dados".format(ctx.message.author.name))
            await ctx.send(results)
key=os.getenv('key')
bot.run(key)