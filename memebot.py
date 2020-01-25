import discord
import praw
import random
import json

# Reads file where credentials are stored
with open('account.json', 'r') as from_file:
    data = from_file.read()
credentials = json.loads(data)

client = discord.Client()
reddit = praw.Reddit(client_id = credentials['client_id'], client_secret = credentials['client_secret'], username = credentials['username'], password = credentials['password'], user_agent = 'Memebot')

# Checks whenever a message is sent by a user
@client.event
async def on_message(message):
    if message.content.startswith('!'):
        if message.content.find(' ') == -1:
            try:
                result = ''
                subreddit = reddit.subreddit(message.content[1:])
                post = subreddit.random()
                if hasattr(post, 'title'):
                    result += post.title
                if hasattr(post, 'url'):
                    result += '\n' + post.url
                if result is not '':
                    await message.channel.send(result)
                else:
                    await message.channel.send('Subreddit not supported!')
            except Exception:
                await message.channel.send('Subreddit does not exist!')
        try:
            await message.delete()
        except Exception:
            await message.channel.send('Not enough permission to delete user command!')

client.run(credentials['token'])