from bs4 import BeautifulSoup
import requests
import re
import discord
client = discord.Client()

@client.event
async def on_ready():
    print("LOGGED IN AS...........")
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game = discord.Game(name = "$servertime", type = 0))

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('$servertime'):
        data = {}
        link = 'https://www.worldtimeserver.com/current_time_in_US-FL.aspx'
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'lxml')
        time_data = soup.find("span",{"class": "fontTS"}).get_text()
        date_data = soup.find("span",{"class": "font6"}).get_text()
        time_data = time_data.replace(" ","")
        time_data = time_data.replace("\n","")
        date_data = date_data.replace(" ","")
        date_data = date_data.replace("\n","")
        data["time"] = time_data
        data["date"] = date_data
        #print(data["time"]+"\n"+data["date"])
        em = discord.Embed()
        em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/367767323953725443/367957942923952128/the_night_watch_edit_2.png")
        em.set_author(name = "Server", icon_url = "https://designmodo.com/wp-content/uploads/2015/09/webview.gif")
        em.add_field(name = "Time:", value = data["time"],inline = True)
        em.add_field(name = "Date: ", value = data["date"], inline = True)
        em.colour = discord.Colour.green()
        em.set_footer(text = "|Night Watch| requested by {}".format(message.author.name),icon_url = message.author.avatar_url)
        await client.send_message(channel,embed = em)
print("Starting........")
client.run("MzY4MDk4MzY1MzQwMTIzMTM3.DMFB2g.qnukkTvzbb65-KM-yMZfNQ0f-8c")
