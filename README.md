# Memebot

A Discord bot that grabs the title + image URL of a random post from any subreddit that supports Python Reddit API Wrapper (PRAW)

# Requirements

1. Reddit account
2. Host (PC, Server, cloud)
3. *Manage Messages* permission on the Discord server in order for the bot to automatically delete the command issued by the user

# Usage

1. Login at [Discord Developers Portal](https://discordapp.com/developers/applications/) and create an application. Click on the created application and go to the **Bot** tab and add a bot. Once the bot is added, copy the token
2. Open **account.json** and paste the token
3. Go to OAuth2 and in *scopes*, click *bot*. Give your bot the *Manage Message* permission and copy the generated OAuth2 URL. Use that link to invite your bot into your Discord server
4. Login your Reddit account, go to [Preferences > Apps](https://www.reddit.com/prefs/apps) and create an application. Note: Choose *script*
5. Copy the client id (13-digit code beside application icon) and *secret* and paste it on the **account.json** file, along with your Reddit username and password
6. Run **Memebot.exe** and your bot should now be online

#Bot Commands

-!subreddit where *subreddit* is any subreddit you want, i.e, funny, memes, etc

# Immportant Notes

1. As of v1, Memebot is a self-hosted Discord bot. Will further update the bot and host it somewhere so you'd just need my invite link
