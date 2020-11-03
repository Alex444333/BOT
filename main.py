import discord
from discord.ext import commands
from config import settings
bot = commands.Bot(command_prefix = settings['prefix'])
@bot.command()
async def hi(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.

    await ctx.send(f'Hello, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
@bot.command()
async def box(ctx):
    await ctx.send(f'САМ ТЫ КОРОБКА')
@bot.command()
async def ping(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.

    await ctx.send(f'{author.mention}') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
@bot.event
async def on_ready():
    await bot.change_presence(status= discord.Status.idle, activity= discord.Game('&help'))

bot.run(settings['token'])