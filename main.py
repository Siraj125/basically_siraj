import discord
import random
from replit import db
from keep_alive import keep_alive
import os

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)

if "responding" not in db.keys():
  db["responding"] = True

summon_words = ["hi siraj","hey siraj","wodup siraj","Hey siraj","Hey Siraj","Siraj","siraj"]

starter_greetings = [
  "lol hi", "Hi there", "run", "you dont belong here", "hello bossa",
  "Whatre you doing here???", "wodup nibba", "nigga mans, sup?", "sup?",
  "wodup homeboi"
]


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send("stfu nigga")

  if message.content.startswith('siraj pls curse'):
    await message.channel.send("fuck you you piece of fucking shit head")

  if db["responding"]:
    if any(word in message.content for word in summon_words):
      await message.channel.send(random.choice(starter_greetings))

  if message.content.startswith('$responding'):
    value = message.content.split("$responding ", 1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Heheheh thanks for the unmute xD")
    if value.lower() == "false":
      db["responding"] = False
      await message.channel.send("I will now stfu")


keep_alive()
client.run(os.getenv("TOKEN"))
