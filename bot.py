import discord
from discord.ext import commands
import os
import random
from botlogic import get_waste_type
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def genpass(ctx, pass_length: int):
    from botlogic import gen_pass
    password = gen_pass(pass_length)
    await ctx.send(f"Generated password: {password}")

@bot.command()
async def animequote(ctx, anime: str):
    from botlogic import gen_anime_quote
    quote = gen_anime_quote(anime.upper())
    await ctx.send(quote)

# === Command: kirim gambar dari folder images/ ===
@bot.command()
async def meme(ctx, name: str):
    """Kirim gambar dari images/<name>.jpeg"""
    file_path = f"images/{name}.jpeg"
    if not os.path.exists(file_path):
        return await ctx.send(f"Gambar tidak ditemukan: {file_path}")

    with open(file_path, "rb") as f:
        picture = discord.File(f)
        # Kirim ke channel tempat command dipanggil
        await ctx.send(file=picture)

@bot.command()
async def meme_random(ctx):
    # nama_folder/nama_file.extension
    # with open('images/mem1.jpeg', 'rb') as f:
    #     # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
    #     picture = discord.File(f)

    #menyimpan nama nama file di suatu folder dalam variabel lsit
    all_local_images = os.listdir('images')
    img_name = random.choice(all_local_images)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def waste(ctx,*,waste: str):
    '''s'''
    waste_type = get_waste_type(waste)
    await ctx.send(waste_type)

@bot.command()
async def tips(ctx, how_many:int):
    '''Setelah kita memanggil perintah tips, program akan memanggil fungsi get_reduce_waste_tips'''
    tips_list = get_reduce_waste_tips(how_many)
    tips_msg = "\n".join(tips_list)
    await ctx.send(tips_msg)

bot.run("MTQ5OTk4MDY4OTM1NTk2NDU1Ng.GScIJ_.G9qBShHRACL3UfS-TZtmA3UwRb_yV1O91Bg4Bk")
