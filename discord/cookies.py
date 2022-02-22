# import discord
# import os
# import requests
# import json
# import random
# # from replit import db
# # from keyWords import token
#
# client = discord.Client()
#
# # todo look for a sad list API that you can pull from in the future
# # OR make one from the users
# sad_words = ["sad", "depressed", "unhappy", "angry", "pissed", "upset",
#              "bad day", "fired", "break up"]
#
# # todo Add more
# starter_encouragements = ["Cheer up Big Homie!", "Hang in there!",
#                           "You are a doing an amazing job"]
#
# # todo
# # In the future think of a way to pull quotes from ones posted by users
# def get_quote():
#     response = requests.get("https://zenquotes.io/api/random")
#     json_data = json.loads(response.text)
#     quote = json_data[0]['q'] + " -" + json_data[0]['a']
#     return(quote)
#
# # Lets users addOn more quotes
#
# def update_encouragments (encouraging_message):
#     if "encouragments" in db.keys():
#         encouragments = db["encouragments"]
#         encouragments.append(encouraging_message)
#         db["encouragments"] = encouragments
#     else:
#         db["encouragments"] = [encouraging_message]
#
# def delete_encouragment(index):
#     encouragments = db["encouragments"]
#     if len(encouragments) > index:
#         del encouragments[index]
#     db["encouragments"] = encouragments
#
#
# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
#
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     msg = message.content
#
#     if msg.startswith('$inspire'):
#         quote = get_quote()
#     await message.channel.send(quote)
#
# # todo
#     options = starter_encouragements
#     if "encouragements" in db.keys():
#         options = options + db["encouragements"]
#
#     if any(word in msg for word in sad_words):
#         await message.channel.send(random.choice(starter_encouragements))
#
#     if msg.startwith("$new"):
#         encouraging_message = msg.split("$new ",1)[1]
#         update_encouragments(encouraging_message)
#         await message.channel.send("Thank you, for adding a New encouraging message.")
#
#     if msg.startswith("$del"):
#         encouragments = []
#         if "encouragments" in db.keys():
#             index = int(msg.split("$del", 1)[1])
#             delete_encouragment(index)
#             encouragments = db["encouragemnts"]
#         await message.channel.send(encouragments)
#
#
#
#
# client.run(token)


