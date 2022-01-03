import discord
import os
import random

client = discord.Client()

# todo look for a sad list API that you can pull from in the future
# OR make one from the users
sad_words = ["sad", "depressed", "unhappy", "angry", "pissed", "upset",
             "bad day", "fired", "break up"]

# todo Add more
starter_encouragements = ["Cheer up Big Homie!", "Hang in there!",
                          "You are a doing an amazing job"]

# todo
# In the future think of a way to pull quotes from ones posted by users
def get_quote():
    response = request.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

client.run(os.getenv('TOKEN'))
